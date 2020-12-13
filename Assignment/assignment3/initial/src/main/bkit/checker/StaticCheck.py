
"""
 * @author nhphung
"""
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

DEBUG = True
# DEBUG = False


def printEnv(env, stop=False):
    if not DEBUG:
        return
    if stop:
        try:
            input(','.join([str(e) for e in env]))
        except EOFError:
            print(','.join([str(e) for e in env]))
    else:
        print(','.join([str(e) for e in env]))


def printDebug(desc, **kwargs):
    if not DEBUG:
        return

    print(desc)

    if 'env' in kwargs:
        if 'stop' in kwargs:
            printEnv(kwargs['env'], kwargs['stop'])
        else:
            printEnv(kwargs['env'])



class StaticChecker(BaseVisitor):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([FloatType()],IntType())),
Symbol("float_of_int",MType([IntType()],FloatType())),
Symbol("int_of_string",MType([StringType()],IntType())),
Symbol("string_of_int",MType([IntType()],StringType())),
Symbol("float_of_string",MType([StringType()],FloatType())),
Symbol("string_of_float",MType([FloatType()],StringType())),
Symbol("bool_of_string",MType([StringType()],BoolType())),
Symbol("string_of_bool",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([StringType()],VoidType())),
Symbol("printStrLn",MType([StringType()],VoidType()))]    

    def updateType(self, name, new_type, o, isSymbol=False, idx = False):
        if name in o[0]:
            if not isSymbol:
                o[0][name] = new_type
            elif isSymbol == 'ret':
                oldMType = o[0][name].mtype
                newMType = (oldMType[0],new_type)
                o[0][name].mtype = newMType
            elif isSymbol == 'param':
                o[0][name].mtype[0][idx] = new_type
        else:
            if not isSymbol:
                o[1][name] = new_type
            elif isSymbol == 'ret':
                oldMType = o[1][name].mtype
                newMType = (oldMType[1],new_type)
                o[1][name].mtype = newMType
            elif isSymbol == 'param':
                o[1][name].mtype[1][idx] = new_type

        return o
    
    def getType(self, name, o, isSymbol=False, idx=False):
        if not isSymbol:
            return o[0][name] if name in o[0] else o[1][name]

        if isSymbol == 'ret':
            return o[0][name].mtype[1] if name in o[0] else o[1][name].mtype[1]
            
        if isSymbol == 'param':
            return o[0][name].mtype[0][idx] if name in o[0] else o[1][name].mtype[0][idx]


   

    def visitProgram(self,ast, c):
        '''
        ast: decl : List[Decl]
        '''
        global_scope = reduce(
            lambda env, elem:
            self.visit(elem, env), ast.decl,({},{}))

    
    def visitFuncDecl(self, ast, o):
        '''ast
    name: Id
    param: List[VarDecl]
    body: Tuple[List[VarDecl],List[Stmt]]'''
        if ast.name.name in o[0]:
            raise Redeclared(ast)

        outer_env = o[1].copy()
        outer_env.update(o[0])

        new_env = ({},outer_env)
        lst = ast.param + ast.body[0] + ast.body[1]
        reduce(lambda env, elem: self.visit(elem, env), lst, new_env)

        param_type = [self.getType(var.name, new_env) for var in ctx.param]
        s = Symbol(ctx.name, MType(param_type, None))
        o[0][ctx.name] = s

        for name in outer_env:
            if name in new_env[0]:
                continue
            if (not self.getType(name, o)) and (outer_env[name]):
                self.updateType(name, outer_env[name], o)
    
    def visitVarDecl(self, ast, c):
        pass

    def visitIntType(self, ast, param):
        return None
    
    def visitFloatType(self, ast, param):
        return None
    
    def visitBoolType(self, ast, param):
        return None
    
    def visitStringType(self, ast, param):
        return None
    
    def visitVoidType(self, ast, param):
        return None
    
    def visitArrayType(self, ast, param):
        return None

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, env):
        pass

    def visitId(self, ast, param):
        pass

    def visitArrayCell(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass
    
    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitWhile(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()







        
