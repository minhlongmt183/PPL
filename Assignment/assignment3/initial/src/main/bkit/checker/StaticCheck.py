
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

    def check(self):
        return self.visit(self.ast,self.global_envi)
    
    def checkRedeclared(self, symbol, kind, env):
        res = list(filter(lambda e: symbol.name == e.name, env))
        if res is not None:
            raise Redeclared(kind, symbol.name)

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


   

    def visitProgram(self,ast, env):
        printDebug("======SCAN PROGRAM======")
        global_scope = reduce(
            lambda returnList, decl:
                [self.visit(
                    decl,
                    {'env': returnList, 'scan': False}
                )] + returnList,
            ast.decl,
            env[:]
        )
        printDebug("======GLOBAL======", env=global_scope)

        if not any(map(
            lambda symbol: isinstance(
                symbol.mtype,
                MType) and symbol.name == 'main' and isinstance(
                    symbol.mtype[1],
                    VoidType) and len(symbol.mtype[0]) == 0,
                global_scope)):
            raise NoEntryPoint()
            
        funcs = filter(lambda x: isinstance(x, FuncDecl), ast.decl)

        for func in funcs:
            self.visit(func, {'env': global_scope, 'scan': True})

        for symbol in global_scope:
            if not isinstance(symbol.mtype, MType):
                continue
            if symbol.name == 'main' and \
                    isinstance(symbol.mtype[1], VoidType):
                continue

        return global_scope

    
    def visitFuncDecl(self, ast, param):
        '''
        ast: FuncDecl{
            name: Id
            param: List[VarDecl]
            body: Tuple[List[VarDecl],List[Stmt]]
        }
        param: {
            env: List[Symbol], # Global Reference Environment
            scan: Bool
        }
        raise Redeclared(Parameter)
        raise Redeclared(Variable)
        => Symbol if not scan else None
        '''

        env = param['env']
        scan = param['scan']

        if not scan:
            printDebug("FUNCDECL", env=env, stop=False)
            param_type = reduce(
                    lambda scope, vardecl:
                        [self.visit(vardecl, {'env': scope})] + scope,
                    ast.param,
                    []
                    )

            s = Symbol(
                ast.name.name,
                MType(
                    param_type,
                    VoidType
                ))
                
            self.checkRedeclared(s, Function(), env)
            return s
        else:
            printDebug("========SCAN FUNC========")
            printDebug(str(ast))

            try:
                # visits VarDecl -- throws Redeclared(Variable)
                parameter = reduce(
                    lambda scope, vardecl:
                        [self.visit(vardecl, {'env': scope})] + scope,
                    ast.param,
                    []
                )
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
            printDebug("PARAM", env=parameter)

            # visits VarDecl -- throws Redeclared(Variable)
            local_scope = reduce(
                lambda scope, vardecl:
                    [self.visit(vardecl, {'env': scope})] + scope,
                ast.local,
                parameter  # for safety reason, copy
            )
            printDebug("LOCAL_VAR", env=local_scope)
            # self.mergeGlobal2Local(local_scope, env)
            local_scope += env
            printDebug("LOCAL_ENV", env=local_scope, stop=False)


    
    def visitVarDecl(self, ast, c):
        '''
        ast: VarDecl{
            
            variable : Id
            varDimen : List[int] # empty list for scalar variable
            varInit  : Literal   # null if no initial
        }
        param: {
            env: List[Symbol]
            ~~scan: Bool~~ # ignore
        }
        => Symbol
        '''
        env = param['env']
        printDebug("VARDECL", env=env, stop=False)

        s = Symbol(
            ast.variable.name,
            self.visit(ast.varInit, c)
        )

        self.checkRedeclared(s, Variable(), env)

        return s


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
        '''
        ast: BinaryOp{
                op:str
                left:Expr
                right:Expr
                }
        param: list[Symbol]
        raise TypeMismatchInExpression
            (+,-,*, \, %): (Int,Int)=>Int
            (+., -., *., \.): (Float, Float) => Float
            (==, !=, <,>, <=,>=): (Int, Int) => Bool
            (=/=, <., >., <=., >=.): (Float, Float) => Bool
        => Type
        '''

        op = ast.op
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)

        def deferType(acceptableTypes, returnType=None):
            if isinstance(left_type, VoidType):
                left_type = acceptableTypes
                self.updateType(ast.left, acceptableTypes, param)
            
            if isinstance(right_type, VoidType):
                right_type = acceptableTypes
                self.updateType(ast.right, acceptableTypes, param)

            if not isinstance(left_type, acceptableTypes):
                raise TypeMismatchInExpression(ast)
            if not isinstance(right_type, acceptableTypes):
                raise TypeMismatchInExpression(ast)

            if returnType is not None:
                return returnType
            if isinstance(left_type, FloatType) or \
                    isinstance(right_type, FloatType):
                return FloatType()
            if isinstance(left_type, type(right_type)):
                return left_type

            raise TypeMismatchInExpression(ast)
    
        if op in ('+','-','*', '\\',' %'):
            return deferType((IntType), IntType())

        if op in ('+.','-.','*.', '\\.'):
            return deferType((FloatType), FloatType())

        if op in ('==', '!=', '<','>', '<=','>='):
            return deferType((IntType), BoolType())

        if op in ('=/=', '<.', '>.', '<=.', '>=.'):
            return deferType((FloatType), BoolType())

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, env):
        pass

    def visitId(self, ast, o):
        '''
        ast: ID
        o: List[Symbol] or {
            'env': List[Symbol]
            'kind': kind
        }
        raise Undeclared
    => Type: Symbol.mtype
        '''
        env = o['env'] if not isinstance(o, list) else o
        kind = o['kind'] if not isinstance(o, list) else Identifier()

        res = list(filter(lambda e: ast.name == e.name, env))

        if len(res) == 0:
            raise Undeclared(kind, ast.name)

        if isinstance(kind, Identifier):
            if isinstance(res.mtype, MType):
                raise Undeclared(kind, ast.name)
            return res.mtype
    
        # param is dict
        if isinstance(kind, Function):
            # check if mtype -- aka function
            if not isinstance(res.mtype, MType):
                raise Undeclared(kind, ast.name)

            if isinstance(kind, Function):
                if isinstance(res.mtype[1], VoidType):
                    raise Undeclared(kind, ast.name)
            return res.mtype


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







        
