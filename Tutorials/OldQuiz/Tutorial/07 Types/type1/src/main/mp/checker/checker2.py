
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
        print(ast.decl)
        print([i.name for i in _env])
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

        return None
    

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

