from Visitor import BaseVisitor
from AST import *
from functools import reduce

class NameExercise(BaseVisitor):
    def visitProgram(self, ast, param):
        return reduce(lambda x, y: x + y, [self.visit(x, ast) for x in ast.decl if type(x) is FuncDecl], [])
        
    def visitFuncDecl(self, ast, param):
        _local = [x for x in ast.local]
        _local.sort(key = lambda x: str(x.variable))

        for i in range(len(_local) - 1):
            if str(_local[i].variable) == str(_local[i + 1].variable):
                raise Exception("Duplicate: " + str(_local[i].variable))
        
        return _local