grammar Q4;
options{
    language=Python3;
}

program:;

// Cau a
A   : 'a'* ('bb') 'b'+;

// Cau b
B   : 'aa'* ('aa' | 'ab' | 'bb') 'bb'*;

// Cau c 
C   : ('a' 'aaa'*) 'b';