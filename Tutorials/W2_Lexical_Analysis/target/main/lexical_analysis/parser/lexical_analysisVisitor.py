# Generated from main/lexical_analysis/parser/lexical_analysis.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .lexical_analysisParser import lexical_analysisParser
else:
    from lexical_analysisParser import lexical_analysisParser

# This class defines a complete generic visitor for a parse tree produced by lexical_analysisParser.

class lexical_analysisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lexical_analysisParser#program.
    def visitProgram(self, ctx:lexical_analysisParser.ProgramContext):
        return self.visitChildren(ctx)



del lexical_analysisParser