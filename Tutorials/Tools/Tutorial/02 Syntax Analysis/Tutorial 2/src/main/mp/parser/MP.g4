/*
   **************************************
   * Student name: Nguyen Ho Minh Phuoc *
   * Student ID: 1612736                *
   **************************************
*/



grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


program:
    program declaration_variables
    | program declaration_function
    | declaration_variables
    | declaration_function
    ;


// Variables
variable_list
    : variable_list CM ID
    | ID
    ;

// Declarations


parameters_list:
    parameters_list SM types variable_list
    | types variable_list
    ;
    
declaration_variables
    : types variable_list SM
    ;
    
declaration_parameters
    : LP parameters_list RP
    | LP RP
    ;

declaration_function:
    types ID declaration_parameters body
    ;
    
// Body
body:
    LB (compound) RB
    ;

compound:
    compound declaration_variables
    | compound statement
    | statement
    | declaration_variables
    |
    ;

// Statement
statement:
    statement_assignment
    | statement_call
    | statement_return
    ;

statement_assignment:
    ID '=' expression SM
    ;

expression_list:
    expression_list CM expression
    | expression
    ;

expression_call:
    ID LP expression_list RP
    | ID LP RP
    ;

statement_call:
    expression_call SM
    ;

statement_return:
    'return' expression SM
    ;
    

// Expression
expression
    : expression_3 ADD expression
    | expression_3
    ;

expression_3
    : expression_4 SUB expression_4
    | expression_4
    ;

expression_4
    : expression_4 MUL expression_5
    | expression_4 DIV expression_5
    | expression_5
    ;

expression_5
    : LP expression RP
    | operand
    ;

operand:
    INTLIT
    | FLOATLIT
    | expression_call
    ;
// types
types:
    INT
    | FLOAT
    ;


INTLIT: [0-9]+;
FLOATLIT: [0-9]+ ('.' [0-9]*)? ([-]?[eE][0-9]+)?
        | '.' [0-9]+ ([-]?[eE][0-9]+)?
        ;
INT: 'int';
FLOAT: 'float';
RETURN: 'return';
LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z0-9_]*;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;


/*

*/