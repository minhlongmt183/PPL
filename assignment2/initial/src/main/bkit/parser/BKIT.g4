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
        raise IllegalEscape(self.text[1:])
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
    : VAR COLON variable_list_decl SEMI
    ;

variable_list_decl
    : variable_decl (COMMA variable_decl)*
    ;

variable_decl
    : IDENT (LB INT_LIT RB)* ('='init_value)?
    ;


init_value
    : literal (COMMA literal)*
    ;

literal
    : bktype
    ;

bktype
    : primitive_type
    | compound_type
    ;

primitive_type
    : FLOAT_LIT
    | INT_LIT
    | STRING_LIT
    | BOOL_LIT
    ;

compound_type
    : array
    ;


func_decl_part
    : func_decl*
    ;

func_decl
    : FUNCTION COLON func_name
        (PARAMETER COLON param_list)?
      BODY COLON statement_list ENDBODY DOT
    ;

func_name
    : IDENT
    ;

param_list
    : func_param_decl (COMMA func_param_decl)*
    ;

func_param_decl
    : IDENT (LB INT_LIT RB)*
    ;

statement_list
    : var_decl_statement*
    ( assign_statement
    | if_statement
    | for_statement
    | while_statement
    | do_while_statement
    | break_statement
    | continue_statement
    | call_statement
    | return_statement
    )*
    ;

var_decl_statement
    : VAR COLON variable_list_decl SEMI
    ;

assign_statement
    : variable '=' expression SEMI
    ;

if_statement
    : IF expression THEN statement_list else_if_part* else_part? ENDIF DOT
    ;

else_if_part
    : ELSEIF expression THEN statement_list
    ;

else_part
    : ELSE statement_list
    ;

for_statement
    : FOR LR scal_var '=' expression COMMA expression COMMA expression  RR DO
     statement_list
     ENDFOR DOT
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
    : func_name LR param_func_call? RR SEMI
    ;

param_func_call
    : expression (COMMA expression)*
    ;

return_statement
    : RETURN expression? SEMI
    ;

variable_list
    : variable (COMMA variable)*
    ;
variable
    : scal_var
    | comp_var
    ;

scal_var
    : IDENT
    ;

comp_var
    : IDENT (LB (literal | expression) RB)+
    ;


////////////////////////////////////////////////////////////////////////////////////////


// expression
expression
    : exp1 ('==' | '!=' | '<' | '>' | '<=' | '>='
        | '=/=' | '<.' | '>.' | '<=.' | '>=.') exp1
    | exp1
    ;

exp1
    : exp1 ('&&' | '||') exp2
    | exp2
    ;

exp2
    : exp2 ('+' | '+.' | '-' | '-.')+ exp3
    | exp3
    ;
exp3
    : exp3 ('*' | '*.' | '\\' | '\\.' | '%') exp4
    | exp4
    ;
exp4
    : '!' exp4
    | exp5
    ;
exp5
    : ('-' | '-.') exp5
    | exp6
    ;

exp6
    : name_index_op index_operator
    | exp7
    ;

exp7
    : operand
    | LR expression RR
    ;

name_index_op
    : IDENT
    | func_call_expr
    ;



operand
    : func_name
    | literal
    | func_call_expr
    ;
index_operator
    :  LB expression RB
    | LB expression RB index_operator
    ;

func_call_expr
    : IDENT LR param_func_call? RR
    ;

array
    : LCURLY arr_elem_list? RCURLY
    ;

arr_elem_list
    : (arr_elem (COMMA arr_elem)*)
    ;

arr_elem
    : bktype
    | IDENT
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
ENDDO       : 'EndDo';

// Operators
////////////////////////////////////////////////////////////////////////////////////////

// Literal

FLOAT_LIT
    : INT_PART (DEC_PART | EXP_PART | DEC_PART EXP_PART)
    ;

fragment INT_PART
    : [0-9]+
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


fragment DEC_PART
    : DOT [0-9]*
    ;

fragment EXP_PART
    : ('E' | 'e') ('+' | '-')? [0-9]+
    ;

BOOL_LIT
    : 'True'
    | 'False'
    ;

STRING_LIT
    : UNCLOSE_STRING'"'
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



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


UNCLOSE_STRING
    : '"' ('\\' [btrnf\\'] | '\'"' | ~[\b\t\r\n\f\\'"])* ('\n' | EOF)?
    ;
UNTERMINATED_COMMENT: '**' .*?;
ILLEGAL_ESCAPE: UNCLOSE_STRING (('\\' ~[btnfr'\\]) | '\'' ~'"') ;
ERROR_CHAR: .;