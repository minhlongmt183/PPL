
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

        local_scope = env['local']
        global_scope = env['global']

        for ele in local_scope:
            if not isinstance(ele, Symbol):
                local_scope.remove(ele)
        env['local'] = local_scope


        res = list(filter(lambda e: symbol.name == e.name, local_scope))
        if len(res) > 0:
            raise Redeclared(kind, symbol.name)


    def updateType(self, name, new_type, param, idx = -1):
        '''
        name: str
        new_type: Type
        param{
            'local': list[symbol]
            'global': list[Symbol]
        }
        '''

        isUpdated = False
        local_scope = param['local']
        global_scope = param['global']
        check = True

        if len(local_scope) == 0 and len(global_scope) == 0:
            return []

        if len(local_scope) > 0:
            new_local_scope = []

            for symbol in local_scope:
                if check:
                    if not isinstance(symbol, Symbol):
                        continue

                    if isinstance(symbol.mtype, ArrayType):
                        if symbol.name == name:
                            if idx >= 0:
                                symbol.mtype.dimen[idx] = new_type
                            else:
                                symbol.mtype.eletype = new_type
                            
                            if not isUpdated:
                                isUpdated = True
                    elif isinstance(symbol.mtype, MType):
                        if symbol.name == name:
                            symbol.mtype.restype = new_type 
                            if not isUpdated:
                                isUpdated = True

                        
                        if idx >= 0:
                            symbol.mtype.intype[idx] = new_type
                            if not isUpdated:
                                isUpdated = True
                    
                    elif symbol.name == name:
                        symbol.mtype = new_type
                        check = False

                new_local_scope.append(symbol)
            
            if isUpdated:
                param['local'] = new_local_scope
                param['global'] = global_scope
                return new_local_scope

        new_global_scope = self.updateType(name, new_type,\
            {'local': global_scope, 'global': []})
        
        if isUpdated:    
            param['local'] = local_scope
            param['global'] = new_global_scope      
        return new_global_scope

    def updateParameter(self, name, new_type, param):
        '''
        name: str
        new_type: Type
        param{
            'local': list[symbol]
            'global': list[Symbol]
        }
        '''
        global_scope = param['global']
        isUpdated = False


        if len(global_scope) > 0:
            new_global_scope = []

            for symbol in global_scope:
                if not isinstance(symbol, Symbol):
                    new_global_scope.append(symbol)
                    continue

                if isinstance(symbol.mtype, MType):
                    if len(symbol.mtype.intype) == 0:
                        new_global_scope.append(symbol)
                        continue
                    for i in range(len(symbol.mtype.intype)):
                        if not isinstance(symbol.mtype.intype[i], Symbol):
                            continue
                        if symbol.mtype.intype[i].name == name:
                            symbol.mtype.intype[i].mtype = new_type
                            isUpdated = True
                            break
                
                new_global_scope.append(symbol)
            
            if isUpdated:
                param['global'] = new_global_scope
                return new_global_scope
        return []

    def updateAPI(self, symbol, new_type, param, idx = -1):
        if isinstance(symbol, ArrayCell):
            ret = self.updateType(symbol.arr.name, new_type, param, idx)

            if len(ret) == 0:
                self.updateParameter(symbol.arr.name, new_type, param)
        elif isinstance(symbol, CallExpr):
            ret = self.updateType(symbol.method.name, new_type, param, idx)

            if len(ret) == 0:
                self.updateParameter(symbol.method.name, new_type, param)

        else:
            ret = self.updateType(symbol.name, new_type, param, idx)

            if len(ret) == 0:
                self.updateParameter(symbol.name, new_type, param)

    


    def callBody(self, ast, env):
        local_scope = env['local']
        global_scope = env['global']

        callParam = [self.visit(x, env) for x in ast.param]

        for ele in local_scope:
            if not isinstance(ele, Symbol):
                local_scope.remove(ele)
        
        env['local'] = local_scope
        

        mtype = self.visit(  # visits Id
            ast.method,
            {
                'local': local_scope,
                'global': global_scope,
                'kind': Function() if isinstance(ast, CallExpr) \
                else VoidType(), 
            }
        )

        error = TypeMismatchInExpression if isinstance(ast, CallExpr) \
            else TypeMismatchInStatement
        
        if isinstance(ast, CallStmt) and not isinstance(mtype, VoidType):
            raise error(ast)

        if not isinstance(mtype.intype, Symbol):
            if len(callParam) != len(mtype.intype):
                raise error(ast)
            idx = -1

            for pair in zip(mtype.intype[::-1], callParam):
                idx += 1
                lhs = pair[0]
                rhs = pair[1]

                if isinstance(lhs, Unknown) and isinstance(rhs, Unknown):
                    return False

                if isinstance(lhs, Unknown):
                    self.updateAPI(ast.method, rhs, env, len(mtype.intypw)-1-idx)
                    lhs = rhs
                    continue
                
                if isinstance(rhs, Unknown):
                    self.updateType(ast.method.name, lhs, env, idx)
                    rhs = lhs
                    continue
                if rhs == False or lhs == False:
                    return False

                self.checkTypeCompatibility(lhs, rhs, error(ast))
            return mtype.restype

        rightParam = mtype.intype
        
        if len(rightParam) != len(callParam):
            raise error(ast)

        idx = -1

        for pair in zip(rightParam[::-1], callParam):
            idx += 1
            lhs = pair[0]
            rhs = pair[1]

            if isinstance(lhs.mtype, Unknown) and isinstance(rhs, Unknown):
                return False

            if isinstance(lhs.mtype, Unknown):
                self.updateType(lhs.name, rhs, env, len(rightParam)-1-idx)
                lhs.mtype = rhs
                continue
            
            if isinstance(rhs, Unknown):
                self.updateType(ast.method.name, lhs.mtype, env, idx)
                rhs = lhs.mtype
                continue

            if rhs == False or lhs == False:
                return False

            self.checkTypeCompatibility(lhs.mtype, rhs, error(ast))

        return mtype.restype

    def loopBody(self, stmts, param):
        local_scope = param['local']
        global_scope = param['global']
        restype = param['restype']


        for stmt in stmts[0]+stmts[1]:
            if self.visit(
                stmt, {
                    'local': local_scope, 
                    'global': global_scope,
                    'inloop': True,
                    'restype': restype
                }
            ):
                outFlag = True

        return True

    def checkTypeCompatibility(self, lhs, rhs, error):
        # array check

        if isinstance(lhs, ArrayType):
            if not isinstance(rhs, ArrayType):
                raise error
            if lhs != rhs:
                raise error
            # self.checkTypeCompatibility(lhs.eleType, rhs.eleType, error)
            if not isinstance(lhs.eletype, type(rhs.eletype)):
                raise error

        # float/int coersion
        elif isinstance(lhs, FloatType):
            if not isinstance(rhs, (IntType, FloatType)):
                raise error

        # else
        elif not isinstance(lhs, type(rhs)):
            raise error   

    def processStatement(self, stmts, param):
        if len(stmts) == 0:
            return False

        returnFlag = False
        for stmt in stmts:
            if self.visit(stmt, param):
                returnFlag = True
        
        return returnFlag

    def visitProgram(self,ast, env):

        global_scope = reduce(
            lambda returnList, decl:
                [self.visit(
                    decl,
                    {'local': returnList,
                    'global': [],
                    'scan': False}
                )] + returnList,
            ast.decl,
            env + self.global_envi
        )

        if not any(map(
            lambda symbol: symbol.name == 'main' ,
                global_scope)):
            raise NoEntryPoint()
            
        funcs = filter(lambda x: isinstance(x, FuncDecl), ast.decl)

        for func in funcs:
            self.visit(func, {'local': [], 'global': global_scope, 'scan': True})

        return global_scope

    
    def visitFuncDecl(self, ast, param):
        local_scope = param['local']
        global_scope = param['global']
        scan = param['scan']

        if not scan:
            s = Symbol(
                ast.name.name,
                MType(
                    reduce(
                    lambda scope, vardecl:
                        [self.visit(vardecl,\
                             {'local': scope, 'global': global_scope})] + scope,
                    ast.param,
                    []
                    ),
                    Unknown()
                ))

            kind = Function()
            for ele in local_scope:
                if not isinstance(ele, Symbol):
                    local_scope.remove(ele)
            param['local'] = local_scope
            self.checkRedeclared(s, kind, param)
            
            return s
        else:

            try:
                parameter = reduce(
                    lambda scope, vardecl:
                        [self.visit(vardecl,\
                             {'local': scope, 'global': global_scope})] + scope,
                    ast.param,
                    []
                )
            except Redeclared as e:
                raise Redeclared(Parameter(), e.n)

            local_scope = reduce(
                lambda scope, vardecl:
                    [self.visit(vardecl,\
                             {'local': scope, 'global': global_scope})] + scope,
                ast.body[0],
                []
            )
            global_scope = local_scope + global_scope

            new_env = {
                        'local': [],
                        'global': global_scope,
                        'inloop': False,
                        'restype': Unknown()
                    }
            if not self.processStatement(
                    ast.body[1], new_env):
                self.updateAPI(ast.name, VoidType(), param)
            else:
                self.updateAPI(ast.name, new_env['restype'], param)

    def visitVarDecl(self, ast, param):

        local_scope = param['local']
        global_scope = param['global']
        if ast.varInit == None:
            varType = Unknown()
        else:
            varType = self.visit(ast.varInit, param)


        s = Symbol(
            ast.variable.name,
            varType if len(ast.varDimen) == 0 else ArrayType(ast.varDimen, varType)
        )

        for ele in local_scope:
            if not isinstance(ele, Symbol):
                local_scope.remove(ele)
        self.checkRedeclared(s, Variable(), {'local': local_scope, 'global': global_scope})

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
        

        op = ast.op
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)

        if left_type == False or right_type == False:
            return False

        def deferType(left_type, right_type,  acceptableTypes, returnType=None):
            
            if isinstance(left_type, Unknown):
                left_type = acceptableTypes
                self.updateAPI(ast.left, acceptableTypes, param)
            
            if isinstance(right_type, Unknown):
                right_type = acceptableTypes
                self.updateAPI(ast.right, acceptableTypes, param)

      
            if not isinstance(left_type, type(acceptableTypes)):
                raise TypeMismatchInExpression(ast)
            if not isinstance(right_type, type(acceptableTypes)):
                raise TypeMismatchInExpression(ast)

            if returnType is not None:
                return returnType
            if isinstance(left_type, FloatType) or \
                    isinstance(right_type, FloatType):
                return FloatType()
            if isinstance(left_type, right_type):
                return left_type

            raise TypeMismatchInExpression(ast)
    
        if op in ('+','-','*', '\\',' %'):                    
            return deferType(left_type, right_type, IntType(), IntType())

        if op in ('+.','-.','*.', '\\.'):                    
            return deferType(left_type, right_type, FloatType(), FloatType())

        if op in ('==', '!=', '<','>', '<=','>='):             
            return deferType(left_type, right_type, IntType(), BoolType())

        if op in ('=/=', '<.', '>.', '<=.', '>=.'):    
            return deferType(left_type, right_type, FloatType(), BoolType())
        
        if op in ('&&', '||'):            
            return deferType(left_type, right_type, BoolType(), BoolType())

    def visitUnaryOp(self, ast, param):
        
        op = ast.op
        expr = self.visit(ast.body, param)

        if op in ('!'):
            if isinstance(expr, Unknown):
                self.updateAPI(ast.body, BoolType(), param)
                expr = BoolType()

            if not isinstance(expr, BoolType):
                raise TypeMismatchInExpression(ast)            
        
            return BoolType()
        
        if op in ('-'):
            if isinstance(expr, Unknown):
                self.updateAPI(ast.body, IntType(), param)
                expr = IntType()

            if not isinstance(expr, IntType):
                raise TypeMismatchInExpression(ast)            
        
            return expr
        
        if op in ('-.'):
            if isinstance(expr, Unknown):
                self.updateAPI(ast.body, FloatType(), param)
                expr = FloatType()

            if not isinstance(expr, FloatType):
                raise TypeMismatchInExpression(ast)        
        
            return expr
        

    def visitCallExpr(self, ast, env):
        return self.callBody(ast, env)

    def visitId(self, ast, param):

        local_scope = param['local']
        global_scope = param['global']
        kind = Function() if ('kind' in param) else Identifier()



        resLst = None

        for e in (local_scope + global_scope + self.global_envi):
            if ast.name == e.name:
                resLst = e
                break 
        
        if resLst == None:
            for e in global_scope:
                if isinstance(e.mtype, MType):
                    if len(e.mtype.intype) == 0:
                        continue
                    for s in e.mtype.intype:
                        if not isinstance(s, Symbol):
                            continue
                        if s.name == ast.name:
                            kind = Parameter()
                            return s.mtype

            raise Undeclared(kind, ast.name)
        return resLst.mtype


    def visitArrayCell(self, ast, param):
        local_scope = param['local']
        global_scope = param['global']

        arr = self.visit(ast.arr, param)

        if arr == False:
            return False

        if len(ast.idx) > 0:
            for i in range(len(ast.idx)):
                typeExpr = self.visit(ast.idx[i], param)

                if isinstance(typeExpr, Unknown):
                    self.updateAPI(ast.arr, IntType(), param, i)
                    typeExpr = IntType()

                if not isinstance(typeExpr, IntType):
                    raise TypeMismatchInExpression(ast)
        
        if isinstance(arr, Unknown):
            return False

        if not isinstance(arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        
        return arr.eletype

    def visitAssign(self, ast, param):
        local_scope = param['local']
        global_scope = param['global']
        for elem in local_scope:
            if not isinstance(elem, Symbol):
                local_scope.remove(elem)
        for elem in global_scope:
            if not isinstance(elem, Symbol):
                global_scope.remove(elem)

        param['local'] = local_scope
        param['global'] = global_scope

        left_type = self.visit(ast.lhs, param)
        right_type = self.visit(ast.rhs, param)

        if left_type == False or right_type == False:
            raise TypeCannotBeInferred(ast)

        if (isinstance(left_type, Unknown) and \
            isinstance(right_type, Unknown)):
            raise TypeCannotBeInferred(ast)
        
        if isinstance(left_type, Unknown):
            self.updateAPI(ast.lhs, right_type, param, -1)
            left_type = right_type
        

        if isinstance(right_type, Unknown):
            self.updateAPI(ast.rhs, left_type, param, -1)
            right_type = left_type

        if type(left_type)!= type(right_type):
            raise TypeMismatchInStatement(ast)

        return True

    def visitIf(self, ast, param):
        expr = self.visit(ast.ifthenStmt[0][0], param)

        if expr == False:
            raise TypeCannotBeInferred(ast)

        if isinstance(expr, Unknown):
            self.updateAPI(ast.ifthenStmt[0][0], BoolType(), param, -1)
            expr = BoolType()
            

        if not isinstance(expr, BoolType):
            raise TypeMismatchInStatement(ast)
        local_scope = []

        if len(ast.ifthenStmt[0][1]) > 0:
            local_scope = reduce(
                lambda scope, vardecl:
                    [self.visit(vardecl,param)] + scope,
                ast.ifthenStmt[0][1],
                param)


        if len(ast.ifthenStmt[0][2]) > 0:
            new_env = {'local': param['local'] + local_scope,
                'global': param['global'],
                'inloop': param['inloop'],
                'restype': param['restype']}

            for stmt in ast.ifthenStmt[0][2]:
                self.visit(stmt, new_env)
        
        local_scope = []

        if len(ast.elseStmt[0]) > 0:
            local_scope = reduce(
                lambda scope, vardecl:
                    [self.visit(vardecl,param)] + scope,
                ast.elseStmt[0],
                param)

        if len(ast.elseStmt[1]) > 0:

            new_env = {'local': param['local'] + local_scope,
                'global': param['global'],
                'inloop': param['inloop'],
                'restype': param['restype']}
            for stmt in ast.elseStmt[1]:
                self.visit(stmt, new_env)
        
        if isinstance(param['restype'], Unknown):
            param['restype'] = new_env['restype']
        
        return True
        
        


    def visitFor(self, ast, param):

        idType = self.visit(ast.idx1, param)

        expr1 = self.visit(ast.expr1, param)
        expr2 = self.visit(ast.expr2, param)
        expr3 = self.visit(ast.expr3, param)


        if isinstance(idType, Unknown):
            self.updateAPI(ast.idx1, IntType(), param, -1)
            idType = IntType()

        if isinstance(expr1, Unknown):
            self.updateAPI(ast.expr1, IntType(), param, -1)
            expr1 = IntType()

        if isinstance(expr2, Unknown):
            self.updateAPI(ast.expr2, BoolType(), param, -1)
            expr2 = BoolType()

        if isinstance(expr3, Unknown):
            self.updateAPI(ast.expr3, IntType(), param, -1)
            expr3 = IntType()
        
        

        if not isinstance(idType, IntType) or \
                not isinstance(expr1, IntType) or \
                not isinstance(expr2, BoolType) or \
                not isinstance(expr3, IntType):
            raise TypeMismatchInStatement(ast)
            
        return self.loopBody(ast.loop, param)


    def visitContinue(self, ast, param):
        if not param['inloop']:
            return False
        return True

    def visitBreak(self, ast, param):
        if not param['inloop']:
            return False
        return True

    def visitReturn(self, ast, param):
        restype = param['restype'] if 'restype' in param else None

        if isinstance(restype, Unknown):
            param['restype'] = self.visit(ast.expr,param) \
                if ast.expr != None else VoidType()

            restype = param['restype']

        if isinstance(restype, VoidType):
            if ast.expr is not None:
                raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None:
                raise TypeMismatchInStatement(ast)
            self.checkTypeCompatibility(
                restype, self.visit(ast.expr, param),
                TypeMismatchInStatement(ast)
            )

        return True

    def visitWhile(self, ast, param):

        exp = self.visit(ast.exp, param)

        if isinstance(exp, Unknown):
            self.updateAPI(ast.exp, BoolType(), param, -1)
            exp = BoolType()

        if not isinstance(exp, BoolType):
            raise TypeMismatchInStatement(ast)

        return self.loopBody(ast.sl, param)

        return False

    def visitCallStmt(self, ast, param):
        self.callBody(ast, param)  # skips return
                 

    def visitIntLiteral(self, ast, param):
        return IntType()
    
    def visitFloatLiteral(self, ast, param):
        return FloatType()
    
    def visitBooleanLiteral(self, ast, param):
        return BoolType()
    
    def visitStringLiteral(self, ast, param):
        return StringType()
    def visitArrayLiteral(self, ast, param):
        rettype = self.visit(ast.value[0], param) \
            if len(ast.value) > 0 else Unknown()
        return ArrayType(ast.value, rettype)







        
