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


    # Visit a parse tree produced by BKITParser#init_value.
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
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


    # Visit a parse tree produced by BKITParser#param.
    def visitParam(self, ctx:BKITParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#scal_parm.
    def visitScal_parm(self, ctx:BKITParser.Scal_parmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#comp_parm.
    def visitComp_parm(self, ctx:BKITParser.Comp_parmContext):
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


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arith_expr.
    def visitArith_expr(self, ctx:BKITParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arith_expr1.
    def visitArith_expr1(self, ctx:BKITParser.Arith_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arith_expr2.
    def visitArith_expr2(self, ctx:BKITParser.Arith_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arith_expr3.
    def visitArith_expr3(self, ctx:BKITParser.Arith_expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_expr.
    def visitBool_expr(self, ctx:BKITParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_expr1.
    def visitBool_expr1(self, ctx:BKITParser.Bool_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_expr2.
    def visitBool_expr2(self, ctx:BKITParser.Bool_expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela_expr.
    def visitRela_expr(self, ctx:BKITParser.Rela_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#rela_expr1.
    def visitRela_expr1(self, ctx:BKITParser.Rela_expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#elem_express.
    def visitElem_express(self, ctx:BKITParser.Elem_expressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_expr.
    def visitIndex_expr(self, ctx:BKITParser.Index_exprContext):
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


    # Visit a parse tree produced by BKITParser#sub_arr.
    def visitSub_arr(self, ctx:BKITParser.Sub_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arr_elem.
    def visitArr_elem(self, ctx:BKITParser.Arr_elemContext):
        return self.visitChildren(ctx)



del BKITParser