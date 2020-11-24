from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
import functools


class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value


def checkRedeclared(listDecl, decl, kind):
    if type(kind) in [Parameter, Variable]:
        if any(de.name == decl.variable.name.lower() for de in listDecl):
                raise Redeclared(kind, decl.variable.name)
        return Symbol(decl.variable.name.lower(), decl.varType)
        
    if any(de.name == decl.name.name.lower() for de in listDecl):
        raise Redeclared(kind, decl.name.name)
    
    return Symbol(decl.name.name.lower(), MType([x.varType for x in decl.param], decl.returnType))

def checkValidAssign(left, right):
    if type(left) is VoidType or type(right) is VoidType:
        return False
    
    if type(left) is ArrayType or type(right) is ArrayType:
        return False
        
    if type(left) is StringType or type(right) is StringType:
        return False
        
    _validAssign = [(BoolType, BoolType), (FloatType, FloatType), (FloatType, IntType), (IntType, IntType)]

    return (type(left), type(right)) in _validAssign
    
def checkValidParse(left, right):
    if type(left) is VoidType or type(right) is VoidType:
        return False
        
    if type(left) is ArrayType and type(right) is ArrayType:
        if left.lower != right.lower or\
           left.upper != right.upper or\
           type(left.eleType) != type(right.eleType):
            return False
        return True
        
    _validParse = [(StringType, StringType), (BoolType, BoolType), (FloatType, FloatType), (FloatType, IntType), (IntType, IntType)]
    
    return (type(left), type(right)) in _validParse
    
def checkValidOperation(left, right):
    if (type(left), type(right)) == (IntType, IntType):
        return IntType()
    if (type(left), type(right)) in [(IntType, FloatType), (FloatType, IntType), (FloatType, FloatType)]:
        return FloatType()
    return None
    
def overrideDeclaration(refenv, name):
    [refenv.remove(id) for id in refenv if id.name == name.lower()]
    
    
class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getint",MType([],IntType())),
    			   Symbol("putintln",MType([IntType()],VoidType())),
                   Symbol("putint", MType([IntType()], VoidType())),
                   Symbol("getfloat", MType([], FloatType())),
                   Symbol("putfloat", MType([FloatType()], VoidType())),
                   Symbol("putfloatln", MType([FloatType()], VoidType())),
                   Symbol("putbool", MType([BoolType()], VoidType())),
                   Symbol("putboolln", MType([BoolType()], VoidType())),
                   Symbol("putstring", MType([StringType()], VoidType())),
                   Symbol("putstringln", MType([StringType()], VoidType())),
                   Symbol("putln", MType([], VoidType()))]
    
