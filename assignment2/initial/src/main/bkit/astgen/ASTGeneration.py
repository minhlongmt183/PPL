from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
from functools import reduce

class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        #  glo_var_decl_part func_decl_part EOF
        return Program(ctx.glo_var_decl_part().accept(self) + ctx.func_decl_part().accept(self))

    def visitGlo_var_decl_part(self, ctx:BKITParser.Glo_var_decl_partContext):
        # var_decl*
        if (ctx.getChildCount() == 0):
            return []
        return reduce(lambda x,y: x + y.accept(self), ctx.var_decl(), [])

    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        # VAR COLON variable_list_decl SEMI
        return ctx.variable_list_decl().accept(self)

    def visitVariable_list_decl(self, ctx:BKITParser.Variable_list_declContext):
        # variable_decl (COMMA variable_decl)*
        return [x.accept(self) for x in ctx.variable_decl()]

    def visitVariable_decl(self, ctx:BKITParser.Variable_declContext):
        # IDENT (LB INT_LIT RB)* ('='init_value)?
        
        variable = Id(ctx.IDENT().getText())
        varDimen = reduce(lambda x,y: x + [self.getINIT_Value(y.getText())], ctx.INT_LIT(), [])

        if ctx.init_value():
            varInit = ctx.init_value().accept(self)
        else:
            varInit = None

        return VarDecl(variable,varDimen,varInit)
    def visitInit_value(self, ctx:BKITParser.Init_valueContext):
        # literal
        return ctx.literal().accept(self)

    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        # bktype
        return ctx.bktype().accept(self)

    def visitBktype(self, ctx:BKITParser.BktypeContext):
        # primitive_type | compound_type

        return ctx.primitive_type().accept(self) if ctx.primitive_type() else ctx.compound_type().accept(self)

    def visitPrimitive_type(self, ctx:BKITParser.Primitive_typeContext):
        if ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        if ctx.INT_LIT():
            return IntLiteral(self.getINIT_Value(ctx.INT_LIT().getText()))
        if ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        if ctx.BOOL_LIT():
            return BooleanLiteral(ctx.BOOL_LIT().getText())


    def visitCompound_type(self, ctx:BKITParser.Compound_typeContext):
        # array
        return ctx.array().accept(self)

    def visitFunc_decl_part(self, ctx:BKITParser.Func_decl_partContext):
        # func_decl*
        # if (ctx.getChildCount() == 0):
        #     return []
        return [x.accept(self) for x in ctx.func_decl()]
        

    def visitFunc_decl(self, ctx:BKITParser.Func_declContext):
        # : FUNCTION COLON func_name
        #     (PARAMETER COLON param_list)?
        #   BODY COLON statement_list ENDBODY DOT


        name    = ctx.func_name().accept(self)
        param   = ctx.param_list().accept(self) if ctx.param_list() else []
        body    = ctx.statement_list().accept(self)

        return FuncDecl(name, param, body)

    def visitFunc_name(self, ctx:BKITParser.Func_nameContext):
        # IDENT
        return Id(ctx.IDENT().getText())

    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        # func_param_decl (COMMA func_param_decl)*
        return [x.accept(self) for x in ctx.func_param_decl()]



    def visitFunc_param_decl(self, ctx:BKITParser.Func_param_declContext):
        # IDENT (LB INT_LIT RB)*
        variable = Id(ctx.IDENT().getText())

        if ctx.INT_LIT():
            varDimen = [self.getINIT_Value(x.getText()) for x in ctx.INT_LIT()]
        else:
            varDimen = [] 
        varInit = None
        return VarDecl(variable,varDimen,varInit)
        

    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):

        var_decl_list = reduce(lambda x, y: x + y.accept(self), ctx.var_decl_statement(), [])
        stmt_list = [ctx.getChild(i).accept(self) for i in range(len(ctx.var_decl_statement()), ctx.getChildCount())]

        return (var_decl_list, stmt_list)
    

    def visitVar_decl_statement(self, ctx:BKITParser.Var_decl_statementContext):
        # VAR COLON variable_list_decl SEMI
        return ctx.variable_list_decl().accept(self)

    def visitAssign_statement(self, ctx:BKITParser.Assign_statementContext):
        # variable '=' expression SEMI
        return Assign(ctx.variable().accept(self), ctx.expression().accept(self))

    def visitIf_statement(self, ctx:BKITParser.If_statementContext):
        # IF expression THEN statement_list else_if_part* else_part? ENDIF DOT

        condition = ctx.expression().accept(self)
        body = ctx.statement_list().accept(self)

        ifthenStmt = [(condition, body[0], body[1])]
        if ctx.else_if_part():
            ifthenStmt += [elif_ctx.accept(self) for elif_ctx in ctx.else_if_part()]
        
        elseStmt = ctx.else_part().accept(self) if ctx.else_part() else ([], [])
        
        return If(ifthenStmt, elseStmt)
        
        
    def visitElse_if_part(self, ctx:BKITParser.Else_if_partContext):
        # ELSEIF expression THEN statement_list
        body = ctx.statement_list().accept(self)
        return (ctx.expression().accept(self), body[0], body[1])

    def visitElse_part(self, ctx:BKITParser.Else_partContext):
        # ELSE statement_list
        return ctx.statement_list().accept(self)

    def visitFor_statement(self, ctx:BKITParser.For_statementContext):
        #      FOR LR scal_var '=' expression COMMA expression COMMA expression  RR DO
        #  statement_list
        #  ENDFOR DOT
        idx1 = ctx.scal_var().accept(self)
        expr1 = ctx.expression(0).accept(self)
        expr2 = ctx.expression(1).accept(self)
        expr3 = ctx.expression(2).accept(self)
        loop = ctx.statement_list().accept(self) 

        return For(idx1, expr1, expr2, expr3, loop)
        

    def visitWhile_statement(self, ctx:BKITParser.While_statementContext):
        # WHILE expression DO statement_list ENDWHILE DOT
        return While(ctx.expression().accept(self), ctx.statement_list().accept(self))


    def visitDo_while_statement(self, ctx:BKITParser.Do_while_statementContext):
        #  DO statement_list WHILE expression ENDDO DOT
        return Dowhile(ctx.statement_list().accept(self), ctx.expression().accept(self))


    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return Continue()

    def visitCall_statement(self, ctx:BKITParser.Call_statementContext):
        # func_name LR param_func_call? RR SEMI
        if ctx.param_func_call():
            return CallStmt(ctx.func_name().accept(self), ctx.param_func_call().accept(self))
        
        return CallStmt(ctx.func_name().accept(self),'')



    def visitParam_func_call(self, ctx:BKITParser.Param_func_callContext):
        return reduce(lambda x,y: x + [y.accept(self)], ctx.expression(), [])


    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        # RETURN expression? SEMI
        if ctx.expression():
            ret_expr = ctx.expression().accept(self)
        else:
            ret_expr = None
        return Return(ret_expr)

    def visitVariable_list(self, ctx:BKITParser.Variable_listContext):
        # variable (COMMA variable)*
        return reduce(lambda x,y: x + y.accept(self), ctx.variable(), [])
        

    def visitVariable(self, ctx:BKITParser.VariableContext):
        #     : scal_var
        #     | comp_var
        #     | expression
        #     ;
        return ctx.getChild(0).accept(self)

    def visitScal_var(self, ctx:BKITParser.Scal_varContext):
        # IDENT
        return Id(ctx.IDENT().getText())

    def visitComp_var(self, ctx:BKITParser.Comp_varContext):
        #  IDENT (LB (literal | expression) RB)+
        
        arr = Id(ctx.IDENT().getText())
        idx_list = ctx.literal() + ctx.expression()
        idx = [x.accept(self) for x in idx_list]

        return ArrayCell(arr, idx)

    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if (ctx.getChildCount() == 1):
            return ctx.exp1(0).accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))

    def visitExp1(self, ctx:BKITParser.Exp1Context):

        if (ctx.getChildCount() == 1):
            return ctx.exp2().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp1().accept(self), ctx.exp2().accept(self))

    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if (ctx.getChildCount() == 1):
            return ctx.exp3().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp2().accept(self), ctx.exp3().accept(self))

    def visitExp3(self, ctx:BKITParser.Exp3Context):
        if (ctx.getChildCount() == 1):
            return ctx.exp4().accept(self)
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp3().accept(self), ctx.exp4().accept(self))

    def visitExp4(self, ctx:BKITParser.Exp4Context):
        if (ctx.getChildCount() == 1):
            return ctx.exp5().accept(self)
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp4().accept(self))

    def visitExp5(self, ctx:BKITParser.Exp5Context):
        if (ctx.exp6()):
            return ctx.exp6().accept(self)
        return UnaryOp(ctx.getChild(0).getText(), ctx.exp5().accept(self))

    def visitExp6(self, ctx:BKITParser.Exp6Context):
            # : name_index_op index_operator
            # | exp7

        if (ctx.getChildCount() == 1):
            return ctx.exp7().accept(self)
        
        return ArrayCell(ctx.name_index_op().accept(self), ctx.index_operator().accept(self))

    def visitExp7(self, ctx:BKITParser.Exp7Context):
        # : operand
        # | LR expression RR
        return ctx.operand().accept(self) if ctx.operand() else ctx.expression().accept(self)

    def visitName_index_op(self, ctx:BKITParser.Name_index_opContext):
        # : IDENT
        # | func_call_expr
        # | LR expression RR
        #     return ctx.getChild(0).accept(self)
        if ctx.IDENT():
            return Id(ctx.IDENT().getText())
        if ctx.func_call_expr():
            return ctx.func_call_expr().accept(self)
        return ctx.expression().accept(self)

    def visitOperand(self, ctx:BKITParser.OperandContext):
        return ctx.getChild(0).accept(self)

    def visitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        #  :  LB expression RB
        #  | LB expression RB index_operator

        if ctx.index_operator():
            return [ctx.expression().accept(self)] + ctx.index_operator().accept(self)
        return [ctx.expression().accept(self)]

    def visitFunc_call_expr(self, ctx:BKITParser.Func_call_exprContext):
        # IDENT LR param_func_call? RR

        method = Id(ctx.IDENT().getText())
        param = ctx.param_func_call().accept(self) if ctx.param_func_call() else []
        return CallExpr(method, param)

    def visitArray(self, ctx:BKITParser.ArrayContext):
        # LCURLY arr_elem_list? RCURLY
        return ArrayLiteral(ctx.arr_elem_list().accept(self) if ctx.arr_elem_list() else [])

    def visitArr_elem_list(self, ctx:BKITParser.Arr_elem_listContext):
        # (arr_elem (COMMA arr_elem)*)
        return reduce(lambda x,y: x + [y.accept(self)], ctx.arr_elem(), [])

    def visitArr_elem(self, ctx:BKITParser.Arr_elemContext):
        if ctx.bktype():
            return ctx.bktype().accept(self)
        return Id(ctx.IDENT().getText())

    def getINIT_Value(self, int_str):
        int_val_str = int_str.lower()
        if '0o' in int_val_str:
            return int(int_val_str,base=8)
        if '0x' in int_val_str:
            return int(int_val_str,base=16)
        return int(int_val_str)

