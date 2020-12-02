/*
   **************************************
   * Student name: Nguyen Ho Minh Phuoc *
   * Student ID: 1612736                *
   **************************************
   lexer2018TNQuiz
*/

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: ; 

//  Question 1 ************************
//  IDENTIFIER: [a-z][a-z0-9]*;
//  ***********************************

//  Question 2 ************************
fragment LOWERCASE: [a-z];
fragment UPPERCASE: [A-Z];
fragment DIGIT: [0-9];

IDENTIFIER: LOWERCASE (LOWERCASE | DIGIT)*;
//  ***********************************



//  Question 3 ************************
fragment E: [eE];
fragment Real_type_1: DIGIT+('.'DIGIT+)?(E(ADD_OP | SUB_OP)DIGIT+)?;
fragment Real_type_2: '.'DIGIT+(E(ADD_OP | SUB_OP)DIGIT+)?;
REALLIT: Real_type_1 | Real_type_2;

fragment CHAR: ~'\'';
fragment D_SINGLE_QUOTES: \'\';
STRINGLIT: '\''(CHAR | D_SINGLE_QUOTES)*'\'';
//  ***********************************

ADD_OP: '+';
SUB_OP: '-';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;