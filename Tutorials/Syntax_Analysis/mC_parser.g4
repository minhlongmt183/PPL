grammar mC_parser;

options{
    language=Python3;
}

program
    :   manydecl EOF
    ;

manydecl
    :   decl manydecl
    |   decl
    ;

decl
    :   var_decl
    |   func_decl
    ;

var_decl
    :   type CM id_list SM
    ;


type
    :   INT
    |   FLOAT
    ;


id_list
    :   ID CM id_list
    |   ID
    ;

func_decl
    :   type ID param_decl body
    ;


param_decl
    :   LP param_list? RP
    ;


param_list
    :   type id_list SM param_list
    |   type id_list
    ;


body
    :   LB var_decl_list? statement? RB
    ;

var_decl_list
    :   var_decl SM var_decl_list
    |   var_decl
    ;




statement
    :   assign_stmt SM
    |   call_stmt SM 
    |   ret_stmt SM
    ;

assign_stmt
    :   ID EQ exp
    ;

call_stmt
    :   ID LB param_list? RB
    ;

ret_stmt
    :   RETURN exp
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
    :   exp1 SUB exp2
    |   exp2
    ;
exp2
    :   exp3 (MUL | DIV) exp2
    |   exp3
exp3
    :   LB exp RB
    | operands
    ;

operands
    :   ID
    |   INTLIT
    |   FLOATLIT
    |   call_stmt
    |   exp
    ;

