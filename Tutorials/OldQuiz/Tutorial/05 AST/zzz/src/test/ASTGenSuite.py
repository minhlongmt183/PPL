import unittest
from TestUtils import TestAST
from AST import *
     

class ASTGenSuite(unittest.TestCase):

    def test_var_declaration_1_simplest(self):        
        input = """vaR Xixinhdep :Boolean ;"""
        expect = str(Program([VarDecl(Id(r'Xixinhdep'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,301))


    def test_var_declaration_2_simplest(self):        
        input = """var a, b :integer;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_var_declaration_3_muti_decl(self):           
        input = """var a, b:integer; 
        c, d :bOOlean   ;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'd'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_declaration_4_muti_var_decl(self):           
        input = """var x, b:integer;
        var a, b:string;"""
        expect = str(Program([VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'a'),StringType()),VarDecl(Id(r'b'),StringType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_var_declaration_5_muti_var_decl(self):           
        input = """var a, b:integer;
        var a, b:integer;
            x, y :real  ;"""
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,305))

# Test Mp TYPE

    def test_type_1_primitype(self):           
        input = """var a, b:integer;
        var a, b:boolean;
            x, y :string ;
        var r, q :real;
              """
        expect = str(Program([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'a'),BoolType()),VarDecl(Id(r'b'),BoolType()),VarDecl(Id(r'x'),StringType()),VarDecl(Id(r'y'),StringType()),VarDecl(Id(r'r'),FloatType()),VarDecl(Id(r'q'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_type_2_nonprimitype(self):           
        input = """var a: array [0 .. 10] of rEal; 
        var b: array [-10 .. -10] of sTRing;
        var c: array [-10 .. 10] of bOOlean;
        var d: array [0 .. -10] of inteGER;
              """
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(0,10,FloatType())),VarDecl(Id(r'b'),ArrayType(-10,-10,StringType())),VarDecl(Id(r'c'),ArrayType(-10,10,BoolType())),VarDecl(Id(r'd'),ArrayType(0,-10,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_type_3(self):           
        input = """var a: array [0 .. 10] of rEal; 
        var b: array [-10 .. -10] of sTRing;
            c: bOOlean;
        var a: InteGER;
              """
        expect = str(Program([VarDecl(Id(r'a'),ArrayType(0,10,FloatType())),VarDecl(Id(r'b'),ArrayType(-10,-10,StringType())),VarDecl(Id(r'c'),BoolType()),VarDecl(Id(r'a'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_simple_program_8_blank_procedure(self):           
        input = """
        procedure  xxx();
        BEgin 
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xxx'),[],[],[],VoidType())]))    
        self.assertTrue(TestAST.test(input,expect,309))

    def test_simple_program_9_vardecls_before_proceduredecl(self):
        input = """
        var a : ReAL;
        procedure  xxx();
        BEgin 
        EnD
        """
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),FuncDecl(Id(r'xxx'),[],[],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_simple_program_10_vardecls_after_proceduredecl(self):
        input = """
        procedure  xxx();
        BEgin 
        EnD
        var a : ReAL;
        """
        expect = str(Program([FuncDecl(Id(r'xxx'),[],[],[],VoidType()),VarDecl(Id(r'a'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,311))
    
    def test_simple_program_10_vardecls_both_before_after_proceduredecl(self):
        input = """
        var x : array[-10 .. 5] of boolEaN;
        procedure  xxx();
        BEgin 
        EnD
        var a : ReAL;
        """
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-10,5,BoolType())),FuncDecl(Id(r'xxx'),[],[],[],VoidType()),VarDecl(Id(r'a'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))
    
    def test_complex_program_simple_procedure(self):
        input = """
        Procedure xixinh () ;
        var a, b :integER;
        BEgin
            Writeln("[1]. PLAY GAME");
            WRITELN("[2]. LOAD GAME");
            Readln(SEL);
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'Writeln'),[StringLiteral(r'[1]. PLAY GAME')]),CallStmt(Id(r'WRITELN'),[StringLiteral(r'[2]. LOAD GAME')]),CallStmt(Id(r'Readln'),[Id(r'SEL')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,313))
    
    def test_complex_program_simple_procedure_with_local_vardecl(self):
        input = """
        Procedure xixinh (e: array[0 .. 10] of StrInG) ;
        var a, b :integER;
        BEgin
            Readln(XiXInh);
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[VarDecl(Id(r'e'),ArrayType(0,10,StringType()))],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'Readln'),[Id(r'XiXInh')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,314))
    
    def test_complex_program_simple_procedure_with_local_vardecl_2(self):
        input = """
        Procedure xixinh (e: array[0 .. 10] of StrInG; b: boolean) ;
        var a, c :integER;
        BEgin
            Readln(XiXInh);
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[VarDecl(Id(r'e'),ArrayType(0,10,StringType())),VarDecl(Id(r'b'),BoolType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'c'),IntType())],[CallStmt(Id(r'Readln'),[Id(r'XiXInh')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,315))
  
    def test_complex_program_1_simple_function(self):
        input = """
        fUNcTion xinh (a, b:integer) : integer;
        var a, b :integER;
        BEgin
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xinh'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,316))
    
    def test_more_complex_program_2_many_stmts_inside_compound_stmt_procedure(self):        
        input = """
        Procedure xixinh () ;
        BEgin
            thatxinh(m);
            a[1] := 3;
        EnD
        """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[],[CallStmt(Id(r'thatxinh'),[Id(r'm')]),Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(3))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,317))
    
    def test_variable_declaration_in_procedure(self):
        input = """Procedure xixinh() ;
                  var a, b, c : integer ;
                    d: array [1 .. 5] of integer ;
                    e , f : real ;
                  BEgin
                    hihi();
                  EnD"""
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),ArrayType(1,5,IntType())),VarDecl(Id(r'e'),FloatType()),VarDecl(Id(r'f'),FloatType())],[CallStmt(Id(r'hihi'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,318))
    
    def test_function_declaration_1_many_decls_in_vardecls_of_(self):
        input = """FUNcTION xix(a, b: integer ; c: real): integer ;
                  var x,y: real ;
                        z ,h :reaL;
                  BEgin
                  EnD
                  """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType()),VarDecl(Id(r'z'),FloatType()),VarDecl(Id(r'h'),FloatType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test_function_declaration_2(self):
        input = """FUNcTION xix(a, b: integer ; c: real): integer ;
                  var x,y: real ;
                  BEgin
                  EnD                  
                  """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_simple_program_9_vardecls_before_functiondecl(self):
        input = """
        var a : ReAL;
        function  xxx():integer;
        BEgin 
            
        EnD
        """
        expect = str(Program([VarDecl(Id(r'a'),FloatType()),FuncDecl(Id(r'xxx'),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_simple_program_10_vardecls_after_functiondecl(self):
        input = """
        function xxx(): BOOLEan;
        BEgin 
        EnD
        var a : ReAL;
        """
        expect = str(Program([FuncDecl(Id(r'xxx'),[],[],[],BoolType()),VarDecl(Id(r'a'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,322))
     
    def test_Procedure_declaration_simple_ex(self):
        input = """Procedure xix(a, b: integer ; c: real) ;
                  var x,y: real ;
                  BEgin
                    hi();
                  EnD
                  """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[CallStmt(Id(r'hi'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_simple_program_10_vardecls_both_before_after_functiondecl(self):
        input = """
        var x : array[-10 .. 5] of boolEaN;
        function xxx():integER;
        BEgin 
        EnD
        var a : ReAL;
        """
        expect = str(Program([VarDecl(Id(r'x'),ArrayType(-10,5,BoolType())),FuncDecl(Id(r'xxx'),[],[],[],IntType()),VarDecl(Id(r'a'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_function_declaration_4(self):
        input = """function xix(a, b: integer ; c: real): integer ;
                  var x,y: real ;
                  BEgin
                  end
                 """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_assign_stmt_1_test_array_elem(self):
        input = """Procedure xix(a, b: integer ; c: boolean) ;
                  var x,y: real ;
                  BEgin
                    a := 1;
                    b := a[12] ;
                  EnD
                  vaR x: integer;
                  """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),BoolType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'a'),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType()),VarDecl(Id(r'x'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_assign_stmt_2_test_assignOP(self):
        input = """Procedure xix() ;                  
                  BEgin
                    a := "onggia";
                  EnD
                  """
        expect = str(Program([FuncDecl(Id(r'xix'),[],[],[Assign(Id(r'a'),StringLiteral(r'onggia'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,327))
    
    def test_assign_stmt_4_many_assign_succesful(self):
        input = """Procedure xix(c: real) ;
                   var x,y: real ;
                   BEgin
                    z := "dsfsd";
                    c := a[12] ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType()),VarDecl(Id(r'y'),FloatType())],[Assign(Id(r'z'),StringLiteral(r'dsfsd')),Assign(Id(r'c'),ArrayCell(Id(r'a'),IntLiteral(12)))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,328))
    
    def test_assign_stmt_5_complex_assign(self):
        input = """function xix(c: real): real ;
                   var x: integer ;
                   BEgin
                    a[1]  :=  f()[3] := a[3] := 1;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),IntType())],[Assign(ArrayCell(Id(r'a'),IntLiteral(3)),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id(r'f'),[]),IntLiteral(3)),ArrayCell(Id(r'a'),IntLiteral(3))),Assign(ArrayCell(Id(r'a'),IntLiteral(1)),ArrayCell(CallExpr(Id(r'f'),[]),IntLiteral(3)))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,329))
    
    def test_assign_stmt_7(self):
        input = """function xix(c: real): real ;
                   var x: integer ;
                   BEgin
                    a[m]  := a[n] :=  f(m)[3] := 1;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),IntType())],[Assign(ArrayCell(CallExpr(Id(r'f'),[Id(r'm')]),IntLiteral(3)),IntLiteral(1)),Assign(ArrayCell(Id(r'a'),Id(r'n')),ArrayCell(CallExpr(Id(r'f'),[Id(r'm')]),IntLiteral(3))),Assign(ArrayCell(Id(r'a'),Id(r'm')),ArrayCell(Id(r'a'),Id(r'n')))],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_if_stmt_1_full_function(self):
        input = """function xix(c: real): real ;
                   var x:real ;
                   BEgin
                    if (true) then a:= b;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BooleanLiteral(True),[Assign(Id(r'a'),Id(r'b'))],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,331))
    
    def test_if_stmt_2_test_operator_and_call_function(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    if  (aa and x) then a:=1 ;
                    else xix();
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'and',Id(r'aa'),Id(r'x')),[Assign(Id(r'a'),IntLiteral(1))],[CallStmt(Id(r'xix'),[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    def test_if_stmt_3_complex_operators(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    if(a>1) then a:=1 ;
                    else if (1<2)<>(2<3) then x:=1 ;
                    else xix(a+1,2);
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[If(BinaryOp(r'<>',BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),BinaryOp(r'<',IntLiteral(2),IntLiteral(3))),[Assign(Id(r'x'),IntLiteral(1))],[CallStmt(Id(r'xix'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,333))
    
    def test_if_stmt_4_call_function_operators(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    if(a>1) then 
                        BEgin 
                            a:=1 ;
                            if (1<2) then 
                                BEgin
                                    x:=1 ; 
                                    hiih();
                                EnD
                            else xix(a+1,2);
                        EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),[Assign(Id(r'x'),IntLiteral(1)),CallStmt(Id(r'hiih'),[])],[CallStmt(Id(r'xix'),[BinaryOp(r'+',Id(r'a'),IntLiteral(1)),IntLiteral(2)])])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,334))
      
    def test_if_stmt_7_nest_if(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    if(a>1) then a:=1 ;
                    if (1<2) then BEgin x:=1 ; EnD
                    else xix(xx);
                    return;
                   EnD"""
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1))],[]),If(BinaryOp(r'<',IntLiteral(1),IntLiteral(2)),[Assign(Id(r'x'),IntLiteral(1))],[CallStmt(Id(r'xix'),[Id(r'xx')])]),Return(None)],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,335))
    
    def test_if_stmt_8_many_stmts_in_if_scope(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    if(a>1) then BEgin
                        a:=1 ;
                        if(1=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    EnD
                    return sfdsf;
                    EnD
                    """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r'a'),IntLiteral(1)),If(BinaryOp(r'=',IntLiteral(1),IntLiteral(1)),[Assign(Id(r'a'),ArrayCell(Id(r'b'),IntLiteral(1)))],[Assign(ArrayCell(Id(r'a'),IntLiteral(1)),IntLiteral(1)),Assign(Id(r'b'),ArrayCell(Id(r'a'),IntLiteral(1)))])],[]),Return(Id(r'sfdsf'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,336))
    
    def test_while_stmt_1_simple(self):
        input = """Procedure xix(c: string) ;
                   var x:real ;
                   BEgin
                    whILe(a=1) do BEgin EnD
                   EnD"""
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),StringType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,337))
    
    def test_while_stmt_2_easy_function_with_while(self):
        input = """function xix(c: boolean) : array [-10 .. 10] of integer;
                   var x:real ;
                   BEgin
                    whILe(a<>1) 
                    do                         
                        xix();                    
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),BoolType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[CallStmt(Id(r'xix'),[])])],ArrayType(-10,10,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,338))
    
    def test_while_stmt_3_nest_while(self):
        input = """Procedure xix(c: real) ;
                   var x:real ;
                   BEgin
                    whILe(a<>1) do BEgin
                        while(1) do x:=1;
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'x'),FloatType())],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[While(IntLiteral(1),[Assign(Id(r'x'),IntLiteral(1))])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,339))
    
    def test_while_stmt_4_nest_while_and_if(self):
        input = """Procedure xix(c: real) ;
                   BEgin
                    whILe(a<>1) do BEgin
                        while(1) do x:=1;
                        if(a=1) then BEgin EnD
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[While(BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),[While(IntLiteral(1),[Assign(Id(r'x'),IntLiteral(1))]),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test_with_stmt_1_simple(self):
        input = """Procedure xix(c: real) ;
                   BEgin
                    with a : integer ;
                         do
                    d := c [a] + b ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'a'),IntType())],[Assign(Id(r'd'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b')))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_with_stmt_3_many_stmts_inside_with_scope(self):
        input = """Procedure xix(c: real) ;
                    var l: real;
                   BEgin
                    with a , b : integer ; c : array [1 .. 2] of real ; 
                    do BEgin
                        daa := c [a] + b ;
                         xix();xix1(a,b,c);
                        with a , b : integer ; do BEgin
                          xix2(a,b,"anc");
                    EnD
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[VarDecl(Id(r'l'),FloatType())],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[Assign(Id(r'daa'),BinaryOp(r'+',ArrayCell(Id(r'c'),Id(r'a')),Id(r'b'))),CallStmt(Id(r'xix'),[]),CallStmt(Id(r'xix1'),[Id(r'a'),Id(r'b'),Id(r'c')]),With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'xix2'),[Id(r'a'),Id(r'b'),StringLiteral(r'anc')])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_with_stmt_4_nest(self):
        input = """function xix(c: real): striNG;
                   BEgin
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; do
                        xix2(a,b,"anc");
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[With([VarDecl(Id(r'c'),IntType()),VarDecl(Id(r'd'),IntType()),VarDecl(Id(r'c'),ArrayType(1,2,FloatType()))],[With([VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[CallStmt(Id(r'xix2'),[Id(r'a'),Id(r'b'),StringLiteral(r'anc')])])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test_for_stmt_1_simple_for(self):
        input = """function xix(c: real): real;
                   BEgin
                    FOR i:=1 to m+ n do 
                        s := s + 1;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),Id(r'n')),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1)))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    def test_for_stmt_2_many_stmts_in_for_scope(self):
        input = """function xix(c: real): striNG;
                   BEgin
                    FOR i:=1 to m+ n do BEgin
                        s := s + 1;
                        if(a=1) then s:=s-1;
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),Id(r'n')),True,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1))),If(BinaryOp(r'=',Id(r'a'),IntLiteral(1)),[Assign(Id(r's'),BinaryOp(r'-',Id(r's'),IntLiteral(1)))],[])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,345))
    
    def test_for_stmt_3_test_to_and_downto(self):
        input = """function xix(c: real): striNG;
                   BEgin
                    FOR i:=1 to n do BEgin
                        for j:=m+ n doWnTO 100 do BEgin
                            s := s + 1;
                            if (a>1) then s:=s-1;
                        EnD
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),Id(r'n'),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'm'),Id(r'n')),IntLiteral(100),False,[Assign(Id(r's'),BinaryOp(r'+',Id(r's'),IntLiteral(1))),If(BinaryOp(r'>',Id(r'a'),IntLiteral(1)),[Assign(Id(r's'),BinaryOp(r'-',Id(r's'),IntLiteral(1)))],[])])])],StringType())]))
        self.assertTrue(TestAST.test(input,expect,346))
    
    def test_for_stmt_4_nest_while_and_for(self):
        input = """Procedure xix(c: real);
                   BEgin
                    FOR i:=1 to m+ n do BEgin
                        while i>1 do
                            FOR i:=m+ n doWnTO 10 do
                                while j>1 do x:=xix(10);
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),Id(r'n')),True,[While(BinaryOp(r'>',Id(r'i'),IntLiteral(1)),[For(Id(r'i'),BinaryOp(r'+',Id(r'm'),Id(r'n')),IntLiteral(10),False,[While(BinaryOp(r'>',Id(r'j'),IntLiteral(1)),[Assign(Id(r'x'),CallExpr(Id(r'xix'),[IntLiteral(10)]))])])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,347))
    
    def test_break_stmt_just_break(self):
        input = """Procedure xix(c: real);
                   BEgin
                    FOR i:=1 to m + n do BEgin
                        brEaK;
                    EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[For(Id(r'i'),IntLiteral(1),BinaryOp(r'+',Id(r'm'),Id(r'n')),True,[Break()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_break_stmt_2_break(self):
        input = """Procedure xix(c: real);
                   begin 
                   break;
                  end
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[Break()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,349))
    
    def test_continue_stmt_continue_in_while_scope(self):
        input = """Procedure xix(c: real);
                   BEgin
                    while (1) do coNtInUe ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Continue()])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,350))
    
    def test_continue_stmt_2_just_continue(self):
        input = """Procedure xix(c: real);
                   BEgin
                    coNtInUe ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[Continue()],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,351))
    
    def test_return_stmt_1_return_in_while(self):
        input = """Procedure xix(c: real);
                   BEgin
                    while (1) do reTuRn ;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Return(None)])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,352))
    
    def test_return_stmt_2_return_function_cal(self):
        input = """function xix(c: real): integer;
                   BEgin
                    while 1 do reTuRn xix(0);
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[While(IntLiteral(1),[Return(CallExpr(Id(r'xix'),[IntLiteral(0)]))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,353))
    
    def test_return_stmt_4_check_many_returns(self):
        input = """function xix(c: real): integer;
                   BEgin
                    reTuRn;
                    reTuRn;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[Return(None),Return(None)],IntType())]))
        self.assertTrue(TestAST.test(input,expect,354))
   
    def test_compound_stmt_nest_compound(self):
        input = """function xix(c: real): integer;
                   BEgin
                     BEgin EnD
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,355))
    
    def test_call_stmt_1_many_functinons_cals(self):
        input = """function xix(c: real): integer;
                   BEgin
                    xix (3,a+1);
                    xix1();
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'xix'),[IntLiteral(3),BinaryOp(r'+',Id(r'a'),IntLiteral(1))]),CallStmt(Id(r'xix1'),[])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,356))
    
    def test_call_stmt_2_funccal_and_return(self):
        input = """function xix(c: real): integer;
                   BEgin
                    xix(1,a<>1,a[1]);
                    return 1;
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'xix'),[IntLiteral(1),BinaryOp(r'<>',Id(r'a'),IntLiteral(1)),ArrayCell(Id(r'a'),IntLiteral(1))]),Return(IntLiteral(1))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,357))
    
    def test_call_stmt_3_nest_function_cals(self):
        input = """function xix(c: real): integer;
                   BEgin
                    xix(xix(1,2)[m+ n]);
                    return xix2();
                   EnD"""
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'xix'),[ArrayCell(CallExpr(Id(r'xix'),[IntLiteral(1),IntLiteral(2)]),BinaryOp(r'+',Id(r'm'),Id(r'n')))]),Return(CallExpr(Id(r'xix2'),[]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,358))
    
    def test_call_stmt_4_really_nest_fucntion_cals(self):
        input = """function xix(c: real): integer;
                   BEgin
                    xix(3,xix(xix1(xix(2,a+1))));
                    return func(a(1,2));
                   EnD"""
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'xix'),[IntLiteral(3),CallExpr(Id(r'xix'),[CallExpr(Id(r'xix1'),[CallExpr(Id(r'xix'),[IntLiteral(2),BinaryOp(r'+',Id(r'a'),IntLiteral(1))])])])]),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,359))
    
    def test_call_stmt_5_(self):
        input = """function xix(c: real): integer;
                   BEgin
                    test(brown);
                	ClrScr(); 
                    return func(a(1,2));
                   EnD
                   """
        expect = str(Program([FuncDecl(Id(r'xix'),[VarDecl(Id(r'c'),FloatType())],[],[CallStmt(Id(r'test'),[Id(r'brown')]),CallStmt(Id(r'ClrScr'),[]),Return(CallExpr(Id(r'func'),[CallExpr(Id(r'a'),[IntLiteral(1),IntLiteral(2)])]))],IntType())]))
        self.assertTrue(TestAST.test(input,expect,360))
    
    def test_string_1(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey Max! Xi Xinh Dep ";
	Delete(S, 4, 4); { "Hey! Xi Xinh Dep " }
	Write(S);
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey Max! Xi Xinh Dep ')),CallStmt(Id(r'Delete'),[Id(r'S'),IntLiteral(4),IntLiteral(4)]),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,361))
        

    def test_string_2_just_wite(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	a := b:=c:=6 and 4;
    writre (a);
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'c'),BinaryOp(r'and',IntLiteral(6),IntLiteral(4))),Assign(Id(r'b'),Id(r'c')),Assign(Id(r'a'),Id(r'b')),CallStmt(Id(r'writre'),[Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,362))
        

    def test_string_3_concat_string_func(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "xi!";
	S2 := " Xi Xinh Dep ";
	Write(Concat(S1, S2)); { "Hey! Xi Xinh Dep " }
End
        """
        expect = str(Program([VarDecl(Id(r'S1'),StringType()),VarDecl(Id(r'S2'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S1'),StringLiteral(r'xi!')),Assign(Id(r'S2'),StringLiteral(r' Xi Xinh Dep ')),CallStmt(Id(r'Write'),[CallExpr(Id(r'Concat'),[Id(r'S1'),Id(r'S2')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,363))
        

    def test_string_4_write_expr(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " Xi Xinh Dep ";
	Write(S1 + S2); { "Hey! Xi Xinh Dep " }
End
        """
        expect = str(Program([VarDecl(Id(r'S1'),StringType()),VarDecl(Id(r'S2'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S1'),StringLiteral(r'Hey!')),Assign(Id(r'S2'),StringLiteral(r' Xi Xinh Dep ')),CallStmt(Id(r'Write'),[BinaryOp(r'+',Id(r'S1'),Id(r'S2'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,364))
        

    def test_string_5(self):
        input = """
Var 
   S : String;
   i : Integer;

Procedure main();
Begin
	S := "Hey! Xi Xinh Dep ";
	For i := 1 to length(S) do
		S[i] := UpCase(S[i]);
	Write(S); { "HEY! Xi Xinh Dep " }
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey! Xi Xinh Dep ')),For(Id(r'i'),IntLiteral(1),CallExpr(Id(r'length'),[Id(r'S')]),True,[Assign(ArrayCell(Id(r'S'),Id(r'i')),CallExpr(Id(r'UpCase'),[ArrayCell(Id(r'S'),Id(r'i'))]))]),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,365))
        

    def test_string__4_func(self):
        input = """
Var 
   S : String;

Procedure main();
Begin
	S := "Hey! Xi Xinh Dep ";
	Write(UpCase(S)); { "HEY! Xi Xinh Dep " }
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'Hey! Xi Xinh Dep ')),CallStmt(Id(r'Write'),[CallExpr(Id(r'UpCase'),[Id(r'S')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,366))
        

    def test_string__5_assign(self):
        input = """
Var 
	S : String;
	i : Real;

Procedure main();
Begin
	i := -0.563; 
	Str(i, S);
	Write(S); 
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),VarDecl(Id(r'i'),FloatType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'i'),UnaryOp(r'-',FloatLiteral(0.563))),CallStmt(Id(r'Str'),[Id(r'i'),Id(r'S')]),CallStmt(Id(r'Write'),[Id(r'S')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,367))
        

    def test_string__6_if_assign(self):
        input = """
Var 
	S     : String;
	error : Integer;
	R     : Real;

Procedure main();
Begin
	S := "-0.563"; 
	Val(S, R, error);
	If error > 0 Then
  	Write("Error in conversion.");
	Else
		Write(R); 
End
        """
        expect = str(Program([VarDecl(Id(r'S'),StringType()),VarDecl(Id(r'error'),IntType()),VarDecl(Id(r'R'),FloatType()),FuncDecl(Id(r'main'),[],[],[Assign(Id(r'S'),StringLiteral(r'-0.563')),CallStmt(Id(r'Val'),[Id(r'S'),Id(r'R'),Id(r'error')]),If(BinaryOp(r'>',Id(r'error'),IntLiteral(0)),[CallStmt(Id(r'Write'),[StringLiteral(r'Error in conversion.')])],[CallStmt(Id(r'Write'),[Id(r'R')])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,368))
        

    def test_complex__7_swap(self):
        input = """
Procedure BubbleSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, temp : Integer;

Begin
	For i := size-1 DownTo 1 do
		For j := 2 to i do
			If (numbers[j-1] > numbers[j]) Then
			Begin
				temp := numbers[j-1];
				numbers[j-1] := numbers[j];
				numbers[j] := temp;
			End

End
        """
        expect = str(Program([FuncDecl(Id(r'BubbleSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'temp'),IntType())],[For(Id(r'i'),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),IntLiteral(1),False,[For(Id(r'j'),IntLiteral(2),Id(r'i'),True,[If(BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),ArrayCell(Id(r'numbers'),Id(r'j'))),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'temp'))],[])])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,369))
        

    def test_complex__8_while(self):
        input = """
Procedure InsertionSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, index : Integer;


Begin
	For i := 2 to size-1 do
	Begin
		index := numbers[i];
		j := i;
		While ((j > 1) AND (numbers[j-1] > index)) do
		Begin
			numbers[j] := numbers[j-1];
			j := j - 1;
		End
		numbers[j] := index;
	End
End
        """
        expect = str(Program([FuncDecl(Id(r'InsertionSort'),[VarDecl(Id(r'numbers'),ArrayType(1,100,IntType())),VarDecl(Id(r'size'),IntType())],[VarDecl(Id(r'i'),IntType()),VarDecl(Id(r'j'),IntType()),VarDecl(Id(r'index'),IntType())],[For(Id(r'i'),IntLiteral(2),BinaryOp(r'-',Id(r'size'),IntLiteral(1)),True,[Assign(Id(r'index'),ArrayCell(Id(r'numbers'),Id(r'i'))),Assign(Id(r'j'),Id(r'i')),While(BinaryOp(r'AND',BinaryOp(r'>',Id(r'j'),IntLiteral(1)),BinaryOp(r'>',ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1))),Id(r'index'))),[Assign(ArrayCell(Id(r'numbers'),Id(r'j')),ArrayCell(Id(r'numbers'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))),Assign(Id(r'j'),BinaryOp(r'-',Id(r'j'),IntLiteral(1)))]),Assign(ArrayCell(Id(r'numbers'),Id(r'j')),Id(r'index'))])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,370))
    

    def test_bool_1_with_if(self):
        input = """
Var quit : Boolean;
    a    : String;
Procedure main();
Begin
	While NOT (quit = True) Do
    Begin
		Writeln("Type \\\"\\\"exit\\\"\\\" to quit:");
		Readln(a);
		If a = "exit" Then 
			quit := True;
    End
End
        """
        expect = str(Program([VarDecl(Id(r'quit'),BoolType()),VarDecl(Id(r'a'),StringType()),FuncDecl(Id(r'main'),[],[],[While(UnaryOp(r'NOT',BinaryOp(r'=',Id(r'quit'),BooleanLiteral(True))),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Type \"\"exit\"\" to quit:')]),CallStmt(Id(r'Readln'),[Id(r'a')]),If(BinaryOp(r'=',Id(r'a'),StringLiteral(r'exit')),[Assign(Id(r'quit'),BooleanLiteral(True))],[])])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,371))
        

    def test_for_2_many_decls(self):
        input = """
Procedure DrawLine(); 
{This procedure helps me to avoid the rewriting the for loops}
Var Counter : Integer;
Begin
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End
End

Procedure Main();
Begin
	
	Readkey();
End
        """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,372))
        

    def test_for_with_1_cpstmt(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
{ the declaration of the variables in brackets are called parameters }
Var Counter : Integer; { this is called a local variable }
Begin
	GotoXy(X,Y); {here I use the arguments of X and Y}
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196));
	End
End

Procedure main();
Begin
	
	Readkey();
End
        """
        expect = str(Program([FuncDecl(Id(r'DrawLine'),[VarDecl(Id(r'X'),IntType()),VarDecl(Id(r'Y'),IntType())],[VarDecl(Id(r'Counter'),IntType())],[CallStmt(Id(r'GotoXy'),[Id(r'X'),Id(r'Y')]),CallStmt(Id(r'textcolor'),[Id(r'green')]),For(Id(r'Counter'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id(r'Write'),[CallExpr(Id(r'chr'),[IntLiteral(196)])])])],VoidType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Readkey'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,373))
        

    def test_procedures_with_var(self):
        input = """
Procedure Square(Index : Integer; Result : Integer);
Begin
	Result := Index * Index;
End

Var
	Res : Integer;

Procedure Main();
Begin
	Writeln("The square of 5 is: ");
	Square(5, Res);
	Writeln(Res);
End
        """
        expect = str(Program([FuncDecl(Id(r'Square'),[VarDecl(Id(r'Index'),IntType()),VarDecl(Id(r'Result'),IntType())],[],[Assign(Id(r'Result'),BinaryOp(r'*',Id(r'Index'),Id(r'Index')))],VoidType()),VarDecl(Id(r'Res'),IntType()),FuncDecl(Id(r'Main'),[],[],[CallStmt(Id(r'Writeln'),[StringLiteral(r'The square of 5 is: ')]),CallStmt(Id(r'Square'),[IntLiteral(5),Id(r'Res')]),CallStmt(Id(r'Writeln'),[Id(r'Res')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,374))
        


    def test_string_real_string_ever(self):
        input = """
Var
	FName, Txt : String;
	UserFile   : String; 

Procedure Main();
Begin
	FName := "Textfile";
	Assign(UserFile, "C:\\\\" + FName + ".txt"); {assign a text file}
	Rewrite(UserFile); {open the file "fname" for writing}
	Writeln(UserFile, "PASCAL PROGRAMMING");
	Writeln(UserFile, "if you did not understand something,");
	Writeln(UserFile, "please send me an email to:");
	Writeln(UserFile, "victorsaliba@hotmail.com");
	Writeln("Write some text to the file:");
	Readln(Txt);
	Writeln(UserFile, "");
	Writeln(UserFile, "The user entered this text:");
	Writeln(UserFile, Txt);
	Close(UserFile);
End
        """
        expect = str(Program([VarDecl(Id(r'FName'),StringType()),VarDecl(Id(r'Txt'),StringType()),VarDecl(Id(r'UserFile'),StringType()),FuncDecl(Id(r'Main'),[],[],[Assign(Id(r'FName'),StringLiteral(r'Textfile')),CallStmt(Id(r'Assign'),[Id(r'UserFile'),BinaryOp(r'+',BinaryOp(r'+',StringLiteral(r'C:\\'),Id(r'FName')),StringLiteral(r'.txt'))]),CallStmt(Id(r'Rewrite'),[Id(r'UserFile')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'PASCAL PROGRAMMING')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'if you did not understand something,')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'please send me an email to:')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'victorsaliba@hotmail.com')]),CallStmt(Id(r'Writeln'),[StringLiteral(r'Write some text to the file:')]),CallStmt(Id(r'Readln'),[Id(r'Txt')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),StringLiteral(r'The user entered this text:')]),CallStmt(Id(r'Writeln'),[Id(r'UserFile'),Id(r'Txt')]),CallStmt(Id(r'Close'),[Id(r'UserFile')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,375))
        

    def test_string_and_cmt(self):
        input = """
Var
	UFile : String;

Procedure main();
Begin
	Assign(UFile); {, "C:\\\\ADDTEXT.TXT");}
	ReWrite(UFile); 
	Writeln(UFile, "How many sentences " + "are present in this file?");
	Close(UFile);
End
        """
        expect = str(Program([VarDecl(Id(r'UFile'),StringType()),FuncDecl(Id(r'main'),[],[],[CallStmt(Id(r'Assign'),[Id(r'UFile')]),CallStmt(Id(r'ReWrite'),[Id(r'UFile')]),CallStmt(Id(r'Writeln'),[Id(r'UFile'),BinaryOp(r'+',StringLiteral(r'How many sentences '),StringLiteral(r'are present in this file?'))]),CallStmt(Id(r'Close'),[Id(r'UFile')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,376))
             
    def test_multi_1_nest_scope(self):
        input = """
                Procedure test1() ;
                BEgin
	               if a=b then
	               BEgin
		                 b := c ;
		                 if(e <> f) then xix(a,c) ;
	               EnD
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'test1'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[Assign(Id(r'b'),Id(r'c')),If(BinaryOp(r'<>',Id(r'e'),Id(r'f')),[CallStmt(Id(r'xix'),[Id(r'a'),Id(r'c')])],[])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,377))
    
    def test_multi_2_full_if_stmt(self):
        input = """
                Procedure test2() ;
                BEgin
	                if a=b then if faLSe then while (true) do
                     BEgin
                     EnD
                    else c := 1;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'test2'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BooleanLiteral(False),[While(BooleanLiteral(True),[])],[Assign(Id(r'c'),IntLiteral(1))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_multi_3_many_decls_var_and_function_and_proceudre(self):
        input = """
                var i: integer ;                
                Procedure xixinh() ;
                var
	               xixinh: integer ;
                BEgin
	               xixinh := f() ;
	               putIntLn(xixinh);
	               with
                    
            		    f: integer;
	               do BEgin
		                xixinh := 100;
		               
	               EnD
	               xxx (xixinh);
                EnD
                var g: real ;
                function xxx(): integer ;
                BEgin
	               return;
                EnD
                """
        expect = str(Program([VarDecl(Id(r'i'),IntType()),FuncDecl(Id(r'xixinh'),[],[VarDecl(Id(r'xixinh'),IntType())],[Assign(Id(r'xixinh'),CallExpr(Id(r'f'),[])),CallStmt(Id(r'putIntLn'),[Id(r'xixinh')]),With([VarDecl(Id(r'f'),IntType())],[Assign(Id(r'xixinh'),IntLiteral(100))]),CallStmt(Id(r'xxx'),[Id(r'xixinh')])],VoidType()),VarDecl(Id(r'g'),FloatType()),FuncDecl(Id(r'xxx'),[],[],[Return(None)],IntType())]))
        self.assertTrue(TestAST.test(input,expect,379))
    
    def test_multi_4_simplier(self):
        input = """
                Procedure Hello(a, b:integer);
                BEgin
                    writeln("Hello, world!");
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'Hello'),[VarDecl(Id(r'a'),IntType()),VarDecl(Id(r'b'),IntType())],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Hello, world!')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,380))
    
    def test_multi_5_concaheo(self):
        input = """
                Var
                    xi1, xi2, Sum : Integer;
                Procedure concaheo(a, c:Real);
                BEgin                   
                    Sum := xi1 + xi2; {phep cong}
                    Write(Sum);
                    Readln();
                EnD
        """
        expect = str(Program([VarDecl(Id(r'xi1'),IntType()),VarDecl(Id(r'xi2'),IntType()),VarDecl(Id(r'Sum'),IntType()),FuncDecl(Id(r'concaheo'),[VarDecl(Id(r'a'),FloatType()),VarDecl(Id(r'c'),FloatType())],[],[Assign(Id(r'Sum'),BinaryOp(r'+',Id(r'xi1'),Id(r'xi2'))),CallStmt(Id(r'Write'),[Id(r'Sum')]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,381))
    
    def test_multi_6_full_format(self):
        input = """
                Var name: striNG;
                Procedure xixinh();
                BEgin
	               write("Nhap :");
	               readln(name);
	               writeln("Ten day du cua ban la : ",name);
	               readln();
                EnD
                """
        expect = str(Program([VarDecl(Id(r'name'),StringType()),FuncDecl(Id(r'xixinh'),[],[],[CallStmt(Id(r'write'),[StringLiteral(r'Nhap :')]),CallStmt(Id(r'readln'),[Id(r'name')]),CallStmt(Id(r'writeln'),[StringLiteral(r'Ten day du cua ban la : '),Id(r'name')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,382))
    
    def test_multi_7(self):
        input = """
                Var PD, Dname, Cmodel : striNG;
                Procedure xixinh();
                BEgin
                	ClrScr(); 
                	GotoXy(28,3);
                	Readln();
                EnD
        """
        expect = str(Program([VarDecl(Id(r'PD'),StringType()),VarDecl(Id(r'Dname'),StringType()),VarDecl(Id(r'Cmodel'),StringType()),FuncDecl(Id(r'xixinh'),[],[],[CallStmt(Id(r'ClrScr'),[]),CallStmt(Id(r'GotoXy'),[IntLiteral(28),IntLiteral(3)]),CallStmt(Id(r'Readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,383))

        
    
    def test_multi_8(self):
        input = """
                Procedure xixinh() ;
                BEgin
                 a[b[c]] := d;
                 
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[],[Assign(ArrayCell(Id(r'a'),ArrayCell(Id(r'b'),Id(r'c'))),Id(r'd'))],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,384))
    
    def test_multi_9(self):
        input = """
                Procedure xixinh() ;
                BEgin
                 if a=b then if c = d then e := f;
                 else i := 1;
                 
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[],[If(BinaryOp(r'=',Id(r'a'),Id(r'b')),[If(BinaryOp(r'=',Id(r'c'),Id(r'd')),[Assign(Id(r'e'),Id(r'f'))],[Assign(Id(r'i'),IntLiteral(1))])],[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,385))
    
    def test_multi_10_nest_for_and_if_and_assign(self):
        input = """
                Procedure xixinh() ;
                var a: array[-100 .. 100] of integer;
                 
                BEgin
                    for i := 0 to n - 2 do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then BEgin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            EnD
                    print(a);
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xixinh'),[],[VarDecl(Id(r'a'),ArrayType(-100,100,IntType()))],[For(Id(r'i'),IntLiteral(0),BinaryOp(r'-',Id(r'n'),IntLiteral(2)),True,[For(Id(r'j'),BinaryOp(r'+',Id(r'i'),IntLiteral(1)),BinaryOp(r'-',Id(r'n'),IntLiteral(1)),True,[If(BinaryOp(r'>',ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),[Assign(Id(r'temp'),ArrayCell(Id(r'a'),Id(r'i'))),Assign(ArrayCell(Id(r'a'),Id(r'i')),ArrayCell(Id(r'a'),Id(r'j'))),Assign(ArrayCell(Id(r'a'),Id(r'j')),Id(r'temp'))],[])])]),CallStmt(Id(r'print'),[Id(r'a')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,386))
    def test_multi_12_test_array_many_decls_in_scope(self):
        input = """
                Procedure haha(A : array[0 .. 10] of integer);
                begin
                    writeln("Hello");
                    writeln("World");
                    readln();
                end
                """
        expect = str(Program([FuncDecl(Id(r'haha'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType()))],[],[CallStmt(Id(r'writeln'),[StringLiteral(r'Hello')]),CallStmt(Id(r'writeln'),[StringLiteral(r'World')]),CallStmt(Id(r'readln'),[])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,387))
    
    def test_multi_13_normal(self):
        input = """
                Function xxx(A: integer ; N:Integer):boolean;
                Var S,i :Integer;
                BEgin
                	S:=0;                	
                	return S;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xxx'),[VarDecl(Id(r'A'),IntType()),VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'S'),IntType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'S'),IntLiteral(0)),Return(Id(r'S'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_multi_14_for_and_if_and_return(self):
        input = """
                Function hihi (N: real) :Integer;
                Var i:Integer;
                BEgin
                 For i:=2 to N-1 do
                  If(truE) then
                    return 0;
                  Else
                    return 1;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'hihi'),[VarDecl(Id(r'N'),FloatType())],[VarDecl(Id(r'i'),IntType())],[For(Id(r'i'),IntLiteral(2),BinaryOp(r'-',Id(r'N'),IntLiteral(1)),True,[If(BooleanLiteral(True),[Return(IntLiteral(0))],[Return(IntLiteral(1))])])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,389))
    
    def test_multi_15_just_var_decl(self):
        input = """
                var i: boolean;
                """
        expect = str(Program([VarDecl(Id(r'i'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,390))
    
    def test_multi_16_just_cmt_in_scope(self):
        input = """
                Procedure ThayTheTatCa (A:array[0 .. 10] of integer;N, x,y:Integer);
                Var i:Integer;
                BEgin
                 //chi viet cmt thoi dc ko nhi
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'ThayTheTatCa'),[VarDecl(Id(r'A'),ArrayType(0,10,IntType())),VarDecl(Id(r'N'),IntType()),VarDecl(Id(r'x'),IntType()),VarDecl(Id(r'y'),IntType())],[VarDecl(Id(r'i'),IntType())],[],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,391))
    
    def test_multi_17_complex_operator(self):
        input = """
                Function xinh () : Boolean;
                begin                
                If d<0 then
                Writeln("Phuong trinh vo nghiem"); Else
                Begin
                x1:= (-b+sqrt(d))/(2*a);
                x2:= (-b-sqrt(d))/(2*a);
                Write("Phuong trinh co hai nghiem: ");
                Writeln(" x1=", x2);
                End
                end
                """
        expect = str(Program([FuncDecl(Id(r'xinh'),[],[],[If(BinaryOp(r'<',Id(r'd'),IntLiteral(0)),[CallStmt(Id(r'Writeln'),[StringLiteral(r'Phuong trinh vo nghiem')])],[Assign(Id(r'x1'),BinaryOp(r'/',BinaryOp(r'+',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),Assign(Id(r'x2'),BinaryOp(r'/',BinaryOp(r'-',UnaryOp(r'-',Id(r'b')),CallExpr(Id(r'sqrt'),[Id(r'd')])),BinaryOp(r'*',IntLiteral(2),Id(r'a')))),CallStmt(Id(r'Write'),[StringLiteral(r'Phuong trinh co hai nghiem: ')]),CallStmt(Id(r'Writeln'),[StringLiteral(r' x1='),Id(r'x2')])])],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,392))
    
    def test_multi_18_complex_operator_and_if_and_for(self):
        input = """
                Function xxx (): Boolean;
                Var Flag:Boolean;
                    i :Integer;
                BEgin
                 Flag:=True;
                 For  i :=1 to N do
                 If(A[i] <> A[N-i  +1]) Then
                 Flag :=False;     
                 return flag;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xxx'),[],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Assign(Id(r'Flag'),BooleanLiteral(True)),For(Id(r'i'),IntLiteral(1),Id(r'N'),True,[If(BinaryOp(r'<>',ArrayCell(Id(r'A'),Id(r'i')),ArrayCell(Id(r'A'),BinaryOp(r'+',BinaryOp(r'-',Id(r'N'),Id(r'i')),IntLiteral(1)))),[Assign(Id(r'Flag'),BooleanLiteral(False))],[])]),Return(Id(r'flag'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,393))
    
    def test_multi_19_nest_scope(self):
        input = """
                Function xxx (  N :Integer) : Boolean;
                Var Flag : Boolean;
                 i :Integer;
                BEgin
                 begin
                 EnD
                 return Flag;
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xxx'),[VarDecl(Id(r'N'),IntType())],[VarDecl(Id(r'Flag'),BoolType()),VarDecl(Id(r'i'),IntType())],[Return(Id(r'Flag'))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,394))
    
    def test_multi_22_if_and_return_both_with_and_without_expr(self):
        input = """
                function power(x:integer):integer;
                BEgin
                if x = 0 then
                 return 1;
                else
                 return x*power(x-1);
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'power'),[VarDecl(Id(r'x'),IntType())],[],[If(BinaryOp(r'=',Id(r'x'),IntLiteral(0)),[Return(IntLiteral(1))],[Return(BinaryOp(r'*',Id(r'x'),CallExpr(Id(r'power'),[BinaryOp(r'-',Id(r'x'),IntLiteral(1))])))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,395))
    
    def test_multi_25_normal_with_file(self):
        input = """
                Procedure file(n: integer);
                BEgin
                 Assign(f,fo);
                  Rewrite(f);                 
                 Close(f);
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'file'),[VarDecl(Id(r'n'),IntType())],[],[CallStmt(Id(r'Assign'),[Id(r'f'),Id(r'fo')]),CallStmt(Id(r'Rewrite'),[Id(r'f')]),CallStmt(Id(r'Close'),[Id(r'f')])],VoidType())]))
        self.assertTrue(TestAST.test(input,expect,396))
    
    def test_multi_27_nest_begin_with_many_stmts(self):
        input = """
                Function ntny(m,n:integer):integer;
               
                 var a: real;
                  BEgin
                    begin
                        for i := 1 to 10 do 
                        a := a +1;
                        break;                    
					end
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'ntny'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'a'),FloatType())],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))]),Break()],IntType())]))
        self.assertTrue(TestAST.test(input,expect,397))
    
    def test_multi_28_really_long_int(self):
        input = """
procedure foo();
begin
    a := 123456789123456789;
    a := 123456789123456789123456789;
    a := 123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789;
    a := 123456789123456789123456789123456789123456789123456789123456789;
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),IntLiteral(123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789123456789)),Assign(Id(r'a'),IntLiteral(123456789123456789123456789123456789123456789123456789123456789))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_multi_29_LB_RB(self):
        input = """
procedure foo();
begin
    a := (((((((((((((((((((((((((((((((((((((((((u)))))))))))))))))))))))))))))))))))))))));
end
"""
        expect = str(Program([FuncDecl(Id(r'foo'),[],[],[Assign(Id(r'a'),Id(r'u'))],VoidType())]))
        self.assertTrue(TestAST.test(input, expect, 399))
    
    
    def test_multi_27_nest_begin_with_many_stmts_too(self):
        input = """
                Function xongroi(m,n:integer):integer;
               
                 var a: real;
                  BEgin
                    for i := 1 to 10 do 
                        x := x +1;                       
					begin
                        for i := 1 to 10 do 
                        a := a +1;
                        break;                    
					end
					for i := 1 to 10 do 
                        y := y +1;
                       
                EnD
                """
        expect = str(Program([FuncDecl(Id(r'xongroi'),[VarDecl(Id(r'm'),IntType()),VarDecl(Id(r'n'),IntType())],[VarDecl(Id(r'a'),FloatType())],[For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'x'),BinaryOp(r'+',Id(r'x'),IntLiteral(1)))]),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'a'),BinaryOp(r'+',Id(r'a'),IntLiteral(1)))]),Break(),For(Id(r'i'),IntLiteral(1),IntLiteral(10),True,[Assign(Id(r'y'),BinaryOp(r'+',Id(r'y'),IntLiteral(1)))])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,400))
    