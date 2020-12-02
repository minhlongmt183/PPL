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

program  : 'int' 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

/*  Section 2: Program Structure
***************************************
*/

// *************************
//  Part 2.1: Variable declaration
variable_declaration:
    VAR variable_declaration_list SEMI
    ;

variable_declaration_list:
    variable_declaration_list SEMI variable_declacation_single
    | variable_declacation_single
    ;

variable_declacation_single: 
    variable_list COLON types
    ;

variable_list: 
    variable COMMA variable_list
    | variable
    ;

variable: 
    IDENTIFIER
    ;

//  End Part 2.1
// *************************

// *************************
//  Part 2.2: Function declaration
function_delcaration:
    FUNCTION IDENTIFIER (LB variable_declaration_list RB | LB RB) COLON types SEMI variable_declaration statement_compound;
    
// parameter_list:
//     variable_declaration_list
//     ;

// End Part 2.2
// *************************

// *************************
//  Part 2.3: Procedure declaration
procedure_declaration:
    PROCEDURE IDENTIFIER (LB variable_declaration_list RB | LB RB) SEMI variable_declaration statement_compound;
//  End Part 2.3
// *************************


/*  Section 3: Lexical Specification
***************************************
*/

// *************************
//  Part 3.1: Character Set
fragment A: [Aa];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];


// *************************
// Part 3.2: Comments
LINE_CMT: '//'~[\n]* -> skip ;

BLOCK_CMT_1: '/*' .*? '*/' -> skip;
BLOCK_CMT_2: '(*' .*? '*)' -> skip;
// End Comments
// *************************


// *************************
// Part 3.3: Token Set


// - Identifiers
identifier: ;
IDENTIFIER: [A-Za-z_][A-Za-z0-9]*;
// - End Identifiers

// - Keywords
// ? with
BREAK: B R E A K;
CONTINUE: C O N T I N U E;

FOR: F O R;
WHILE: W H I L E;
TO: T O;
DOWNTO: D O W N T O;
WITH: W I T H;
DO: D O;

IF: I F;
THEN: T H E N;
ELSE: E L S E;

VAR: V A R;
OF: O F;

BEGIN: B E G I N;
END: E N D;
RETURN: R E T U R N;

FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;

TRUE: T R U E;
FALSE: F A L S E;

ARRAY: A R R A Y;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
// - End Keywords

// - Operators
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;

ADD: '+';
SUB: '-';
MUL: '*';
DIV_F: '/';

EQUAL: '=';
NOTEQUAL: '<>';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';

ANDTHEN: A N D ' ' T H E N;
ORELSE: O R ' ' E L S E;

// OR_OP: '||';
// AND_OP: '&&';
// NOT_OP: '!';
// CONCAT_OP: '^';
ASSIGN_OP: ':=';
// - End Operators

// End Token Set
// *************************


// *************************
// Part 3.4: Separators
LSB: '[';
RSB: ']';
COLON: ':';
LB: '(' ;
RB: ')' ;
SEMI: ';';
DDOT: '..';
COMMA: ',';
LP: '{';
RP: '}';
// DOT: '.';
// End seperators
// *************************


// *************************
// Part 3.5: Literals
literal:
    INTLIT 
    | REALLIT 
    | BOOLEANLIT 
    | STRINGLIT
    ;

fragment DIGIT: [0-9];
INTLIT: DIGIT+;

fragment EXPONENT: [eE] '-'? DIGIT+ ;
REALLIT: DIGIT+ ('.' DIGIT*)? EXPONENT?
        | '.' DIGIT+ EXPONENT?
        ;
// 1.E10?

BOOLEANLIT: TRUE | FALSE ;

// STRINGLIT: ;

fragment BSP: '\\b';
fragment FF: '\\f';
fragment CR: '\\r';
fragment NEWLINE: '\\n';
fragment TAB: '\\t';
fragment SQUOTE: '\\\'';
fragment DQUOTE: '\\"';
fragment BSL: '\\''\\';
fragment LEGAL_ESCAPE:
    BSP
    | FF
    | CR
    | NEWLINE
    | TAB
    | SQUOTE
    | DQUOTE
    | BSL
    ;
    
ILLEGAL_EXCAPE: '"' (~([\n\r] | '"' | '\\') | LEGAL_ESCAPE)*? '\\' ~([brnft] | '"' | '\'' | '\\')
{
    setText(getText().substring(1, getText().length()));
};

