from Visitor import BaseVisitor
from AST import *

class NameExercise(BaseVisitor):
    def visitProgram(self, ast, param):
        return [x for x in ast.decl if type(x) is VarDecl]