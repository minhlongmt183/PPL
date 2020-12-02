
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

def checkRedeclaration(listDecl, decl, kind):
    if kind == "Variable":
        if any(de.name == decl.variable.name for de in listDecl):
            raise Redeclared(Variable(), decl.variable.name)
        else:
            return Symbol(decl.variable.name, decl.varType)
    
    if kind == "Parameter":
        if any(de.name == decl.variable.name for de in listDecl):
            raise Redeclared(Parameter(), decl.variable.name)
        else:
            return Symbol(decl.variable.name, decl.varType)
    
    if any(de.name == decl.name.name for de in listDecl):
        if type(decl.returnType) is VoidType:
            raise Redeclared(Procedure(), decl.name.name)
        else:
            raise Redeclared(Function(), decl.name.name)
    return Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType))

def checkValidAssign(left, right):
    if type(left) is VoidType or type(left) is ArrayType or type(left) is StringType:
        return False
    
    _validAssign = [(BoolType, BoolType), (FloatType, FloatType), (FloatType, IntType), (IntType, IntType)]
    return (type(left), type(right)) in _validAssign
        
def checkValidOperation(left, right):
    if (type(left), type(right)) == (IntType, IntType):
        return IntType()
    if (type(left), type(right)) in [(IntType, FloatType), (FloatType, IntType), (FloatType, FloatType)]:
        return FloatType()
    return None
        

def overrideDeclaration(refenv, name):
    [refenv.remove(id) for id in refenv if id.name == name]
        
class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType())),
                   Symbol("putInt", MType([IntType()], VoidType())),
                   Symbol("getFloat", MType([], FloatType())),
                   Symbol("putFloat", MType([FloatType()], VoidType())),
                   Symbol("putFloatLn", MType([FloatType()], VoidType())),
                   Symbol("putBool", MType([BoolType()], VoidType())),
                   Symbol("putBoolLn", MType([BoolType()], VoidType())),
                   Symbol("putString", MType([StringType()], VoidType())),
                   Symbol("putStringLn", MType([StringType()], VoidType())),
                   Symbol("putLn", MType([], VoidType()))]

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c): 
        _env = c.copy()
        
        for _decl in ast.decl:
            _env.append(checkRedeclaration(_env, _decl, "Variable" if type(_decl) is VarDecl else "Function"))
        
        for _decl in ast.decl:
            self.visit(_decl, _env)

        return None

    def visitVarDecl(self, ast, c):
        pass

    def visitFuncDecl(self,ast, c):
        _env = c.copy()
        _localVar = [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType))]
        overrideDeclaration(_env, ast.name.name)
        
        for _param in ast.param:
            _localVar.append(checkRedeclaration(_localVar, _param, "Parameter"))
            overrideDeclaration(_env, _param.variable.name)
        
        for _local in ast.local:
            _localVar.append(checkRedeclaration(_localVar, _local, "Variable"))
            overrideDeclaration(_env, _local.variable.name)

        _env += _localVar

        for _st in ast.body:
            self.visit(_st, _env)

        return None

    def visitCallStmt(self, ast, c): 
        _env = c.copy()
        at = [self.visit(x, _env) for x in ast.param]
        
        res = self.lookup(ast.method.name, _env, lambda x: x.name)

        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        if len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)   
        for i in range(len(at)):
            if not checkValidAssign(res.mtype.partype[i], at[i]):
                raise TypeMismatchInStatement(ast)

        return None

    def visitBinaryOp(self, ast, c):
        _env = c.copy()
        leftType = self.visit(ast.left, _env)
        rightType = self.visit(ast.right, _env)
        op = ast.op
        
        if op in ["+", "-", "*"]:
            rtype = checkValidOperation(leftType, rightType)
            if rtype is None:
                raise TypeMismatchInExpression(ast)
            return rtype

        if op == "/":
            rtype = checkValidOperation(leftType, rightType)
            if rtype is None:
                raise TypeMismatchInExpression(ast)
            return FloatType()

        if op in ["<", ">", "<=", ">=", "=", "<>"]:
            rtype = checkValidOperation(leftType, rightType)
            if rtype is None:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        if op in ["and", "or", "andthen", "orelse"]:
            if (type(leftType), type(rightType)) == (BoolType, BoolType):
                return BoolType
            raise TypeMismatchInExpression(ast)

        if op in ["div", "mod"]:
            if (type(leftType), type(rightType)) == (IntType, IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)

        return None

    def visitUnaryOp(self, ast, c):
        _env = c.copy()
        rtype = self.visit(ast.body, _env)
        if ast.op == "-":
            if type(rtype) in [IntType, FloatType]:
                return rtype
            raise TypeMismatchInExpression(ast)
        if ast.op == "not":
            if rtype is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
            
        return None

    def visitCallExpr(self, ast, c):
        _env = c.copy()
        _func = self.lookup(ast.method.name, _env, lambda x: x.name)
        _listParam = [self.visit(x, _env) for x in ast.param]
        
        if type(_func.mtype.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        
        if len(_func.mtype.partype) != len(_listParam):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(_listParam)):
            if not checkValidAssign(_func.mtype.partype[i], _listParam[i]):
                raise TypeMismatchInExpression(ast)
        
        return _func.mtype.rettype

    def visitId(self, ast, c):
        id = self.lookup(ast.name, c, lambda x: x.name)
        if id is None:
            raise Undeclared(Identifier(), ast.name)
        if type(id.mtype) is MType:
            return id.mtype.rettype
        return id.mtype

    def visitArrayCell(self, ast, c):
        _env = c.copy()
        arrType = self.visit(ast.arr, _env)
        return arrType.eleType

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()