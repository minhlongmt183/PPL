grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
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

// program  : Identifier1 Identifier2 REAL STR EOF ;
program
    : manydecl EOF
    ;

manydecl
    : decl manydecl
    | decl
    ;

decl
    : var_decl
    | func_decl
    ;

var_decl
    : data_type id_list SM
    ;

data_type
    : INT | FLOAT
    ;

id_list
    : ID (CM ID)*
    |
    ;

func_decl
    : data_type ID param_decl body
    ;

param_decl
    : LP param_list? RP
    ;

param_list
    : data_type id_list (SM (data_type id_list) )*
    ;

body
    : LB (var_decl_list | statement)* RB
    ;

var_decl_list
    : var_decl (SM var_decl)*
    ;

statement
    : assign_stmt SM
    | call_stmt SM
    | ret_stmt SM
    ;

assign_stmt
    : ID EQ exp
    ;

call_stmt
    : ID LP call_param? RP
    ;

call_param
    : ( one_param (CM one_param)*)
    ;
one_param
    : INTLIT
    | FLOATLIT
    | param_list
    ;



ret_stmt
    : RETURN exp
    ;


// exp
//     :   LB exp RB
//     |   <assoc = left> exp MUL exp
//     |   <assoc = left> exp DIV exp
//     |   exp SUB exp
//     |   <assoc = right> exp ADD exp
//     |   operands
//     ;

exp
    :   exp1 ADD exp
    |   exp1
    ;


exp1
    :   exp2 SUB exp2
    |   exp2
    ;
exp2
    :   exp3 (MUL | DIV) exp2
    |   exp3
    ;

exp3
    :   LP exp RP
    | operands
    ;

operands
    :   ID
    |   INTLIT
    |   FLOATLIT
    |   call_stmt
    ;

comment: COMMENT;

COMMENT
    : ('""' .*?'""') -> skip
    ;





INT     : 'int';
FLOAT   : 'float';
RETURN  : 'return';
LB      : '{';
RB      : '}';
SM      : ';';
CM      : ',';
EQ      : '=';
LP      : '(';
RP      : ')';
ADD     : '+';
SUB     : '-';
MUL     : '*';
DIV     : '/';
ID      : LETTER (LETTER | DIGIT)* ;
LETTER  : (LOWER_LETTER | UPPER_LETTER);
FLOATLIT    :   INT_PART ( DEC_PART | EPX_PART | DEC_PART EPX_PART);
INTLIT  : INT_PART;



// ------------------------------ Tut1 --------------------
// // Question 1
Identifier1 :   [a-z][a-z0-9]* ;


// Question 2
fragment LOWER_LETTER:    [a-z];
fragment UPPER_LETTER:    [A-Z];
fragment DIGIT:    [0-9];
Identifier2:     LOWER_LETTER (LOWER_LETTER | DIGIT)*;



// Question 3
// a)
REAL    :   INT_PART ( DEC_PART | EPX_PART | DEC_PART EPX_PART);

fragment    INT_PART:   [1-9] DIGIT* | '0'+;
fragment    DEC_PART:   '.' DIGIT+;
fragment    EPX_PART:   'e' '-'? DIGIT+;
// fragment    DIGIT:  [0-9];

// b)
STR     :   '\'' (DOUBLE_QUOTE | ~'\'')* '\'';
fragment    DOUBLE_QUOTE:   '\'\'';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

