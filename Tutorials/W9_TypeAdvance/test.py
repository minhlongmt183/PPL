from functools import reduce
from abc import ABC
from dataclasses import dataclass


class Visitor(ABC):
    def visit(self,ctx,o):
        return ctx.accept(self, o)

class Program: #decl:List[VarDecl],stmts:List[Assign]
    def __init__(self,decl,stmts):
        self.decl,self.stmts = decl,stmts
    def accept(self,visitor,param):
        return visitor.visitProgram(self,param)
    def __str__(self):
        return "{}([{}],[{}])".format("Program",",".join([str(i) for i in self.decl],",".join([str(i) for i in self.stmts])))

class Block: #decl:List[VarDecl],stmts:List[Stmt]
    def __init__(self,decl,stmts):
        self.decl,self.stmts = decl,stmts
    def accept(self,visitor,param):
        return visitor.visitBlock(self,param)
    def __str__(self):
        return "{}([{}],[{}])".format("Block",",".join([str(i) for i in self.decl],",".join([str(i) for i in self.stmts])))
    

class VarDecl: #name:str
    def __init__(self,name):
        self.name = name
    def accept(self,visitor,param):
        return visitor.visitVarDecl(self,param)
    def __str__(self):
        return """{}("{}")""".format("VarDecl",self.name)

class FuncDecl:
    #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def __init__(self,name, param, local, stmts):
        self.name   = name
        self.param  = param
        self.local  = local
        self.stmts  = stmts

    def accept(self,visitor,param):
        return visitor.visitFuncDecl(self,param)
    def __str__(self):
        return """{}("{},{}")("{}")""".format("FuncDecl",self.name, self.param, self.local, self.stmts)

class CallStmt: #name:str,args:List[Exp]
    def __init__(self,name, args):
        self.name   = name
        self.args   = args

    def accept(self,visitor,param):
        return visitor.visitCallStmt(self,param)
    def __str__(self):
        return """{}("{}")""".format("CallStmt",self.name, self.args)



class Assign: #lhs:Id,rhs:Exp
    def __init__(self,lhs,rhs):
        self.lhs,self.rhs = lhs,rhs
    def accept(self,visitor,param):
        return visitor.visitAssign(self,param)
    def __str__(self):
        return """{}({},{})""".format("Assign",str(self.lhs),str(self.rhs))

class Exp(ABC): #abstract class
    pass

class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def __init__(self,op,e1,e2):
        self.op,self.e1,self.e2 = op,e1,e2
    def accept(self,visitor,param):
        return visitor.visitBinOp(self,param)
    def __str__(self):
        return """{}("{}",{},{})""".format("BinOp",self.op,str(self.e1),str(self.e2))


class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    def __init__(self,op,e):
        self.op,self.e =op,e
    def accept(self,visitor,param):
        return visitor.visitUnOp(self,param)
    def __str__(self):
        return """{}("{}",{})""".format("UnOp",self.op,str(self.e))

class IntLit(Exp): #val:int
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitIntLit(self,param)
    def __str__(self):
        return "{}({})".format("IntLit",str(self.val))

class FloatLit(Exp): #val:float
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitFloatLit(self,param)
    def __str__(self):
        return "{}({})".format("FloatLit",str(self.val))

class BoolLit(Exp): #val:bool
    def __init__(self,val):
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitBoolLit(self,param)

    def __str__(self):
        return "{}({})".format("BoolLit",str(self.val))

class Id(Exp): #name:str
    def __init__(self,name):
        self.name = name
    def accept(self,visitor,param):
        return visitor.visitId(self,param)
    def __str__(self):
        return "{}({})".format("Id",str(self.name))

class Type(ABC): #abstract class
    pass
class IntType(Type): pass

class FloatType(Type): pass

class BoolType(Type): pass