#    global_envi = []

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        _referenceEnvironment = c.copy()
        _returnType = None
        _isLoop = False
        _reachableFunctions = {}
        _isMainCall = False
        
        _entryPoint = False

        for decl in ast.decl:
            _referenceEnvironment.append(checkRedeclared(_referenceEnvironment, decl, Variable() if type(decl) is VarDecl else Procedure() if type(decl.returnType) is VoidType else Function()))
            if type(decl) is FuncDecl:
                _entryPoint = decl.name.name == "main" if not _entryPoint else _entryPoint
                _reachableFunctions[decl.name.name.lower()] = decl.name.name == "main"

        if not _entryPoint:
            raise NoEntryPoint()

        for decl in ast.decl:
            if not type(decl) is VarDecl:
                #print(type(ast.decl))
                self.visit(decl, (_referenceEnvironment, _returnType, _isLoop, _reachableFunctions, _isMainCall))

        for func in _reachableFunctions:
            if not _reachableFunctions[func]:
                _func = self.lookup(func.lower(), _referenceEnvironment, lambda x: x.name)
                ftype = Procedure() if type(_func.mtype.rettype) is VoidType else Function()
                raise Unreachable(ftype, func)

        return None

    def visitVarDecl(self, ast, c):
        _local = c[0]
        _type = c[1]
        _refenv = c[2]
        _local.append(checkRedeclared(_local, ast, c[1]))
        overrideDeclaration(_refenv, ast.variable.name)
        return None

    def visitFuncDecl(self, ast, c):
        _refenv = c[0].copy()
        _returnType = ast.returnType
        _isMainCall = c[4]
        _isEnd = 0

        if ast.name.name == "main":
            _isMainCall = True

        _local = []
        [self.visit(param, (_local, Parameter(), _refenv)) for param in ast.param]
        [self.visit(local, (_local, Variable(), _refenv)) for local in ast.local]
        
        _refenv += _local
        
        _isEnd = self.visitBlockStmt(ast.body, (_refenv, _returnType, c[2], c[3], _isMainCall))

        if _isEnd != 1 and not type(_returnType) is VoidType:
            raise FunctionNotReturn(ast.name.name)

        return None

    def visitBlockStmt(self, ls, c):
        _isEnd = 0
        
        for stmt in ls:
            if _isEnd:
                raise UnreachableStatement(stmt)
            _isEnd = self.visit(stmt, c)

        return _isEnd

    def visitAssign(self, ast, c):
        _refenv = c[0].copy()
        
        if not type(ast.lhs) in [Id, ArrayCell]:
            raise TypeMismatchInStatement(ast)
            
        _lhsType = self.visit(ast.lhs, (_refenv, c[1], c[2], c[3], c[4]))
        _rhsType = self.visit(ast.exp, (_refenv, c[1], c[2], c[3], c[4]))
        
        if not checkValidAssign(_lhsType, _rhsType):
            raise TypeMismatchInStatement(ast)
            
        return 0

    def visitFor(self, ast, c):
        _refenv = c[0].copy()

        _id = self.visit(ast.id, (_refenv, c[1], c[2], c[3], c[4]))
        if not type(_id) is IntType:
            raise TypeMismatchInStatement(ast)

        _exp1 = self.visit(ast.expr1, (_refenv, c[1], c[2], c[3], c[4]))
        if not type(_exp1) is IntType:
            raise TypeMismatchInStatement(ast)

        _exp2 = self.visit(ast.expr2, (_refenv, c[1], c[2], c[3], c[4]))
        if not type(_exp2) is IntType:
            raise TypeMismatchInStatement(ast)

        _isEnd = 0
        for stmt in ast.loop:
            if _isEnd != 0:
                raise UnreachableStatement(stmt)
            _isEnd = self.visit(stmt, (_refenv, c[1], True, c[3], c[4]))
            
        _isEnd = self.visitBlockStmt(self, ast.loop, c)

        if _isEnd != 1 and not type(_returnType) is VoidType:
            raise FunctionNotReturn(ast.name.name)

            
        return 0
        
    def visitCallStmt(self, ast, c):
        try:
            self.visitCallBody(ast, (c[0], c[1], c[2], c[3], c[4], Procedure()))
        except:
            raise TypeMismatchInStatement(ast)
        return 0

    def visitCallBody(self, ast, c):
        _refenv = c[0].copy()
        _isMainCall = c[4]
        _type = c[5]
        
        _param = [self.visit(x, (_refenv, c[1], c[2], c[3], c[4])) for x in ast.param]
        _func = self.lookup(ast.method.name.lower(), _refenv, lambda x: x.name)
        
        if _func is None or not type(_func.mtype) is MType:
            raise Undeclared(c[5], ast.method.name)
        
        if (not type(_func.mtype.rettype) is VoidType and type(c[5]) is Procedure) or (type(_func.mtype.rettype) is VoidType and type(c[5]) is Function):
            raise Undeclared(c[5], ast.method.name)
        
        if len(_func.mtype.partype) != len(_param):
            raise TypeMismatchInStatement(ast)
        
        if not all([checkValidParse(_func.mtype.partype[i], _param[i]) for i in range(len(_param))]):
            raise TypeMismatchInStatement(ast)
        
        if _isMainCall:
            c[3][ast.method.name.lower()] = True
        
        return _func.mtype.rettype
        
        
    def visitBinaryOp(self, ast, c):
        _refenv = c[0].copy()
        
        leftType = self.visit(ast.left, (_refenv, c[1], c[2], c[3], c[4]))
        rightType = self.visit(ast.right, (_refenv, c[1], c[2], c[3], c[4]))
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
                return BoolType()
            raise TypeMismatchInExpression(ast)
            
        if op in ["div", "mod"]:
            if (type(leftType), type(rightType)) == (IntType, IntType):
                return IntType()
            raise TypeMismatchInExpression(ast)
            
        raise TypeMismatchInExpression(ast)
        
    def visitUnaryOp(self, ast, c):
        _refenv = c[0].copy()
        expType = self.visit(ast.body, (_refenv, c[1], c[2], c[3], c[4]))
        op = ast.op
        if op == "-":
            if type(expType) in [IntType, FloatType]:
                return expType
            raise TypeMismatchInExpression(ast)
        if op == "not":
            if type(expType) is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        try:
            ret = self.visitCallBody(ast, (c[0], c[1], c[2], c[3], c[4], Function()))
        except:
            raise TypeMismatchInExpression(ast)
        return ret

    def visitId(self, ast, c):
        _refenv = c[0].copy()
        id = self.lookup(ast.name.lower(), _refenv, lambda x: x.name)
        if id is None:
            raise Undeclared(Identifier(), ast.name)
        if type(id.mtype) is MType:
            if (c[4]):
                c[3][ast.name.lower()] = True
            return id.mtype.rettype
        return id.mtype
        
    def visitArrayCell(self, ast, c):
        _refenv = c[0].copy()
        
        if not type(ast.arr) is Id and not type(ast.arr) is CallExpr:
            raise TypeMismatchInExpression(ast)
        
        _arr = self.lookup(ast.arr.name.lower() if type(ast.arr) is Id else ast.arr.method.name, _refenv, lambda x: x.name)
        #_arr = self.visit(ast.arr, (_refenv, c[1], c[2], c[3], c[4]))
        if _arr is None:
            if type(ast.arr) is Id:
                raise Undeclared(Identifier(), ast.arr)
            else:
                raise Undeclared(Function(), ast.arr.method.name)
        
        _idx = self.visit(ast.idx, (_refenv, c[1], c[2], c[3], c[4]))
        
        if not type(_idx) is IntType:
            raise TypeMismatchInExpression(ast)
        
        if type(_arr.mtype) is MType:
            if (c[4]):
                c[3][_arr.name.lower()] = True
            return _arr.mtype.rettype.eleType
        
        if not type(_arr.mtype) is ArrayType:
            raise TypeMismatchInExpression(ast)
        
        return _arr.mtype.eleType
        
    def visitBreak(self, ast, c):
        _isLoop = c[2]
        
        if not _isLoop:
            raise BreakNotInLoop()
            
        return 2
        
    def visitContinue(self, ast, c):
        _isLoop = c[2]
        
        if not _isLoop:
            raise ContinueNotInLoop()
        
        return 2
        
    def visitReturn(self, ast, c):
        _refenv = c[0].copy()
        _returnType = c[1]
        
        if ast.expr is None:
            if type(_returnType) is VoidType:
                return 1
            raise TypeMismatchInStatement(ast)
        
        if checkValidParse(_returnType, self.visit(ast.expr, (_refenv, c[1], c[2], c[3], c[4]))):
            return 1
        raise TypeMismatchInStatement(ast)
        
    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()
        