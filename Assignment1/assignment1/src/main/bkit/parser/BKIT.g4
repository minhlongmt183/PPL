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

program  : VAR COLON IDENT SEMI EOF ;


// Lexer
IDENT
    : [a-z] [a-zA-Z0-9_]*
    ;

// Keywords
BODY
    : 'Body'
    ;

BREAK
    : 'Break'
    ;

CONTINUE
    : 'Continue'
    ;

DO
    : 'Do'
    ;

ELSE
    : 'Else'
    ;

ELSEIF
    : 'ElseIf'
    ;

ENDBODY
    : 'EndBody'
    ;

ENDIF
    : 'EndIf'
    ;

ENDFOR
    : 'EndFor'
    ;

ENDWHILE
    : 'EndWhile'
    ;

FOR
    : 'For'
    ;

FUNCTION
    : 'Function'
    ;

IF
    : 'If'
    ;

PARAMETER
    : 'Parameter'
    ;

RETURN
    : 'Return'
    ;

THEN
    : 'Then'
    ;

VAR
    : 'Var'
    ;

WHILE
    : 'While'
    ;

TRUE
    : 'True'
    ;

FALSE
    : 'False'
    ;

EndDO
    : 'EndDo'
    ;

// Operator
PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

STAR
    : '*'
    ;

SLASH
    : '/'
    ;

EQUAL
    : '='
    ;

NOT_EQUAL
    : '<>'
    ;

LT
    : '<'
    ;

LE
    : '<='
    ;

GE
    : '>='
    ;

GT
    : '>'
    ;

ASSIGN
    : ':='
    ;


// Separators
LCURLY
   : '{'
   ;

RCURLY
   : '}'
   ;

LR
    : '('
    ;

RR
    : ')'
    ;

LB
    : '['
    ;

RB
    : ']'
    ;

SEMI
    : ';'
    ;

DOT
    : '.'
    ;

COMMA
    : ','
    ;

COLON
    : ':'
    ;

// Literal
INT_LIT
    : DEC 
    | OCT 
    | HEX
    ;

DEC
    : '0' | [1-9] [0-9]*
    ;

OCT
    : '0' 'O | o' [1-7] [0-7]* 
    ;

HEX
    : '0' 'X | x' [1-9A-F] [0-9A-F]*
    ;

FLOAT_LIT
    : INT_PART (DEC_PART | EXP_PART | DEC_PART EXP_PART)
    ;

INT_PART
    : [0-9]+ 
    ;

DEC_PART
    : '.' [0-9]*
    ;

EXP_PART
    : 'E | e' '+ | -'? [0-9]+
    ;

BOOL_LIT
    : TRUE
    | FALSE
    ;

STRING_LIT
    : UNCLOSE_STRING '"'
    {self.text = self.text[1:-1]}
    ;
UNCLOSE_STRING
    : '"' ('\\' [btrnf\\'] | '\'"' | ~[\b\t\r\n\f\\'"])*
    ;
    
ARRAY_LIT
    : LCURLY ELEM_LIT RCURLY
    ;

ELEM_LIT
    : SUB_ARRAY (',' SUB_ARRAY)*
    | ELEM_VAL (',' ELEM_VAL)* 
    ;

SUB_ARRAY
    : LCURLY ELEM_VAL (',' ELEM_VAL)*
    ;

ELEM_VAL
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | BOOL_LIT
    ;

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


ERROR_CHAR: .;
ILLEGAL_ESCAPE: UNCLOSE_STRING '\\' ~[btnfr'\\];

UNTERMINATED_COMMENT: .;