class StaticCheck(Visitor):

    def updateType(self, name, new_type, o):
        if name in o[0]:
            o[0][name] = new_type
        else:
            o[1][name] = new_type
        
        return o
    
    def getType(self, name, o):
        return o[0][name] if name in o[0] else o[1][name]

    def visitProgram(self,ctx:Program,o):
        #decl:List[Decl],stmts:List[Stmt]
        reduce(lambda env, elem: self.visit(elem, env), ctx.decl + ctx.stmts, ({},{}))

    def visitVarDecl(self,ctx:VarDecl,o): 
        #name:str
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        
        o[0][ctx.name] = None
        return o


    def visitFuncDecl(self,ctx:FuncDecl,o):
        #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
        if ctx.name in o[0]:
            raise Redeclared(ctx)
        
        outer_env = o[1].copy()
        outer_env.update(o[0])
        
        new_env = ({},outer_env)
        reduce(lambda env, elem: self.visit(elem, env), ctx.param + ctx.local + ctx.stmts, new_env)

        param_type = [self.getType(var.name, new_env) for var in ctx.param]
        o[0][ctx.name] = param_type

        for name in outer_env:
            if name in new_env[0]:
                continue

            if (not self.getType(name, o)) and (outer_env[name]):
                self.updateType(name, outer_env[name], o)

        return o



    def visitCallStmt(self,ctx:CallStmt,o):
        # name:str,args:List[Exp]
        if (ctx.name not in o[0]) and (ctx.name not in o[1]):
            raise UndeclaredIdentifier(ctx.name)
        
        param_type  = self.getType(ctx.name, o)
        arg_type    = [self.visit(arg, o) for arg in ctx.args]

        if (type(param_type) is list) and (len(arg_type) != len(param_type)):
            raise TypeMismatchInStatement(ctx)
        
        for i in range(len(arg_type)):
            if (not param_type[i]) and (not arg_type[i]):
                raise TypeCannotBeInferred(ctx)
            elif not param_type[i]:
                param_type[i] = arg_type[i]
                self.updateType(ctx.name,param_type, o)
            elif (not arg_type[i]):
                self.updateType(ctx.args[i].name, param_type[i], o)
            elif type(arg_type[i]) != type(param_type[i]):
                raise TypeMismatchInStatement(ctx)
        
        return o



    def visitAssign(self,ctx:Assign,o):
        #lhs:Id,rhs:Exp
        exp_type    = self.visit(ctx.rhs, o)
        id_type     = self.visit(ctx.lhs, o)

        if (not id_type) and (not exp_type):
            raise TypeCannotBeInferred(ctx)

        elif not id_type:
            self.updateType(ctx.lhs.name, exp_type, o)
            
        elif not exp_type:
            self.updateType(ctx.rhs.name, id_type, o)
                
        elif type(id_type) != type(exp_type):
            raise TypeMismatchInStatement(ctx)

        return o

    def visitIntLit(self,ctx:IntLit,o):
        return IntType()

    def visitFloatLit(self,ctx,o):
        return FloatType()

    def visitBoolLit(self,ctx,o):
        return BoolType()

    def visitId(self, ctx, o):
        if ctx.name not in o[0] and ctx.name not in o[1]:
            raise UndeclaredIdentifier(ctx.name)
            
        return self.getType(ctx.name, o)



class StaticError(Exception):
    pass

@dataclass
class Redeclared(StaticError):
    target: object
    def __str__(self):
        return "Redeclare " + str(self.target)

@dataclass
class UndeclaredIdentifier(StaticError):
    target: object
    def __str__(self):
        return  "Undeclared variable "+ str(self.target)

@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Exp

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Assign

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Assign

    def __str__(self):
        return "Type Cannot Be Inferred: "+ str(self.stmt)

StaticCheck().visitProgram(Program([VarDecl("x"), VarDecl("y"),FuncDecl("foo",[],[],[Assign(Id("x"),FloatLit(2))])],[CallStmt("foo",[]), Assign(Id("x"), Id("y"))])

,
    None
)
