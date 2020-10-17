// MSSV: 1812951

grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program 
    : glo_var_decl_part func_decl_part EOF 
    ;

glo_var_decl_part
    : var_decl*
    ;

var_decl
    : VAR COLON variable_list SEMI
    ;

variable_list
    : variable (COMMA variable)* ('=' init_value)?
    ;

variable
    : scal_var
    | comp_var
    ;

scal_var
    : IDENT 
    ; 

comp_var
    : IDENT (LB INT_LIT RB)+
    ;

init_value
    : literal (COMMA literal)*
    ;

literal
    : INT_LIT
    | FLOAT_LIT
    | BOOL_LIT
    | STRING_LIT
    | IDENT
    | array
    ;


func_decl_part
    : func_decl*
    ;

func_decl
    : FUNCTION COLON func_name
        (PARAMETER COLON param_list)?
      BODY statement_list ENDBODY DOT
    ;

func_name
    : IDENT
    ;

param_list
    : param (COMMA param)*
    ;

param
    : scal_parm
    | comp_parm
    ;

scal_parm
    : IDENT
    ;

comp_parm
    : IDENT (LB INT_LIT RB)+
    ;
statement_list
    : var_decl_statement
    | assign_statement
    | if_statement
    | for_statement
    | while_statement
    | do_while_statement
    | break_statement
    | continue_statement
    | call_statement
    | return_statement
    ;

var_decl_statement
    : VAR COLON variable_list SEMI
    ;

assign_statement
    : variable '==' expression SEMI
    ;

if_statement
    : IF expression THEN statement_list else_if_part* else_part* ENDIF DOT
    ;

else_if_part
    : ELSEIF expression THEN statement_list
    ;

else_part
    : ELSE statement_list
    ;

for_statement
    : FOR LB scal_var '==' expression COMMA expression COMMA expression  RB DO ENDFOR
    ;

while_statement
    : WHILE expression DO statement_list ENDWHILE DOT
    ;

do_while_statement
    : DO statement_list WHILE expression ENDDO DOT
    ;

break_statement
    : BREAK SEMI
    ;

continue_statement
    : CONTINUE SEMI
    ;

call_statement
    : func_name LB param_func_call? RB SEMI
    ;

param_func_call
    : (IDENT | CONST | expression) (COMMA expression)*
    ;

return_statement
    : RETURN expression? SEMI
    ;

////////////////////////////////////////////////////////////////////////////////////////


// expression
expression
    : arith_expr
    | bool_expr
    | rela_expr
    | func_call_expr
    ;

arith_expr
    : arith_expr ('+' | '+.' | '-' | '-.') arith_expr1
    | arith_expr1 
    ;
arith_expr1
    : arith_expr1 ('*' | '*.' | '\\' | '\\.' | '%') arith_expr2
    | arith_expr2
    ;
arith_expr2
    : arith_expr3 ('-' | '-.') arith_expr2
    | arith_expr3
    ;
arith_expr3
    : LR arith_expr3 RR
    | operand
    ;
operand
    : IDENT
    | INT_LIT
    | FLOAT_LIT
    | func_call_expr
    ;


bool_expr
    : '!' bool_expr1
    | bool_expr1
    ;
bool_expr1
    : bool_expr1 ('&&' | '||') bool_expr2
    | bool_expr2
    ;
bool_expr2
    : LR bool_expr2 RR
    | operand
    ;

rela_expr
    : rela_expr ('==' | '!=' | '<' | '>' | '<=' | '>=' 
        | '=/=' | '<.' | '>.' | '<=.' | '>=.') rela_expr
    | rela_expr1
    ;
rela_expr1
    : LR rela_expr RR
    | operand
    ;

elem_express
    : expression index_expr
    ;
index_expr
    : LB expression RR
    | LR expression RR index_expr
    ;

func_call_expr
    : IDENT LR param_func_call? RR
    ;



array
    : LCURLY arr_elem_list RCURLY
    ;

arr_elem_list
    : (arr_elem (COMMA arr_elem)*)
    | (sub_arr (COMMA sub_arr)*)
    ;
sub_arr
    : (arr_elem (COMMA arr_elem)*)
    ;

arr_elem
    : STRING_LIT
    | BOOL_LIT
    | INT_LIT
    | FLOAT_LIT
    | WS
    ;

///////////////////////////////////////////////////////////////////////////////////////////
// Lexer
// Comment
COMMENT
    : ('**' .*? '**')+ -> skip
    ;

IDENT
    : [a-z] [a-zA-Z0-9_]*
    ;

// Keywords
BODY        : 'Body';
BREAK       : 'Break';
CONTINUE    : 'Continue';
DO          : 'Do';
ELSE        : 'Else';
ELSEIF      : 'ElseIf';
ENDBODY     : 'EndBody';
ENDIF       : 'EndIf';
ENDFOR      : 'EndFor';
ENDWHILE    : 'EndWhile';
FOR         : 'For';
FUNCTION    : 'Function';
IF          : 'If';
PARAMETER   : 'Parameter';
RETURN      : 'Return';
THEN        : 'Then';
VAR         : 'Var';
WHILE       : 'While';
TRUE        : 'True';
FALSE       : 'False';
ENDDO       : 'EndDo';

// Operators
////////////////////////////////////////////////////////////////////////////////////////

// Literal


CONST
    : INT_LIT
    | FLOAT_LIT
    ;

INT_LIT
    : '0'
    | DEC
    | OCT
    | HEX
    ;

fragment DEC
    : [1-9] [0-9]*
    ;

fragment OCT
    : '0' ('O' | 'o') [1-7] [0-7]*
    ;

fragment HEX
    : '0' ('X' | 'x') [1-9A-F] [0-9A-F]*
    ;

FLOAT_LIT
    : ('0' | DEC) (DEC_PART | EXP_PART | DEC_PART EXP_PART)
    ;


fragment DEC_PART
    : DOT [0-9]*
    ;

fragment EXP_PART
    : ('E' | 'e') ('+' | '-')? [0-9]+
    ;

BOOL_LIT
    : TRUE
    | FALSE
    ;

STRING_LIT
    : UNCLOSE_STRING '"'
    {self.text = self.text[1:-1]}
    ;


// Separators
LCURLY      : '{';
RCURLY      : '}';
LR          : '(';
RR          : ')';
LB          : '[';
RB          : ']';
SEMI        : ';';
DOT         : '.';
COMMA       : ',';
COLON       : ':';



fragment ESCAPE_STRING
    : '\\b'
    | '\\f'
    | '\\r'
    | '\\n'
    | '\\t'
    | '\\\''
    | '\\'
    | '\\\\'
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



ILLEGAL_ESCAPE: UNCLOSE_STRING (('\\' ~[btnfr'\\]) | '\'') ;
UNCLOSE_STRING
    : '"' ('\\' [btrnf\\'] | '\'"' | ~[\b\t\r\n\f\\'"])*
    ;
UNTERMINATED_COMMENT: '**' .*?;
ERROR_CHAR: .;