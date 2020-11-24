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


    # Visit a parse tree produced by MPParser#many_declarations.
    def visitMany_declarations(self, ctx:MPParser.Many_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variable_declaration.
    def visitVariable_declaration(self, ctx:MPParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_declarations.
    def visitList_declarations(self, ctx:MPParser.List_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#v_declaration.
    def visitV_declaration(self, ctx:MPParser.V_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_identifiers.
    def visitList_identifiers(self, ctx:MPParser.List_identifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#function_declaration.
    def visitFunction_declaration(self, ctx:MPParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_parameters.
    def visitList_parameters(self, ctx:MPParser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#not_null_list_parameters.
    def visitNot_null_list_parameters(self, ctx:MPParser.Not_null_list_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MPParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procedure_declaration.
    def visitProcedure_declaration(self, ctx:MPParser.Procedure_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#types.
    def visitTypes(self, ctx:MPParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primitive_type.
    def visitPrimitive_type(self, ctx:MPParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_type.
    def visitCompound_type(self, ctx:MPParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array_type.
    def visitArray_type(self, ctx:MPParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_1.
    def visitExpression_1(self, ctx:MPParser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression_2.
    def visitExpression_2(self, ctx:MPParser.Expression_2Context):
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


    # Visit a parse tree produced by MPParser#expression_6.
    def visitExpression_6(self, ctx:MPParser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arr_element.
    def visitArr_element(self, ctx:MPParser.Arr_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#func_call.
    def visitFunc_call(self, ctx:MPParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_expression.
    def visitList_expression(self, ctx:MPParser.List_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#not_null_list_expression.
    def visitNot_null_list_expression(self, ctx:MPParser.Not_null_list_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment_statement.
    def visitAssignment_statement(self, ctx:MPParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_var_idx_ass.
    def visitList_var_idx_ass(self, ctx:MPParser.List_var_idx_assContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_statement.
    def visitIf_statement(self, ctx:MPParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_statement.
    def visitWhile_statement(self, ctx:MPParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_statement.
    def visitFor_statement(self, ctx:MPParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#break_statement.
    def visitBreak_statement(self, ctx:MPParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_statement.
    def visitContinue_statement(self, ctx:MPParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_statement.
    def visitReturn_statement(self, ctx:MPParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_statement.
    def visitCompound_statement(self, ctx:MPParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_statements.
    def visitList_statements(self, ctx:MPParser.List_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#not_null_list_statements.
    def visitNot_null_list_statements(self, ctx:MPParser.Not_null_list_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_statement.
    def visitWith_statement(self, ctx:MPParser.With_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call_statement.
    def visitCall_statement(self, ctx:MPParser.Call_statementContext):
        return self.visitChildren(ctx)



del MPParser