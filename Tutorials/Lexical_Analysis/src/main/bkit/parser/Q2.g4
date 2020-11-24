grammar Q2;
options{
    language=Python3;
}

program:;

// Question 2
Identifier:     LOWER_LETTER (LOWER_LETTER | DIGIT)*;
fragment LOWER_LETTER:    [a-z];
fragment DIGIT:    [0-9];


