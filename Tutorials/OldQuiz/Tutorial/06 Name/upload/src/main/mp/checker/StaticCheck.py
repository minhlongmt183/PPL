
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ','.join(str(i) for i in self.partype) + "]," + str(self.rettype) + ")"
        
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    
    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + "," + str(self.value) + ")"

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType()))]
            
    
    def __init__(self,ast):
        self.ast = ast
   
    def checkRedeclared(self, sym, kind, env):
        if self.lookup(sym.name, env, lambda x: x.name):
            raise Redeclared(kind, sym.name)
        else:
            return True
   
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        s = reduce(lambda x, y: [self.visit(y, c)] + x, ast.decl, [])
        # = [i.name for i in tmp]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if s[i].name == s[j].name:
                    if s[j].mtype is not MType:
                        raise(Redeclared(Variable(), s[j].name))
                    elif (s[j].mtype.rettype == VoidType()):
                        raise(Redeclared(Procedure(), s[j].name))
                    else:
                        raise(Redeclared(Function(), s[j].name))
        return reduce(lambda x, y: [self.visit(y, c)] + x, ast.decl, [])

    def visitFuncDecl(self,ast, c): 
        tmp = list(map(lambda x: self.visit(x, (c, True)), ast.body))
        kind = Procedure() if type(ast.returnType) is VoidType else Function()
        return Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType))
    
    def visitVarDecl(self, ast, c):
        return Symbol(ast.variable.name, ast.varType)
    
    def visitCallStmt(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)            
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()

