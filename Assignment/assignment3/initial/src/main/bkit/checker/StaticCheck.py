
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
        if len(res) > 0:
            raise Redeclared(kind, symbol.name)

    def updateType(self, symbol, new_type, param):
        oldType = symbol.mtype
        newType = (oldType[0],new_type)
        symbol.mtype = newType
    
    def getType(self, name, o, isSymbol=False, idx=False):
        if not isSymbol:
            return o[0][name] if name in o[0] else o[1][name]

        if isSymbol == 'ret':
            return o[0][name].mtype.restype if name in o[0] else o[1][name].mtype.restype

        if isSymbol == 'param':
            return o[0][name].mtype[0][idx] if name in o[0] else o[1][name].mtype[0][idx]

    def callBody(self, ast, env):
        '''
        ast: CallStmt
        env: List[Symbol]
        raise TypeMismatchInStatement | TypeMismatchInExpression
        => Type: MType
        ; Used by CallStmt and CallExpr
        ; Both have exact structure difference only on
        ; Raising Error and Kind Expectation
        '''    
        callParam = [self.visit(x, env) for x in ast.param]
 

        mtype = self.visit(  # visits Id
            ast.method,
            {
                'env': env,
                'kind': Function() 
            }
        )
        rightParam = mtype.intype

        error = TypeMismatchInExpression if isinstance(ast, CallExpr) \
            else TypeMismatchInStatement
        
        if len(rightParam) != len(callParam):
            raise error(ast)
        
        for pair in zip(rightParam, callParam):
            lhs = pair[0]
            rhs = pair[1]

            self.checkTypeCompatibility(lhs, rhs, error(ast))

        return mtype.restype

    def loopBody(self, stmts, param):
        '''
        stmt: List[Statement]
        param: {
            'env': List[Symbol],
            'inloop': Bool,
            'rettype': Type
        }
        '''
        env = param['env']
        rettype = param['rettype']

        outFlag = False
        for stmt in stmts:
            # if outFlag:
            #     raise UnreachableStatement(stmt)
            if self.visit(
                stmt, {
                    'env': env, 'inloop': True, 'rettype': rettype
                }
            ):
                outFlag = True

        return False

    def checkTypeCompatibility(self, lhs, rhs, error):
        # array check
        if isinstance(lhs, ArrayType):
            if not isinstance(rhs, ArrayType):
                raise error
            if lhs.lower != rhs.lower or \
                    lhs.upper != rhs.upper:
                raise error
            # self.checkTypeCompatibility(lhs.eleType, rhs.eleType, error)
            if not isinstance(lhs.eleType, type(rhs.eleType)):
                raise error

        # float/int coersion
        elif isinstance(lhs, FloatType):
            if not isinstance(rhs, (IntType, FloatType)):
                raise error

        # else
        elif not isinstance(lhs, type(rhs)):
            raise error   

    def visitProgram(self,ast, env):
        # printDebug("======SCAN PROGRAM======")
        s1 = Symbol("read",MType([],StringType()))
        s2 = Symbol("printLn",MType([],VoidType()))
        s3 = Symbol("printStr",MType([StringType()],VoidType()))
        s4 = Symbol("printStrLn",MType([StringType()],VoidType()))  
        env = [s1,s2,s3,s4]

        global_scope = reduce(
            lambda returnList, decl:
                [self.visit(
                    decl,
                    {'env': returnList, 'scan': False}
                )] + returnList,
            ast.decl,
            env
        )

 
        # printDebug("======GLOBAL======", env=global_scope)

        if not any(map(
            lambda symbol: symbol.name == 'main' ,
                global_scope)):
            raise NoEntryPoint()
            
        funcs = filter(lambda x: isinstance(x, FuncDecl), ast.decl)

        for func in funcs:
            self.visit(func, {'env': global_scope, 'scan': True})

        for symbol in global_scope:
            if not isinstance(symbol.mtype, MType):
                continue
            if symbol.name == 'main' and \
                    isinstance(symbol.mtype.restype, VoidType):
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
            # printDebug("FUNCDECL", env=env, stop=False)
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
            # printDebug("========SCAN FUNC========")
            printDebug(str(ast))

            try:
                # visits VarDecl -- throws Redeclared(Variable)
                parameter = reduce(
                    lambda scope, vardecl:
                        [self.visit(vardecl, {'env': scope})] + scope,
                    ast.param,
                    env
                )
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)
            # printDebug("PARAM", env=parameter)

            # visits VarDecl -- throws Redeclared(Variable)
            local_scope = reduce(
                lambda scope, vardecl:
                    [self.visit(vardecl, {'env': scope})] + scope,
                ast.body[0]+ast.body[1],
                parameter  # for safety reason, copy
            )
            local_scope += env


    
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
        # printDebug("VARDECL", env=env, stop=False)

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
            ('&&', '||'): (Bool, Bool) => Bool
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
        
        if op in ('&&', '||'):
            return deferType((BoolType), BoolType())

    def visitUnaryOp(self, ast, param):
        '''
        ast: UnaryOp{
            op:str
            body:Expr
        }
        param: List[Symbol]
        raise TypeMismatchInExpression
            ! Bool => Bool
            - Int => Int
            -. Float => Float
        => Type
        '''
        op = ast.op
        expr = self.visit(ast.body, param)

        if op in ('!'):
            if not isinstance(expr, BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ('-'):
            if not isinstance(expr, IntType):
                raise TypeMismatchInExpression(ast)
            return expr
        
        if op in ('-.'):
            if not isinstance(expr, FloatType):
                raise TypeMismatchInExpression(ast)
            return expr
        

    def visitCallExpr(self, ast, env):
        '''
        ast: CallExpr ~ CallStmt
        env: list[Symbol]
        raise Undeclared(Function)
        raise TypeMismatchInExpression
            wrong param size
            wrong param type
        => Type
        '''
        if isinstance(env, dict):
            return self.callBody(ast, env['env'])
        
        return self.callBody(ast, env)

    def visitId(self, ast, o):
        '''
        ast: ID: name
        o: List[Symbol] or {
            'env': List[Symbol]
            'kind': kind
        }
        raise Undeclared
        => Type: Symbol.mtype
        '''

        env = o['env'] if not isinstance(o, list) else o
        kind = o['kind'] if not isinstance(o, list) else Identifier()


        resLst = list(filter(lambda e: ast.name == e.name, env))
        
      
        if len(resLst) == 0:
            raise Undeclared(kind, ast.name)

        return resLst[0].mtype


    def visitArrayCell(self, ast, param):
        '''
        ast: ArrayCell{
            arr:Expr
            idx:List[Expr]
        }
        param: List[Symbol]
        raise TypeMismatchInExpression
            arr[idx] --> ArrayType[IntType] => ArrayType.eleType
        => Type
        '''
        arr = self.visit(ast.arr, param)
        idx = self.visit(ast.idx, param)

        if not isinstance(idx, IntType) or \
                not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)

        return arr.eleType

    def visitAssign(self, ast, param):
        '''
        ast: Assign{        
            lhs: LHS
            rhs: Expr
        }
        param: {
            'env': List[Symbol]
            'inloop': Bool
        }
        raise TypeMismatchInStatement
            Float := Float/Int
            Int := Int
            Bool := Bool
            // no String, Array
        => Returned?
        '''
        env = param['env']
        left_type = self.visit(ast.lhs, env)
        right_type = self.visit(ast.exp, env)

        if (isinstance(left_type, VoidType) and \
            isinstance(right_type, VoidType)):
            raise TypeMismatchInStatement(ast)

        self.checkTypeCompatibility(
            left_type, right_type, TypeMismatchInStatement(ast))

        return False    

    def visitIf(self, ast, param):
        '''
        ast: If{
            ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
            elseStmt:Tuple[List[VarDecl],List[Stmt]]
        }
        param: {
            'env': List[Symbol]
            'inloop': Bool
            'rettype': Type
        }
        => Returned?
        '''

        # expr = self.visit(ast.expr, param['env'])
        # if not isinstance(expr, BoolType):
        #     raise TypeMismatchInStatement(ast)
        pass


    def visitFor(self, ast, param):
        '''
        ast: For{
                idx1: Id
                expr1:Expr
                expr2:Expr
                expr3:Expr
                loop: Tuple[List[VarDecl],List[Stmt]]
        }
        param: {
            'env': List[Symbol],
            'rettype': Type
        }
        '''
        pass

    def visitContinue(self, ast, param):
        '''
        ast: Continue
        param: {
            'inloop': Bool
        }
        '''
        if not param['inloop']:
            raise ContinueNotInLoop()
        return True

    def visitBreak(self, ast, param):
        '''
        ast: Break
        param: {
            'inloop': Bool
        }
        '''
        if not param['inloop']:
            raise BreakNotInLoop()
        return True

    def visitReturn(self, ast, param):
        '''
        ast: Return{
            expr:Expr # None if no expression
        }
        param: {
            'env': List[Symbol]
            'rettype': Type
        }
        '''
        rettype = param['rettype']
        env = param['env']
        if isinstance(rettype, VoidType):
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast)
            self.checkTypeCompatibility(
                rettype, self.visit(ast.expr, env),
                TypeMismatchInStatement(ast)
            )

        return True

    def visitWhile(self, ast, param):
        '''
        ast: While{
            exp: Expr
            sl:Tuple[List[VarDecl],List[Stmt]]
        }
        param: {
            'env': List[Symbol],
            'inloop': Bool,
            'rettype': Type
        }
        '''
        env = param['env']

        exp = self.visit(ast.exp, env)
        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

        # return self.loopBody(ast.sl, param)
        return False

    def visitCallStmt(self, ast, param):
        '''
        ast: CallStmt
        param: {
            'env': list[Symbol]
        }
        raise Undeclared(Procedure)
        raise TypeMismatchInStatement
            wrong param size
            wrong param type
        => Returned?
        '''
        return self.callBody(ast, param['env'])  # skips return
         

    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()







        
