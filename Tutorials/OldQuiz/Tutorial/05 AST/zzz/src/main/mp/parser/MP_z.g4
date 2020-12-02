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
    list_identifiers COLON mtype SEMI
    ;

list_identifiers:
    list_identifiers COMMA ID
    | ID
    ;
    
procedure_declaration: PROCEDURE ID LB RB SEMI body; 

function_declaration: FUNCTION ID LB RB COLON mtype SEMI body;

body: BEGIN stmt*? END  ;

stmt: funcall SEMI;

funcall: ID LB exp? RB ;

exp: INTLIT ;

mtype: INTTYPE;

INTLIT: [0-9]+ ;

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COLON: ':' ;

COMMA: ',' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

VAR: V A R;

PROCEDURE: P R O C E D U R E;

FUNCTION: F U N C T I O N;

BEGIN: B E G I N;

END: E N D;

INTTYPE: I N T E G E R;

ID: [a-zA-Z]+ ;

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

ERROR_CHAR: .;
