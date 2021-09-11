'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym
        self.gen = False
        self.isFor = False

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("read", MType([], StringType()), CName(self.libName)),
                    Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                    Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
		    Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        '''
        ast: Program
        c: Any
        => c
        '''
        
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = MethodEnv(None, self.env)

        # use to infer type
        for x in ast.decl:
            self.env += [self.visit(x, e)]
        
        print("Infer Type Done")
        e.gen = True
        # begin gencode
        for x in ast.decl:
            self.visit(x, e)
        
            
        # self.genMain(e)
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    # def genMain(self,o):

    #     methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
    #     frame = Frame(methodname, methodtype.rettype)
    #     self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
    #     frame.enterScope(True)
        
    #     varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
    #     startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
    #     self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
    #     self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        
    #     # visit statement
    #     list(map(lambda x: self.visit(x, o), self.astTree.decl))
        
        
    #     self.emit.printout(self.emit.emitLABEL(endLabel, frame))
    #     self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
    #     self.emit.printout(self.emit.emitENDMETHOD(frame))
    

    def updateType(self, name, new_type, param, idx = -1):
        '''
        name: str
        new_type: Type
        param{
            frame
            sym: list[Symbol]
        }
        '''

        print("Update Type")
        for typ in param.sym:
            print("name: {} \t intype: {} \t outtype: {}".format(typ.name, typ.mtype.partype, typ.mtype.rettype))


        isUpdated = False
        syms = param.sym
        check = True

        if len(syms) == 0:
            return []

        for i in range(len(syms)):
            symbol = syms[i]
            if check:
                if isinstance(symbol.mtype, ArrayType):
                    if symbol.name == name:
                        if idx >= 0:
                            symbol.mtype.dimen[idx] = new_type
                        else:
                            symbol.mtype.eletype = new_type
                        
                        syms[i] = symbol
                elif isinstance(symbol.mtype, MType):
                    if symbol.name == name:
                        symbol.mtype.restype = new_type 
                    
                    if idx >= 0:
                        symbol.mtype.intype[idx] = new_type
                        
                    syms[i] = symbol
                elif symbol.name == name:
                    symbol.mtype = new_type
                    syms[i] = symbol
                    check = False
        param.sym = syms
        
        print("End Update Type")
        
        for typ in param.sym:
            print("intype: {} \t outtype: {}".format(typ.mtype.partype, typ.mtype.rettype))


    def genMethod(self, ast, o):
        print("genMethod")
        func = list(filter(lambda x: x.name == ast.name.name, self.env))[0]
        print("func: {}".format(func))

        if ast.name.name == 'main':
            func.mtype = MType([ArrayType([], StringType())], VoidType())
        frame = Frame(ast.name.name, func.mtype)
        print("func_type: {}".format(func.mtype.rettype))
        self.emit.printout(self.emit.emitMETHOD(ast.name.name, func.mtype, True, frame))
        frame.enterScope(True)
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        syms = o.sym

        if ast.name.name == 'main':
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([],StringType()), startLabel, endLabel, frame))
        else:
            for param, typ in zip(ast.param, func.mtype.intype):
                idx = frame.getNewIndex()
                self.emit.printout(self.emit.emitVAR(idx. param.variable.name, typ, startLabel, endLabel, frame))
                syms = [Symbol(param.variable.name, typ, Index(idx))] + syms
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))
        env = reduce(lambda acc, ele: MethodEnv(frame, [self.visit(ele, acc)] + acc.sym), ast.body[0], MethodEnv(frame, syms))

        has_return_global = False
        for stmt in ast.body[1]:
            self.visit(stmt, env)

            if not has_return_global:   
                has_return_global = type(stmt) is Return
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        if not has_return_global:
            self.emit.printout(self.emit.emitRETURN(func.mtype.rettype, frame))
        self.emit.printout(self.emit.emitMETHOD(frame))
        frame.exitScope()

    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def visitFuncDecl(self, ast, o):
        '''
        ast: FuncDecl{
            name: Id
            param: List[VarDecl]
            body: Tuple[List[VarDecl],List[Stmt]]
            }
        o: env
        => None if generate code
        => else Symbol
        '''

        if o.gen:
            # on gen

            self.genMethod(ast, o)
        else:
            # infer type
            params = [self.visit(var.variable, o) for var in ast.param] if len(ast.param) > 0 else []
            for x in ast.body[0] + ast.body[1]:
                self.visit(x, o)
            
            return Symbol(ast.name.name, MType(params, None), CName(self.className))


        # funccode, functype = self.visit(ast.name, o)
        # params = [v.varType for in ast.param]

    def visitVarDecl(self, ast, o):
        '''
        ast: VarDecl{
            variable : Id
            varDimen : List[int] # empty list for scalar variable
            varInit  : Literal   # null if no initial
        }
        '''
        print("VarDecl")
        if o.gen:
            code, typ = self.visit(ast.variable, o)

            if o.frame is None:
                # gen for global
                code = self.emit.emitATTRIBUTE(ast.variable.name, typ, False, '')
            else:
                # gen for local
                frame = o.frame
                code = self.emit.emitVAR(o.sym.value.value, ast.variable.name, typ, frame.getStartLabel(), frame.getEndLabel(), frame)
            
            self.emit.printout(code)
        
        else:
            if o.frame is None:
                return Symbol(ast.variable.name, None, CName(self.className))
            
            idx = frame.getNewIndex()
            return Symbol(ast.variable.name, None, Index(idx))
    
    def visitBinaryOp(self, ast, o):
        '''
        ast: BinaryOp
        o:  Access
        => code, type

        Rules:
        (+,-,*,\,%): Int-Int => Int
        (+. ,-. ,*. ,\. ): Float-Float => float
        (<, <=, >, >=, ==, !=): Int - Int => Bool
        (=/=, <. , >. , <=. , >=.): Float - Float => Bool
        (&&, ||) : Bool - Bool => Bool

        '''
        frame = o.frame
        sym = o.sym

        lhs, ltype = self.visit(ast.left, o)
        rhs, rtype = self.visit(ast.right, o)

        if o.gen:

            if isinstance(ltype, Mtype):
                ltype = ltype.rettype
            if isinstance(rtype, MType):
                rtype = rtype.rettype

            if not isinstance(ltype, type(rtype)):
                if isinstance(ltype, IntType):
                    lhs += self.emit.emitI2F(frame)
                
                if isinstance(rtype, IntType):
                    rhs += self.emit.emitI2F(frame)
                
                intype = FloatType()
                rettype = FloatType()
            else:
                intype = ltype
                rettype = ltype
            
            code = ''
            code += lhs
            code += rhs

            if ast.op in ['+', '+.', '-', '-.']:
                code += self.emit.emitADDOP(ast.op[0], intype, frame)
            elif ast.op in ['*', '*.', '//' , '//.']:
                code += self.emit.emitMULOP(ast.op[0],intype, frame)
            elif ast.op in ['&&']:
                code += self.emit.emitANDOP(frame)
            elif ast.op in ['||']:
                code += self.emit.emitOROP(frame)
            else:
                code += self.emit.emitREOP(ast.op, intype, frame)
                rettype = BoolType()
            
            return code, rettype

        else:
            print("Infer Type")

        

    def visitUnaryOp(self, ast, o):
        frame = o.frame
        sym = o.sym

        bodycode, bodytype = self.visit(ast.body, o)

        code = ''
        code += bodycode

        if ast.op in ['!']:
            code += self.emit.emitNOT(bodytype, frame)
        elif ast.op in ['-', '-.']:
            code += self.emit.emitNEGOP(bodytype, frame)
        
        return code, bodytype

    def visitCallExpr(self, ast, env):
        '''
        ast: CallExpr
        o: Access
        => (name, type) of function being called
        '''
        return self.callBody(ast, o)

    def visitId(self, ast, o):
        '''
        ast: Id
        o
        '''

        print("visit ID")

        res = self.lookup(ast.name, o.sym, lambda env: env.name)


        # not likely, checker catches
        if res is None:
            print("End visit ID")
            return None, None
        
        # function call
        if isinstance(res.mtype, MType):
            print("End visit ID")
            return res, res.mtype

        frame = o.frame
        # global variable
        # res: Symbol(,,CName)
        if isinstance(res.value, CName):
            varname = res.value.value + '/' + res.name
            if o.isLeft:
                code = self.emit.emitPUTSTATIC(varname, res.mtype, frame)
            else:
                code = self.emit.emitGETSTATIC(varname, res.mtype, frame)
            
            print("End visit ID")
            return code, res.mtype
        
        # Local variable
        if o.isLeft:
            code = self.emit.emitWRITEVAR(res.name, res.mtype, res.value.value, frame)
        else:
            code = self.emit.emitREADVAR(res.name, res.mtype, res.value.value, frame)
        
        print("End visit ID")
        return code, res.mtype



    def visitArrayCell(self, ast, o):
        '''
        ast: ArrayCell{
            arr:Expr
            idx:List[Expr]
        },
        o: Access
        '''
        print("visit Array Cell")
        if o.gen:
            frame = o.frame
            sym = o.sym
            arrcode, arrtype = self.visit(o.idx, o)
        else:
            self.visit(ast.arr, o)
            print("array: {}".format(ast.arr))

            for i in range(len(ast.idx)):
                typ = self.visit(ast.idx[i], o)
                if typ == None:
                    self.updateType(ast.arr, IntType(), o, i)


    def visitAssign(self, ast, o):
        '''
        ast: Assign
        o:
        '''
        frame = o.frame
        sym = o.sym
        expcode, exptype = self.visit(ast.exp, o)
        lhscode, lhstype = self.visit(ast.lhs, o)

        if isinstance(exptype, Symbol):
            exptype = exptype.mtype.rettype

        if not isinstance(exptype, type(lhstype)):
            # float = int
            # others => checker catches
            expcode += self.emit.emitI2F(frame)
        
        code = ''
        code += expcode + lhscode
        self.emit.printout(code)


    def visitIf(self, ast, o):
        '''
        ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
        elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
        '''

        print("visit IF")
        if o.gen:
            frame = o.frame
            sym = o.sym

            haveElseIf = True if len(ast.ifthenStmt) > 1 else False
            haveElse = True if len(ast.elseStmt) > 0 else False

            if haveElse:
                endLabel = frame.getNewLabel()
            elseLabel = frame.getNewLabel()

            code = ''
            if haveElseIf:
                for case in ast.ifthenStmt[:-1]:
                    expr = case[0]
                    varDecls = case[1]
                    stmts = case[2]

                    expcode, exptype = self.visit(expr, o)
                    code = expcode
                    elseIfLabel = frame.getNewLabel()

                    code += self.emit.emitIFFALSE(elseIfLabel, frame)
                    self.emit.printout(code)
                    code = ''
                    # print out then code
                    for stmt in varDecls + stmts:
                        self.visit(stmt, o)
                    
                    if haveElse:
                        code += self.emit.emitGOTO(endLabel, frame)
                    else:
                        code += self.emit.emitGOTO(elseLabel, frame)
                    
                    code += self.emit.emitLabel(elseIfLabel, frame)
                    self.emit.printout(code)
                    code = ''
            
            expr = ast.ifthenStmt[-1][0]
            varDecls = ast.ifthenStmt[-1][1]
            stmts = ast.ifthenStmt[-1][2]

            expcode, exptype = self.visit(expr, o)
            code = expcode
            code += self.emitIFFALSE(elseLabel, frame)
            self.emit.printout(code)
            code = ''

            # print out then code
            for stmt in varDecls + stmts:
                self.visit(stmt, o)
            
            if haveElse:
                code += self.emit.emitGOTO(endLabel, frame)
            code += self.emit.emitLabel(elseLabel, frame)
            self.emit.printout(code)
            code = ''

            if not haveElse:
                return
            
            # printout else code
            for stmt in ast.elseStmt[0] + ast.elseStmt[1]:
                self.visit(stmt, o)
            
            code = self.emit.emitLabel(endLabel, frame)
            self.emit.printout(code)
        else:
            for case in ast.ifthenStmt:
                expr = self.visit(case[0], o)

                if expr == None:
                    print("case0: {}".format(case[0]))
                    self.updateType(case[0], BoolType(), o)
                
                for stmt in case[1] + case[2]:
                    self.visit(stmt, o)
            
            if len(ast.elseStmt) > 0:
                for stmt in ast.elseStmt[0] + ast.elseStmt[1]:
                    self.visit(stmt, o)

            print("env: {}".format(o))


    def visitFor(self, ast, o):
        pass


    def visitContinue(self, ast, o):
        continueLabel = o.frame.getContinueLabel()
        code = self.emit.emitGOTO(continueLabel, o.frame)
        self.emit.printout(code)

    def visitBreak(self, ast, o):
        breakLabel = o.frame.getBreakLabel()
        code = self.emit.emitGOTO(breakLabel, o.frame)
        self.emit.printout(code)

    def visitReturn(self, ast, o):
        pass

    def visitWhile(self, ast, o):
        pass

    def visitCallStmt(self, ast, o):
        pass
                 

    def visitIntLiteral(self, ast, o):
        if o.gen:
            return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()
        return IntType()
    
    def visitFloatLiteral(self, ast, o):
        if o.gen:
            return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()
        return FloatType()

    def visitBooleanLiteral(self, ast, o):
        if o.gen:
            return self.emit.emitPUSHICONST(ast.value, o.frame), BoolType()
        return BoolType()

    def visitStringLiteral(self, ast, o):
        if o.gen:
            return self.emit.emitPUSHCONST('"{}"'.format(ast.value),
                StringType(), o.frame), StringType()
        return StringType()
    def visitArrayLiteral(self, ast, o):
        print("visit Array Literal")
        pass






    
