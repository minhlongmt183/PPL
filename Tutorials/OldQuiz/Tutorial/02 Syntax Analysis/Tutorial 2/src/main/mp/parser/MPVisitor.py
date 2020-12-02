# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variable_list.
    def visitVariable_list(self, ctx:MPParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parameters_list.
    def visitParameters_list(self, ctx:MPParser.Parameters_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration_variables.
    def visitDeclaration_variables(self, ctx:MPParser.Declaration_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration_parameters.
    def visitDeclaration_parameters(self, ctx:MPParser.Declaration_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration_function.
    def visitDeclaration_function(self, ctx:MPParser.Declaration_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#body.
    def visitBody(self, ctx:MPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound.
    def visitCompound(self, ctx:MPParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement_assignment.
    def visitStatement_assignment(self, ctx:MPParser.Statement_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_list.
    def visitExpression_list(self, ctx:MPParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_call.
    def visitExpression_call(self, ctx:MPParser.Expression_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement_call.
    def visitStatement_call(self, ctx:MPParser.Statement_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement_return.
    def visitStatement_return(self, ctx:MPParser.Statement_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_3.
    def visitExpression_3(self, ctx:MPParser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_4.
    def visitExpression_4(self, ctx:MPParser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_5.
    def visitExpression_5(self, ctx:MPParser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#types.
    def visitTypes(self, ctx:MPParser.TypesContext):
        return self.visitChildren(ctx)



del MPParser