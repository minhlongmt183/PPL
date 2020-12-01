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

class Symbol:
    def __init__(self, name, tp = None):
        self.name = name
        self.tp = tp
def check_and_set(sym, tp):
    if sym.tp is None:
        sym.tp = tp
def get_type(obj):
    if type(obj) is Symbol:
        return obj.tp
    return obj


class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):
        reduce(lambda env, ele: ele.accept(self, env), ctx.decl + ctx.stmts, ([], []))
    def visitVarDecl(self,ctx:VarDecl,o):
        if any(ctx.name == s.name for s in o[0]):
            raise Redeclared(ctx)
        return o[0] + [Symbol(ctx.name)], o[1]
    def visitBlock(self,ctx:Block,o): 
        new_env = ([], o[0] + o[1])
        reduce(lambda env, ele: ele.accept(self, env), ctx.decl + ctx.stmts, new_env)
        return o
    def visitAssign(self,ctx:Assign,o):
        right = ctx.rhs.accept(self, o)
        left = ctx.lhs.accept(self, o)
        if type(right) is Symbol:
            if left.tp and right.tp and left.tp != right.tp:
                raise TypeMismatchInStatement(ctx)
            elif not left.tp and not right.tp:
                raise TypeCannotBeInferred(ctx)
            elif not left.tp:
                check_and_set(left, right.tp)
            else:
                check_and_set(right, left.tp)
        else:
            if left.tp and left.tp != right:
                raise TypeMismatchInStatement(ctx)
            elif not left.tp:
                check_and_set(left, right)
        return o
    def visitBinOp(self,ctx:BinOp,o):
        op = ctx.op
        left = ctx.e1.accept(self, o)
        right = ctx.e2.accept(self, o)
        if op in '+-*/>=':
            if type(left) is Symbol:
                check_and_set(left, int)
            if type(right) is Symbol:
                check_and_set(right, int)
            if get_type(left) is int and get_type(right) is int:
                if op in '>=':
                    return bool
                return int
        elif op in ['+.', '-.', '*.', '/.', '>.', '=.']:
            if type(left) is Symbol:
                check_and_set(left, float)
            if type(right) is Symbol:
                check_and_set(right, float)
            if get_type(left) is float and get_type(right) is float:
                if op in ['>.', '=.']:
                    return bool
                return float
        elif op in ['&&', '||', '>b', '=b']:
            if type(left) is Symbol:
                check_and_set(left, bool)
            if type(right) is Symbol:
                check_and_set(right, bool)
            if get_type(left) is bool and get_type(right) is bool:
                return bool
        raise TypeMismatchInExpression(ctx)
            
    def visitUnOp(self,ctx:UnOp,o):
        op = ctx.op
        exp = ctx.e.accept(self, o)
        if op == '-':
            if type(exp) is Symbol:
                check_and_set(exp, int)
            if get_type(exp) is int:
                return int
        elif op == '!':
            if type(exp) is Symbol:
                check_and_set(exp, bool)
            if get_type(exp) is bool:
                return bool
        elif op == '-.':
            if type(exp) is Symbol:
                check_and_set(exp, float)
            if get_type(exp) is float:
                return float
        elif op == 'i2f':
            if type(exp) is Symbol:
                check_and_set(exp, int)
            if get_type(exp) is int:
                return float
        elif op == 'floor':
            if type(exp) is Symbol:
                check_and_set(exp, float)
            if get_type(exp) is float:
                return int
        raise TypeMismatchInExpression(ctx)
            
    def visitIntLit(self,ctx:IntLit,o): return int
    def visitFloatLit(self,ctx,o): return float
    def visitBoolLit(self,ctx,o): return bool
    def visitId(self,ctx,o):
        id = list(filter(lambda x: x.name == ctx.name, o[0] + o[1]))
        if not id:
            raise UndeclaredIdentifier(ctx.name)
        return id[0]


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

StaticCheck().visitProgram(Program([VarDecl("x"), VarDecl("y")],[Assign(Id("x"),IntLit(3)),Block([VarDecl("y")],[Assign(Id("x"),Id("y"))]),Assign(Id("y"),BoolLit(True))])

,
    None
)
