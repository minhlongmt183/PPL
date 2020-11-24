# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Assignments/Assignment1/assignment1/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#glo_var_decl_part.
    def enterGlo_var_decl_part(self, ctx:BKITParser.Glo_var_decl_partContext):
        pass

    # Exit a parse tree produced by BKITParser#glo_var_decl_part.
    def exitGlo_var_decl_part(self, ctx:BKITParser.Glo_var_decl_partContext):
        pass


    # Enter a parse tree produced by BKITParser#var_decl.
    def enterVar_decl(self, ctx:BKITParser.Var_declContext):
        pass

    # Exit a parse tree produced by BKITParser#var_decl.
    def exitVar_decl(self, ctx:BKITParser.Var_declContext):
        pass


    # Enter a parse tree produced by BKITParser#variable_list.
    def enterVariable_list(self, ctx:BKITParser.Variable_listContext):
        pass

    # Exit a parse tree produced by BKITParser#variable_list.
    def exitVariable_list(self, ctx:BKITParser.Variable_listContext):
        pass


    # Enter a parse tree produced by BKITParser#variable.
    def enterVariable(self, ctx:BKITParser.VariableContext):
        pass

    # Exit a parse tree produced by BKITParser#variable.
    def exitVariable(self, ctx:BKITParser.VariableContext):
        pass


    # Enter a parse tree produced by BKITParser#scal_var.
    def enterScal_var(self, ctx:BKITParser.Scal_varContext):
        pass

    # Exit a parse tree produced by BKITParser#scal_var.
    def exitScal_var(self, ctx:BKITParser.Scal_varContext):
        pass


    # Enter a parse tree produced by BKITParser#comp_var.
    def enterComp_var(self, ctx:BKITParser.Comp_varContext):
        pass

    # Exit a parse tree produced by BKITParser#comp_var.
    def exitComp_var(self, ctx:BKITParser.Comp_varContext):
        pass


    # Enter a parse tree produced by BKITParser#init_value.
    def enterInit_value(self, ctx:BKITParser.Init_valueContext):
        pass

    # Exit a parse tree produced by BKITParser#init_value.
    def exitInit_value(self, ctx:BKITParser.Init_valueContext):
        pass


    # Enter a parse tree produced by BKITParser#literal.
    def enterLiteral(self, ctx:BKITParser.LiteralContext):
        pass

    # Exit a parse tree produced by BKITParser#literal.
    def exitLiteral(self, ctx:BKITParser.LiteralContext):
        pass


    # Enter a parse tree produced by BKITParser#func_decl_part.
    def enterFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        pass

    # Exit a parse tree produced by BKITParser#func_decl_part.
    def exitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        pass


    # Enter a parse tree produced by BKITParser#func_decl.
    def enterFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass

    # Exit a parse tree produced by BKITParser#func_decl.
    def exitFunc_decl(self, ctx:BKITParser.Func_declContext):
        pass


    # Enter a parse tree produced by BKITParser#func_name.
    def enterFunc_name(self, ctx:BKITParser.Func_nameContext):
        pass

    # Exit a parse tree produced by BKITParser#func_name.
    def exitFunc_name(self, ctx:BKITParser.Func_nameContext):
        pass


    # Enter a parse tree produced by BKITParser#param_list.
    def enterParam_list(self, ctx:BKITParser.Param_listContext):
        pass

    # Exit a parse tree produced by BKITParser#param_list.
    def exitParam_list(self, ctx:BKITParser.Param_listContext):
        pass


    # Enter a parse tree produced by BKITParser#param.
    def enterParam(self, ctx:BKITParser.ParamContext):
        pass

    # Exit a parse tree produced by BKITParser#param.
    def exitParam(self, ctx:BKITParser.ParamContext):
        pass


    # Enter a parse tree produced by BKITParser#scal_parm.
    def enterScal_parm(self, ctx:BKITParser.Scal_parmContext):
        pass

    # Exit a parse tree produced by BKITParser#scal_parm.
    def exitScal_parm(self, ctx:BKITParser.Scal_parmContext):
        pass


    # Enter a parse tree produced by BKITParser#comp_parm.
    def enterComp_parm(self, ctx:BKITParser.Comp_parmContext):
        pass

    # Exit a parse tree produced by BKITParser#comp_parm.
    def exitComp_parm(self, ctx:BKITParser.Comp_parmContext):
        pass


    # Enter a parse tree produced by BKITParser#statement_list.
    def enterStatement_list(self, ctx:BKITParser.Statement_listContext):
        pass

    # Exit a parse tree produced by BKITParser#statement_list.
    def exitStatement_list(self, ctx:BKITParser.Statement_listContext):
        pass


    # Enter a parse tree produced by BKITParser#var_decl_statement.
    def enterVar_decl_statement(self, ctx:BKITParser.Var_decl_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#var_decl_statement.
    def exitVar_decl_statement(self, ctx:BKITParser.Var_decl_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#assign_statement.
    def enterAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#assign_statement.
    def exitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#if_statement.
    def enterIf_statement(self, ctx:BKITParser.If_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#if_statement.
    def exitIf_statement(self, ctx:BKITParser.If_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#else_if_part.
    def enterElse_if_part(self, ctx:BKITParser.Else_if_partContext):
        pass

    # Exit a parse tree produced by BKITParser#else_if_part.
    def exitElse_if_part(self, ctx:BKITParser.Else_if_partContext):
        pass


    # Enter a parse tree produced by BKITParser#else_part.
    def enterElse_part(self, ctx:BKITParser.Else_partContext):
        pass

    # Exit a parse tree produced by BKITParser#else_part.
    def exitElse_part(self, ctx:BKITParser.Else_partContext):
        pass


    # Enter a parse tree produced by BKITParser#for_statement.
    def enterFor_statement(self, ctx:BKITParser.For_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#for_statement.
    def exitFor_statement(self, ctx:BKITParser.For_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#while_statement.
    def enterWhile_statement(self, ctx:BKITParser.While_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#while_statement.
    def exitWhile_statement(self, ctx:BKITParser.While_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#do_while_statement.
    def enterDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#do_while_statement.
    def exitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#break_statement.
    def enterBreak_statement(self, ctx:BKITParser.Break_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#break_statement.
    def exitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#continue_statement.
    def enterContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#continue_statement.
    def exitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#call_statement.
    def enterCall_statement(self, ctx:BKITParser.Call_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#call_statement.
    def exitCall_statement(self, ctx:BKITParser.Call_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#param_func_call.
    def enterParam_func_call(self, ctx:BKITParser.Param_func_callContext):
        pass

    # Exit a parse tree produced by BKITParser#param_func_call.
    def exitParam_func_call(self, ctx:BKITParser.Param_func_callContext):
        pass


    # Enter a parse tree produced by BKITParser#return_statement.
    def enterReturn_statement(self, ctx:BKITParser.Return_statementContext):
        pass

    # Exit a parse tree produced by BKITParser#return_statement.
    def exitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        pass


    # Enter a parse tree produced by BKITParser#expression.
    def enterExpression(self, ctx:BKITParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BKITParser#expression.
    def exitExpression(self, ctx:BKITParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BKITParser#arith_expr.
    def enterArith_expr(self, ctx:BKITParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#arith_expr.
    def exitArith_expr(self, ctx:BKITParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#arith_expr1.
    def enterArith_expr1(self, ctx:BKITParser.Arith_expr1Context):
        pass

    # Exit a parse tree produced by BKITParser#arith_expr1.
    def exitArith_expr1(self, ctx:BKITParser.Arith_expr1Context):
        pass


    # Enter a parse tree produced by BKITParser#arith_expr2.
    def enterArith_expr2(self, ctx:BKITParser.Arith_expr2Context):
        pass

    # Exit a parse tree produced by BKITParser#arith_expr2.
    def exitArith_expr2(self, ctx:BKITParser.Arith_expr2Context):
        pass


    # Enter a parse tree produced by BKITParser#arith_expr3.
    def enterArith_expr3(self, ctx:BKITParser.Arith_expr3Context):
        pass

    # Exit a parse tree produced by BKITParser#arith_expr3.
    def exitArith_expr3(self, ctx:BKITParser.Arith_expr3Context):
        pass


    # Enter a parse tree produced by BKITParser#operand.
    def enterOperand(self, ctx:BKITParser.OperandContext):
        pass

    # Exit a parse tree produced by BKITParser#operand.
    def exitOperand(self, ctx:BKITParser.OperandContext):
        pass


    # Enter a parse tree produced by BKITParser#bool_expr.
    def enterBool_expr(self, ctx:BKITParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#bool_expr.
    def exitBool_expr(self, ctx:BKITParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#bool_expr1.
    def enterBool_expr1(self, ctx:BKITParser.Bool_expr1Context):
        pass

    # Exit a parse tree produced by BKITParser#bool_expr1.
    def exitBool_expr1(self, ctx:BKITParser.Bool_expr1Context):
        pass


    # Enter a parse tree produced by BKITParser#bool_expr2.
    def enterBool_expr2(self, ctx:BKITParser.Bool_expr2Context):
        pass

    # Exit a parse tree produced by BKITParser#bool_expr2.
    def exitBool_expr2(self, ctx:BKITParser.Bool_expr2Context):
        pass


    # Enter a parse tree produced by BKITParser#rela_expr.
    def enterRela_expr(self, ctx:BKITParser.Rela_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#rela_expr.
    def exitRela_expr(self, ctx:BKITParser.Rela_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#rela_expr1.
    def enterRela_expr1(self, ctx:BKITParser.Rela_expr1Context):
        pass

    # Exit a parse tree produced by BKITParser#rela_expr1.
    def exitRela_expr1(self, ctx:BKITParser.Rela_expr1Context):
        pass


    # Enter a parse tree produced by BKITParser#elem_express.
    def enterElem_express(self, ctx:BKITParser.Elem_expressContext):
        pass

    # Exit a parse tree produced by BKITParser#elem_express.
    def exitElem_express(self, ctx:BKITParser.Elem_expressContext):
        pass


    # Enter a parse tree produced by BKITParser#index_expr.
    def enterIndex_expr(self, ctx:BKITParser.Index_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#index_expr.
    def exitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#func_call_expr.
    def enterFunc_call_expr(self, ctx:BKITParser.Func_call_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#func_call_expr.
    def exitFunc_call_expr(self, ctx:BKITParser.Func_call_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#array.
    def enterArray(self, ctx:BKITParser.ArrayContext):
        pass

    # Exit a parse tree produced by BKITParser#array.
    def exitArray(self, ctx:BKITParser.ArrayContext):
        pass


    # Enter a parse tree produced by BKITParser#arr_elem_list.
    def enterArr_elem_list(self, ctx:BKITParser.Arr_elem_listContext):
        pass

    # Exit a parse tree produced by BKITParser#arr_elem_list.
    def exitArr_elem_list(self, ctx:BKITParser.Arr_elem_listContext):
        pass


    # Enter a parse tree produced by BKITParser#sub_arr.
    def enterSub_arr(self, ctx:BKITParser.Sub_arrContext):
        pass

    # Exit a parse tree produced by BKITParser#sub_arr.
    def exitSub_arr(self, ctx:BKITParser.Sub_arrContext):
        pass


    # Enter a parse tree produced by BKITParser#arr_elem.
    def enterArr_elem(self, ctx:BKITParser.Arr_elemContext):
        pass

    # Exit a parse tree produced by BKITParser#arr_elem.
    def exitArr_elem(self, ctx:BKITParser.Arr_elemContext):
        pass



del BKITParser