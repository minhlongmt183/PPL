grammar Q3;
options{
    language=Python3;
}

program:;

// Question 3
// a)
REAL    :   INT_PART ( DEC_PART | EPX_PART | DEC_PART EPX_PART);
fragment    INT_PART:   '-'? [1-9] DIGIT* | '0';
fragment    DEC_PART:   '.' DIGIT+;
fragment    EPX_PART:   'e-' DIGIT+;
fragment    DIGIT:  [0-9];

// b)
STR     :   '\'' (DOUBLE_QUOTE | ~'\'')* '\'';
fragment    DOUBLE_QUOTE:   '\'\'';