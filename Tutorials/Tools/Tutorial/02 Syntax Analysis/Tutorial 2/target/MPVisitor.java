// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1

    package mc.parser;

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MPParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MPVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MPParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MPParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(MPParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#vardeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardeclaration(MPParser.VardeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#primitivetype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitivetype(MPParser.PrimitivetypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#variablelist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariablelist(MPParser.VariablelistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable(MPParser.VariableContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#funcdeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncdeclaration(MPParser.FuncdeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(MPParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#parameterlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterlist(MPParser.ParameterlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#parameterdeclaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterdeclaration(MPParser.ParameterdeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#blockstatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlockstatement(MPParser.BlockstatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#operator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperator(MPParser.OperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#separator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSeparator(MPParser.SeparatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(MPParser.LiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#arraypointerinput}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArraypointerinput(MPParser.ArraypointerinputContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#arraypointeroutput}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArraypointeroutput(MPParser.ArraypointeroutputContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(MPParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression1(MPParser.Expression1Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression2(MPParser.Expression2Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression3(MPParser.Expression3Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression4(MPParser.Expression4Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression5(MPParser.Expression5Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression6}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression6(MPParser.Expression6Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression7}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression7(MPParser.Expression7Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression8}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression8(MPParser.Expression8Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expression9}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression9(MPParser.Expression9Context ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(MPParser.OperandContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#functioncall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctioncall(MPParser.FunctioncallContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#expressionlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionlist(MPParser.ExpressionlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(MPParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#ifstatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfstatement(MPParser.IfstatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#dowhilestatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDowhilestatement(MPParser.DowhilestatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#forstatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForstatement(MPParser.ForstatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MPParser#returnstatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnstatement(MPParser.ReturnstatementContext ctx);
}