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

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym
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
        self.genMain(e)
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
    def genMain(self,o):
        methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
    
    
        
    def visitFuncDecl(self, ctx, o):
        pass

    def visitVarDecl(self, ctx, o):
        pass

    def visitIntType(self, ctx, o):
        pass
    
    def visitFloatType(self, ctx, o):
        pass
    
    def visitBoolType(self, ctx, o):
        pass
    def visitStringType(self, ctx, o):
        pass
    def visitVoidType(self, ctx, o):
        pass
    
    def visitArrayType(self, ctx, o):
        pass
    def visitBinaryOp(self, ctx, o):
        '''
        ctx: BinaryOp
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

        lhs, ltype = self.visit(ctx.left, Access(frame, sym))
        rhs, rtype = self.visit(ctx.right, Access(frame, sym))

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

        if ctx.op in ['+', '+.', '-', '-.']:
            code += self.emit.emitADDOP(ctx.op[0], intype, frame)
        elif ctx.op in ['*', '*.', '//' , '//.']:
            code += self.emit.emitMULOP(ctx.op[0],intype, frame)
        elif ctx.op in ['&&']:
            code += self.emit.emitANDOP(frame)
        elif ctx.op in ['||']:
            code += self.emit.emitOROP(frame)
        else:
            code += self.emit.emitREOP(ctx.op, intype, frame)
            rettype = BoolType()
        
        return code, rettype
        





    def visitUnaryOp(self, ctx, o):
        pass

    def visitCallExpr(self, ast, env):
        pass

    def visitId(self, ctx, o):
        pass


    def visitArrayCell(self, ctx, o):
        pass

    def visitAssign(self, ctx, o):
        pass

    def visitIf(self, ctx, o):
        pass
        
        


    def visitFor(self, ctx, o):
        pass


    def visitContinue(self, ctx, o):
        continueLabel = o.frame.getContinueLabel()
        code = self.emit.emitGOTO(continueLabel, o.frame)
        self.emit.printout(code)

    def visitBreak(self, ctx, o):
        breakLabel = o.frame.getBreakLabel()
        code = self.emit.emitGOTO(breakLabel, o.frame)
        self.emit.printout(code)

    def visitReturn(self, ctx, o):
        pass

    def visitWhile(self, ctx, o):
        pass

    def visitCallStmt(self, ctx, o):
        pass
                 

    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()
    
    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()
    
    def visitBooleanLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), BoolType()
    
    def visitStringLiteral(self, ctx, o):
        return self.emit.emitPUSHCONST('"{}"'.format(ctx.value),
            StringType(), o.frame), StringType()
            
    def visitArrayLiteral(self, ctx, o):
        pass






    
