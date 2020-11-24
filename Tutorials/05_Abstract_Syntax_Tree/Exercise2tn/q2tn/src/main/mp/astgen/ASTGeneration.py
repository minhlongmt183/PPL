from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return None

    def visitMptype(self,ctx:MPParser.MptypeContext):
        return None

    def visitArraytype(self,ctx:MPParser.ArraytypeContext):
        return None

    def visitPrimtype(self,ctx:MPParser.PrimtypeContext): 
        return None

    def visitDimens(self,ctx:MPParser.DimensContext):
        return None
  
    def visitDimen(self,ctx:MPParser.DimenContext):
        return None

        

