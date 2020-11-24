# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#glo_var_decl_part.
    def visitGlo_var_decl_part(self, ctx:BKITParser.Glo_var_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_list_decl.
    def visitVariable_list_decl(self, ctx:BKITParser.Variable_list_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_decl.
    def visitVariable_decl(self, ctx:BKITParser.Variable_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#init_value.
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bktype.
    def visitBktype(self, ctx:BKITParser.BktypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primitive_type.
    def visitPrimitive_type(self, ctx:BKITParser.Primitive_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#compound_type.
    def visitCompound_type(self, ctx:BKITParser.Compound_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl_part.
    def visitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_decl.
    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_name.
    def visitFunc_name(self, ctx:BKITParser.Func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_list.
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_param_decl.
    def visitFunc_param_decl(self, ctx:BKITParser.Func_param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl_statement.
    def visitVar_decl_statement(self, ctx:BKITParser.Var_decl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_statement.
    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement.
    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_if_part.
    def visitElse_if_part(self, ctx:BKITParser.Else_if_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#else_part.
    def visitElse_part(self, ctx:BKITParser.Else_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement.
    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement.
    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement.
    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_statement.
    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_func_call.
    def visitParam_func_call(self, ctx:BKITParser.Param_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable_list.
    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scal_var.
    def visitScal_var(self, ctx:BKITParser.Scal_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#comp_var.
    def visitComp_var(self, ctx:BKITParser.Comp_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#name_index_op.
    def visitName_index_op(self, ctx:BKITParser.Name_index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operator.
    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call_expr.
    def visitFunc_call_expr(self, ctx:BKITParser.Func_call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr_elem_list.
    def visitArr_elem_list(self, ctx:BKITParser.Arr_elem_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr_elem.
    def visitArr_elem(self, ctx:BKITParser.Arr_elemContext):
        return self.visitChildren(ctx)



del BKITParser