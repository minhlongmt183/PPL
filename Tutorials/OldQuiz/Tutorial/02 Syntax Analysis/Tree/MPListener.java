// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MPParser}.
 */
public interface MPListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MPParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MPParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#many_declarations}.
	 * @param ctx the parse tree
	 */
	void enterMany_declarations(MPParser.Many_declarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#many_declarations}.
	 * @param ctx the parse tree
	 */
	void exitMany_declarations(MPParser.Many_declarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(MPParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(MPParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void enterVariable_declaration(MPParser.Variable_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#variable_declaration}.
	 * @param ctx the parse tree
	 */
	void exitVariable_declaration(MPParser.Variable_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_declarations}.
	 * @param ctx the parse tree
	 */
	void enterList_declarations(MPParser.List_declarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_declarations}.
	 * @param ctx the parse tree
	 */
	void exitList_declarations(MPParser.List_declarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#v_declaration}.
	 * @param ctx the parse tree
	 */
	void enterV_declaration(MPParser.V_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#v_declaration}.
	 * @param ctx the parse tree
	 */
	void exitV_declaration(MPParser.V_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_identifiers}.
	 * @param ctx the parse tree
	 */
	void enterList_identifiers(MPParser.List_identifiersContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_identifiers}.
	 * @param ctx the parse tree
	 */
	void exitList_identifiers(MPParser.List_identifiersContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration(MPParser.Function_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration(MPParser.Function_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_parameters}.
	 * @param ctx the parse tree
	 */
	void enterList_parameters(MPParser.List_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_parameters}.
	 * @param ctx the parse tree
	 */
	void exitList_parameters(MPParser.List_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#not_null_list_parameters}.
	 * @param ctx the parse tree
	 */
	void enterNot_null_list_parameters(MPParser.Not_null_list_parametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#not_null_list_parameters}.
	 * @param ctx the parse tree
	 */
	void exitNot_null_list_parameters(MPParser.Not_null_list_parametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#parameter_declaration}.
	 * @param ctx the parse tree
	 */
	void enterParameter_declaration(MPParser.Parameter_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#parameter_declaration}.
	 * @param ctx the parse tree
	 */
	void exitParameter_declaration(MPParser.Parameter_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#procedure_declaration}.
	 * @param ctx the parse tree
	 */
	void enterProcedure_declaration(MPParser.Procedure_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#procedure_declaration}.
	 * @param ctx the parse tree
	 */
	void exitProcedure_declaration(MPParser.Procedure_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(MPParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(MPParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#types}.
	 * @param ctx the parse tree
	 */
	void enterTypes(MPParser.TypesContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#types}.
	 * @param ctx the parse tree
	 */
	void exitTypes(MPParser.TypesContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_type(MPParser.Primitive_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#primitive_type}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_type(MPParser.Primitive_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#compound_type}.
	 * @param ctx the parse tree
	 */
	void enterCompound_type(MPParser.Compound_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#compound_type}.
	 * @param ctx the parse tree
	 */
	void exitCompound_type(MPParser.Compound_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#array_type}.
	 * @param ctx the parse tree
	 */
	void enterArray_type(MPParser.Array_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#array_type}.
	 * @param ctx the parse tree
	 */
	void exitArray_type(MPParser.Array_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(MPParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(MPParser.OperandContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(MPParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(MPParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_1}.
	 * @param ctx the parse tree
	 */
	void enterExpression_1(MPParser.Expression_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_1}.
	 * @param ctx the parse tree
	 */
	void exitExpression_1(MPParser.Expression_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_2}.
	 * @param ctx the parse tree
	 */
	void enterExpression_2(MPParser.Expression_2Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_2}.
	 * @param ctx the parse tree
	 */
	void exitExpression_2(MPParser.Expression_2Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_3}.
	 * @param ctx the parse tree
	 */
	void enterExpression_3(MPParser.Expression_3Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_3}.
	 * @param ctx the parse tree
	 */
	void exitExpression_3(MPParser.Expression_3Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_4}.
	 * @param ctx the parse tree
	 */
	void enterExpression_4(MPParser.Expression_4Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_4}.
	 * @param ctx the parse tree
	 */
	void exitExpression_4(MPParser.Expression_4Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_5}.
	 * @param ctx the parse tree
	 */
	void enterExpression_5(MPParser.Expression_5Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_5}.
	 * @param ctx the parse tree
	 */
	void exitExpression_5(MPParser.Expression_5Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#expression_6}.
	 * @param ctx the parse tree
	 */
	void enterExpression_6(MPParser.Expression_6Context ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#expression_6}.
	 * @param ctx the parse tree
	 */
	void exitExpression_6(MPParser.Expression_6Context ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#arr_element}.
	 * @param ctx the parse tree
	 */
	void enterArr_element(MPParser.Arr_elementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#arr_element}.
	 * @param ctx the parse tree
	 */
	void exitArr_element(MPParser.Arr_elementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#func_call}.
	 * @param ctx the parse tree
	 */
	void enterFunc_call(MPParser.Func_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#func_call}.
	 * @param ctx the parse tree
	 */
	void exitFunc_call(MPParser.Func_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_expression}.
	 * @param ctx the parse tree
	 */
	void enterList_expression(MPParser.List_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_expression}.
	 * @param ctx the parse tree
	 */
	void exitList_expression(MPParser.List_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#not_null_list_expression}.
	 * @param ctx the parse tree
	 */
	void enterNot_null_list_expression(MPParser.Not_null_list_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#not_null_list_expression}.
	 * @param ctx the parse tree
	 */
	void exitNot_null_list_expression(MPParser.Not_null_list_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MPParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MPParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#assignment_statement}.
	 * @param ctx the parse tree
	 */
	void enterAssignment_statement(MPParser.Assignment_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#assignment_statement}.
	 * @param ctx the parse tree
	 */
	void exitAssignment_statement(MPParser.Assignment_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_var_idx_ass}.
	 * @param ctx the parse tree
	 */
	void enterList_var_idx_ass(MPParser.List_var_idx_assContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_var_idx_ass}.
	 * @param ctx the parse tree
	 */
	void exitList_var_idx_ass(MPParser.List_var_idx_assContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void enterIf_statement(MPParser.If_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#if_statement}.
	 * @param ctx the parse tree
	 */
	void exitIf_statement(MPParser.If_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#while_statement}.
	 * @param ctx the parse tree
	 */
	void enterWhile_statement(MPParser.While_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#while_statement}.
	 * @param ctx the parse tree
	 */
	void exitWhile_statement(MPParser.While_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void enterFor_statement(MPParser.For_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#for_statement}.
	 * @param ctx the parse tree
	 */
	void exitFor_statement(MPParser.For_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void enterBreak_statement(MPParser.Break_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#break_statement}.
	 * @param ctx the parse tree
	 */
	void exitBreak_statement(MPParser.Break_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void enterContinue_statement(MPParser.Continue_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#continue_statement}.
	 * @param ctx the parse tree
	 */
	void exitContinue_statement(MPParser.Continue_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void enterReturn_statement(MPParser.Return_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#return_statement}.
	 * @param ctx the parse tree
	 */
	void exitReturn_statement(MPParser.Return_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#compound_statement}.
	 * @param ctx the parse tree
	 */
	void enterCompound_statement(MPParser.Compound_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#compound_statement}.
	 * @param ctx the parse tree
	 */
	void exitCompound_statement(MPParser.Compound_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#list_statements}.
	 * @param ctx the parse tree
	 */
	void enterList_statements(MPParser.List_statementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#list_statements}.
	 * @param ctx the parse tree
	 */
	void exitList_statements(MPParser.List_statementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#not_null_list_statements}.
	 * @param ctx the parse tree
	 */
	void enterNot_null_list_statements(MPParser.Not_null_list_statementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#not_null_list_statements}.
	 * @param ctx the parse tree
	 */
	void exitNot_null_list_statements(MPParser.Not_null_list_statementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#with_statement}.
	 * @param ctx the parse tree
	 */
	void enterWith_statement(MPParser.With_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#with_statement}.
	 * @param ctx the parse tree
	 */
	void exitWith_statement(MPParser.With_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MPParser#call_statement}.
	 * @param ctx the parse tree
	 */
	void enterCall_statement(MPParser.Call_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MPParser#call_statement}.
	 * @param ctx the parse tree
	 */
	void exitCall_statement(MPParser.Call_statementContext ctx);
}