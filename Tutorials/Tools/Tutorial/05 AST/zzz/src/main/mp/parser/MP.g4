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

program: many_declarations EOF;

many_declarations:
    many_declarations declaration
    | declaration
    ;

declaration:
    variable_declaration
    | function_declaration
    | procedure_declaration
    ;

// 2.1
variable_declaration:
    VAR list_declarations
    ;

list_declarations:
    list_declarations v_declaration
    | v_declaration
    ;

v_declaration:
    list_identifiers COLON types SEMI
    ;

list_identifiers:
    list_identifiers COMMA IDENTIFIER
    | IDENTIFIER
    ;

// 2.2
function_declaration:
    FUNCTION IDENTIFIER LB list_parameters RB COLON types SEMI variable_declaration? compound_statement
    ;

list_parameters:
    not_null_list_parameters
    |
    ;

not_null_list_parameters:
    not_null_list_parameters SEMI parameter_declaration
    | parameter_declaration
    ;
    
parameter_declaration:
    list_identifiers COLON types
    ;

// 2.3

procedure_declaration:
    PROCEDURE IDENTIFIER LB list_parameters RB SEMI variable_declaration? compound_statement
//    | main_procedure
    ;

// 3.1
fragment A: 
    [Aa]
    ;
    
fragment B: 
    [Bb]
    ;
    
fragment C: 
    [Cc]
    ;
    
fragment D: 
    [Dd]
    ;
    
fragment E: 
    [Ee]
    ;
    
fragment F: 
    [Ff]
    ;
    
fragment G: 
    [Gg]
    ;
    
fragment H: 
    [Hh]
    ;
    
fragment I: 
    [Ii]
    ;
    
fragment J: 
    [Jj]
    ;
    
fragment K: 
    [Kk]
    ;
    
fragment L: 
    [Ll]
    ;
    
fragment M: 
    [Mm]
    ;
    
fragment N: 
    [Nn]
    ;
    
fragment O: 
    [Oo]
    ;
    
fragment P: 
    [Pp]
    ;
    
fragment Q: 
    [Qq]
    ;
    
fragment R: 
    [Rr]
    ;
    
fragment S: 
    [Ss]
    ;
    
fragment T: 
    [Tt]
    ;
    
fragment U: 
    [Uu]
    ;
    
fragment V: 
    [Vv]
    ;
    
fragment W: 
    [Ww]
    ;
    
fragment X: 
    [Xx]
    ;
    
fragment Y: 
    [Yy]
    ;
    
fragment Z: 
    [Zz]
    ;
    
// 3.2
LINE_CMT: 
    '//'~[\n]* -> skip
    ;

BLOCK_CMT_1: 
    '{' .*? '}' -> skip
    ;

BLOCK_CMT_2: 
    '(*' .*? '*)' -> skip
    ;

// 3.3


// Keywords
//MAIN: M A I N;

//ANDTHEN: A N D  T H E N;
//ORELSE: O R  E L S E;

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



ARRAY: A R R A Y;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;

// Operators
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



ASSIGN: ':=';

// 3.4: Separators
LSB: 
    '['
    ;
RSB: 
    ']'
    ;
    
COLON: 
    ':'
    ;
    
LB: 
    '(' 
    ;
    
RB: 
    ')' 
    ;
    
SEMI: 
    ';'
    ;
    
DDOT: 
    '..'
    ;
    
COMMA: 
    ','
    ;

/*LP: 
    '{'
    ;
    
RP: 
    '}'
    ;
*/

// 3.5: Literals
literal:
    INTEGER_LITERAL
    | REAL_LITERAL
    | TRUE
    | FALSE
    | STRING_LITERAL
    ;

fragment DIGIT: 
    [0-9]
    ;
    
INTEGER_LITERAL:
    DIGIT+
    ;
    
fragment EXPONENT: 
    [eE] '-'? DIGIT+ 
    ;
    
REAL_LITERAL: 
    DIGIT+ ('.' DIGIT*)? EXPONENT?
    | '.' DIGIT+ EXPONENT?
    ;

/*    
BOOLEAN_LITERAL:
    TRUE | FALSE
    ;
*/

TRUE: T R U E;
FALSE: F A L S E;
    
fragment BSP: 
    '\\b'
    ;
    
fragment FF: 
    '\\f'
    ;
    
fragment CR: 
    '\\r'
    ;
    
fragment NEWLINE: 
    '\\n'
    ;
    
fragment TAB: 
    '\\t'
    ;
    
fragment SQUOTE: 
    '\\\''
    ;
    
fragment DQUOTE: 
    '\\"'
    ;
    
