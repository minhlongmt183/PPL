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


class VarDecl: #name:str, typ: Type
    def __init__(self,name):
        self.name = name
        self.typ = typ
    def accept(self,visitor,param):
        return visitor.visitVarDecl(self,param)
    def __str__(self):
        return """{}("{}{}")""".format("VarDecl",self.name, self.typ)

class ConstDecl: #name:str,val:Lit
    def __init__(self,name):
        self.name = name
        self.val = val
    def accept(self,visitor,param):
        return visitor.visitConstDecl(self,param)
    def __str__(self):
        return """{}("{}{}")""".format("ConstDecl",self.name, self.val)

class FuncDecl: #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def __init__(self, name, param, body):
        self.name = name
        self.param = param
        self.body = body
    def accept(self, visitor, param):
        return visitor.visitFuncDecl(self, param)
    
    def __str__(self):
        return """{}("{}{}{}")""".format("FuncDecl",self.name, self.param, self.body)


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

    def visitProgram(self,ctx:Program,o:object):
        #decl:List[Decl]
        env = reduce(lambda acc, ele: self.visit(ele, acc), ctx.decl, {})

    def visitVarDecl(self,ctx:VarDecl,o:object):
        #name:str,typ:Type
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o[ctx.name] = ctx.typ
        return o

    def visitConstDecl(self,ctx:ConstDecl,o:object):
         #name:str,val:Lit
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        o[ctx.name] = ctx.val
        return o
        

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
        
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        reduce(lambda acc, ele: self.visit(ele, acc), ctx.param + ctx.body, {})
        o[ctx.name] = None
        return o
            

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o


class StaticError(Exception):
    pass

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

StaticCheck().visitProgram(Program([VarDecl("a",IntType()),ConstDecl("b",IntLit(3)),FuncDecl("a",[],([],[]))])
, None
)