UNCLOSE_STRING: '"' (~([\n\r] | '"' | '\\') | LEGAL_ESCAPE)*
{
    setText(getText().substring(1, getText().length()));
};

STRINGLIT: UNCLOSE_STRING '"'
{
    setText(getText().substring(1, getText().length() - 1));
};

// End Literals
// *************************

/*  Section 4: Types and Values
***************************************
*/

// *************************
types: 
    type_primitive
    | type_compound
    ;
type_primitive: 
    INTEGER
    | REAL 
    | BOOLEAN 
    | STRING 
    ;

type_compound:
    type_array
    ;

// Part 4.1: The boolean Types and Values
// End Part 4.1

// Part 4.2: The integer Type and Values
// End Part 4.2

// Part 4.3: The real Type and Values
// End Part 4.3

// Part 4.4: Array Types and Their Values
type_array:
    ARRAY LSB INTLIT DDOT INTLIT RSB OF type_primitive
    ;
// End Part 4.4

/*  Section 5: Expressions
***************************************
*/

// Part 5.1: Precedence and Associativity
expression_list:
    expression_list COMMA expression
    | expression
    ;

expression: 
    expression ANDTHEN expression_4
    | expression ORELSE expression_4
    | expression_4
    ;

expression_4: 
    expression_5 EQUAL expression_5
    | expression_5 NOTEQUAL expression_5
    | expression_5 LESSTHAN expression_5
    | expression_5 GREATERTHAN expression_5
    | expression_5 LESSEQUAL expression_5
    | expression_5 GREATEREQUAL expression_5
    | expression_5
    ;

expression_5:
    expression_5 ADD expression_6
    | expression_5 SUB expression_6
    | expression_5 OR expression_6
    | expression_6
    ;

expression_6:
    expression_6 DIV_F expression_7
    | expression_6 MUL expression_7
    | expression_6 DIV expression_7
    | expression_6 MOD expression_7
    | expression_6 AND expression_7
    | expression_7
    ;

expression_7: 
    SUB expression_7
    | NOT expression_7
    | expression_8
    ;

expression_8: 
    expression_9 LSB expression RSB
    | expression_9
    ;

expression_9: 
    LB expression RB
    | operand
    ;

operand:
    IDENTIFIER
    | literal
    | funcall
    ;

    
// End Part 5.1

// Part 5.2: Type Coercions
// End Part 5.2

// Part 5.3: Index Expression
// End Part 5.3

// Part 5.4: Invocation Expression
// End Part 5.4

// Part 5.5 Evaluation Order
// End Part 5.5


/*  Section 6: Statements and Control Flow
***************************************
*/
statement: 
    expression SEMI
    | statement_break
    | statement_call
    | statement_compound
    | statement_continue
    | statement_for
    | statement_if
    | statement_return
    | statement_while
    | statement_with
    ;

// Part 6.1: Assignment Statement
// End Part 6.1

// Part 6.2: The if Statement
statement_if: 
    IF expression THEN statement (ELSE statement)? ;
// End Part 6.2

// Part 6.3: The while Statement
statement_while: 
    WHILE expression DO statement
    ;
// End Part 6.3

// Part 6.4: The for Statement
statement_for: 
    FOR identifier ASSIGN_OP expression (TO | DOWNTO) expression DO statement;
// End Part 6.4

// Part 6.5: The break Statement
statement_break:
    BREAK SEMI;
// End Part 6.5

// Part 6.6: The continue Statement
statement_continue:
    CONTINUE SEMI;
// End Part 6.6

// Part 6.7: The return Statement
statement_return:
    RETURN expression SEMI
    | RETURN SEMI;
// End Part 6.7

// Part 6.8: The compound Statement
statement_compound:
    BEGIN statement* END;
// End Part 6.8

// Part 6.9: The with Statement
statement_with:
    WITH variable_declaration_list COMMA DO statement;
// End Part 6.9

// Part 6.10: Call Statement
statement_call:
    IDENTIFIER LB expression_list RB
    | IDENTIFIER LB RB;
// End Part 6.10


/*  Section 7: Built-in Functions
***************************************
*/


/*  Section 8: Scope Rules
***************************************
*/


/*  Section 9: The main function
***************************************
*/


/*  Section 10: Change Log
***************************************
*/


ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;