fragment BSL: 
    '\\''\\'
    ;

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
    
UNCLOSE_STRING: 
    '"' (~[\n\r\\'"] | LEGAL_ESCAPE)*
//    '"' (~[\n\r\b\f\t\\'"] | LEGAL_ESCAPE)*
{
    raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE:
    UNCLOSE_STRING ('\\' ~[nrbft'"] | '\'')
//    UNCLOSE_STRING [\b\f\t\\']
{
    raise IllegalEscape(self.text[1:])
};          

STRING_LITERAL: 
    UNCLOSE_STRING '"'
{
    self.text = self.text[1:-1]
};

// 4. Types and Values

types:
    primitive_type
    | compound_type
    ;

primitive_type:
    BOOLEAN
    | INTEGER
    | REAL
    | STRING
    ;

compound_type:
    array_type
    ;

array_type:
    ARRAY LSB SUB? INTEGER_LITERAL DDOT SUB? INTEGER_LITERAL RSB OF primitive_type
    ;

// 5. Expressions

operand:
    literal
    | IDENTIFIER
//    | arr_element
    | func_call
    ;

expression:
    expression AND THEN expression_1
    | expression OR ELSE expression_1
//    expression_1 AND THEN expression
//    | expression_1 OR ELSE expression
    | expression_1
//    | operand
    ;

expression_1:
    expression_2 EQUAL expression_2
    | expression_2 NOTEQUAL expression_2
    | expression_2 LESSTHAN expression_2
    | expression_2 GREATERTHAN expression_2
    | expression_2 LESSEQUAL expression_2
    | expression_2 GREATEREQUAL expression_2
    | expression_2
    ;

expression_2:
    expression_2 ADD expression_3
    | expression_2 SUB expression_3
    | expression_2 OR expression_3
    | expression_3
    ;

expression_3:
    expression_3 DIV_F expression_4
    | expression_3 MUL expression_4
    | expression_3 DIV expression_4
    | expression_3 MOD expression_4
    | expression_3 AND expression_4
    | expression_4
    ;

expression_4:
    SUB expression_4
    | NOT expression_4
    | expression_5
    ;

expression_5:
    expression_5 LSB expression RSB
    | expression_6
    ;
    
expression_6:
    LB expression RB
    | operand
    ;


// 5.3: Index Expression
arr_element:
    expression_5 LSB expression RSB
    ;

// 5.4: Invocation Expression
func_call:
    IDENTIFIER LB list_expression RB
    ;

list_expression:
    not_null_list_expression
    |
    ;
    
not_null_list_expression:
    not_null_list_expression COMMA expression
    | expression
    ;

// 6. Statements and Control Flow

statement:
    assignment_statement
    | if_statement
    | while_statement
    | for_statement
    | break_statement
    | continue_statement
    | return_statement
    | compound_statement
    | with_statement
    | call_statement
    ;

// 6.1 Assignment Statement
assignment_statement:
    (IDENTIFIER | arr_element) ASSIGN assignment_statement
    | (IDENTIFIER | arr_element) ASSIGN expression SEMI
    ;

list_var_idx_ass:
    list_var_idx_ass ASSIGN IDENTIFIER
    | list_var_idx_ass ASSIGN arr_element
    | IDENTIFIER
    | arr_element
    ;

// 6.2 If Statement

if_statement:
    IF expression THEN statement (ELSE statement)?
    ;

// 6.3 While Statement
while_statement:
    WHILE expression DO statement
    ;

// 6.4 For Statement
for_statement:
    FOR IDENTIFIER ASSIGN expression (TO | DOWNTO) expression DO statement
    ;

// 6.5 Break Statement
break_statement:
    BREAK SEMI
    ;

// 6.6 Continue Statement
continue_statement:
    CONTINUE SEMI
    ;

// 6.7 Return Statement
return_statement:
    RETURN expression? SEMI
    ;

// 6.8 Compound Statement
compound_statement:
    BEGIN list_statements END
    ;

list_statements:
    not_null_list_statements
    |
    ;

not_null_list_statements:
    not_null_list_statements statement
    | statement
    ;

// 6.9 With Statement
with_statement:
    WITH list_declarations DO statement
    ;

// 6.10 Call Statement
call_statement:
    func_call SEMI
    ;

// 9. The main function
/*main_procedure:
    PROCEDURE MAIN LB RB SEMI variable_declaration? compound_statement
    ;
*/

IDENTIFIER:
    [a-zA-Z_][a-zA-Z_0-9]*
    ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR:
    .
{
    raise ErrorToken(self.text)
}
;



//ERROR_CHAR: .;
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;

