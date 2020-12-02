import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_many_declaration_1(self):
        """Test Many Declaration"""
        input = """ Function foo():integer; Begin END
                    var x,y: real; 
                    var m:integer;
                    var a,b: real; 
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[]),VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(m),IntType),VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,301))

    def test_many_declaration_2(self):
        """Test Many Declaration"""
        input = """ var x,y: real; 
                    Procedure foo(a,b:integer); Begin END
                    Function foo(a,b:integer):integer; Begin END
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[]),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,302))

    def test_many_declaration_3(self):
        """Test Many Declaration"""
        input = """ var x,y: real; 
                    Procedure foo(a,b:integer); Begin END
                    var z: real; 
                    Function foo(a,b:integer):integer; Begin END
                    var a: real;                    
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],VoidType(),[],[]),VarDecl(Id(z),FloatType),FuncDecl(Id(foo),[VarDecl(Id(a),IntType),VarDecl(Id(b),IntType)],IntType,[],[]),VarDecl(Id(a),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,303))

    def test_var_decl_1(self):
        """Test Variable Declaration: many declaration"""
        input = """ var x,y: real; 
                        z: sTring;
                    var a,b: boolean;                        
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),StringType),VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType)])"
        self.assertTrue(TestAST.test(input,expect,304))

    def test_var_decl_2(self):
        """Test Variable Declaration: many declaration"""
        input = """ var x,y: real; 
                        z: sTring;
                    var a,b: boolean;
                    var c: string;
                        d,e,f: integer;
                        h:real;                        
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),StringType),VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType),VarDecl(Id(c),StringType),VarDecl(Id(d),IntType),VarDecl(Id(e),IntType),VarDecl(Id(f),IntType),VarDecl(Id(h),FloatType)])"
        self.assertTrue(TestAST.test(input,expect,305))

    def test_var_decl_3(self):
        """Test Variable Declaration: Array type"""
        input = """ var x,y: real; 
                        z: array [-1 .. 5] of integer;                      
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),ArrayType(-1,-5,IntType))])"
        self.assertTrue(TestAST.test(input,expect,306))


    def test_var_decl_4(self):
        """Test Variable Declaration: Array type"""
        input = """ var x,y: real; 
                    var    z: array [-1 .. 5] of integer;                      
                """
        expect = "Program([VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),ArrayType(-1,-5,IntType))])"
        self.assertTrue(TestAST.test(input,expect,307))

    def test_func_decl_1(self):
        """Test function declaration: parameter list"""
        input = """ Function foo():integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,308))

    def test_func_decl_2(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b,c:real):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(c),FloatType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_func_decl_3(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b:real;x,y:Boolean):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_func_decl_4(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a,b:real;x,y:Boolean;z:string):integer;
                        Begin
                         END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(b),FloatType),VarDecl(Id(x),BoolType),VarDecl(Id(y),BoolType),VarDecl(Id(z),StringType)],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_func_decl_5(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(a:real;z: array [-1 .. 5] of boolean):integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(a),FloatType),VarDecl(Id(z),ArrayType(-1,-5,BoolType))],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_func_decl_6(self):
        """Test function declaration: parameter list"""
        input = """ Function foo(z: array [-1 .. -55] of boolean):integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(Id(z),ArrayType(-1,-55,BoolType))],IntType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_func_decl_7(self):
        """Test function declaration: return type"""
        input = """ Function foo():boolean;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],BoolType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_func_decl_8(self):
        """Test function declaration: return type"""
        input = """ Function foo():real;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],FloatType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_func_decl_9(self):
        """Test function declaration: return type"""
        input = """ Function foo():string;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],StringType,[],[])])"
        self.assertTrue(TestAST.test(input,expect,316))

    def test_func_decl_10(self):
        """Test function declaration: return type"""
        input = """ Function foo():array [-1 .. -55] of string;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],ArrayType(-1,-55,StringType),[],[])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_func_decl_11(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType)],[])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_func_decl_12(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType)],[])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_func_decl_13(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                        var a: array [1 .. -5] of integer;
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType),VarDecl(Id(a),ArrayType(-1,-5,IntType))],[])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_func_decl_14(self):
        """Test function declaration: variable declaration"""
        input = """ Function foo():integer;
                        var x,y: real;
                            z: boolean;
                        var a: array [1 .. -5] of integer;
                        var b: array [1 .. -5] of real;
                        
                        Begin
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType),VarDecl(Id(z),BoolType),VarDecl(Id(a),ArrayType(-1,-5,IntType)),VarDecl(Id(b),ArrayType(-1,-5,FloatType))],[])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_expression_1(self):
        """Test expression:  andthen, orelse"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 anD then 1.2;
                            return "nm" or else true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(orelse,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_expression_2(self):
        """Test expression:  =, <>"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 = 1.2;
                            return "nm" > true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(=,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(>,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_expression_3(self):
        """Test expression:  <, <="""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 < 1.2;
                            return "nm" <= true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(<,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(<=,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test_expression_4(self):
        """Test expression:  >, >="""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 > 1.2;
                            return "nm" >= true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(>,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(>=,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_expression_5(self):
        """Test expression:  +, -"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 + 1.2;
                            return "nm" - true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(+,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(-,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,326))
        
    def test_expression_6(self):
        """Test expression:  or, /"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 or 1.2;
                            return "nm" / true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(or,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(/,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,327))
        
    def test_expression_7(self):
        """Test expression:  *, div"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 * 1.2;
                            return "nm" div true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(*,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(div,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,328))

    def test_expression_8(self):
        """Test expression:  mod, and"""
        input = """ Function foo():integer;                      
                        Begin
                            return a1 mod 1.2;
                            return "nm" and true;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(mod,Id(a1),FloatLiteral(1.2)))),Return(Some(BinaryOp(and,StringLiteral(nm),BooleanLiteral(True))))])])"
        self.assertTrue(TestAST.test(input,expect,329))

    def test_expression_9(self):
        """Test expression:  unary: -, not"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - 1.2;
                            return not true;
                            return  -2;
                            return not"nm";
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,FloatLiteral(1.2)))),Return(Some(UnaryOp(not,BooleanLiteral(True)))),Return(Some(UnaryOp(-,IntLiteral(2)))),Return(Some(UnaryOp(not,StringLiteral(nm))))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    def test_expression_10(self):
        """Test expression:  call function"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - foo();
                            return  - foo(x);

                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,CallExpr(Id(foo),[])))),Return(Some(UnaryOp(-,CallExpr(Id(foo),[Id(x)]))))])])"
        self.assertTrue(TestAST.test(input,expect,331))

    def test_expression_11(self):
        """Test expression:  call function"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - foo(x,y);
                            return  not foo(x,y,int(2,int1()));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,CallExpr(Id(foo),[Id(x),Id(y)])))),Return(Some(UnaryOp(not,CallExpr(Id(foo),[Id(x),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])])]))))])])"
        self.assertTrue(TestAST.test(input,expect,332))

    def test_expression_12(self):
        """Test expression:  index expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - 1[a];
                            return  - "2"[3][5];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,ArrayCell(IntLiteral(1),Id(a))))),Return(Some(UnaryOp(-,ArrayCell(ArrayCell(StringLiteral(2),IntLiteral(3)),IntLiteral(5)))))])])"
        self.assertTrue(TestAST.test(input,expect,333))
        
    def test_expression_13(self):
        """Test expression:  index expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  - ("ab"[tham])[123];
                            return  not true[false[23]];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(UnaryOp(-,ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123))))),Return(Some(UnaryOp(not,ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23))))))])])"
        self.assertTrue(TestAST.test(input,expect,334))

    def test_expression_14(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return  not true[false[23]] + ("ab"[tham])[123];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(+,UnaryOp(not,ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23)))),ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123)))))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    def test_expression_15(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return (1 - true[false[23]]) - ("ab"[tham])[123];
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(-,BinaryOp(-,IntLiteral(1),ArrayCell(BooleanLiteral(True),ArrayCell(BooleanLiteral(False),IntLiteral(23)))),ArrayCell(ArrayCell(StringLiteral(ab),Id(tham)),IntLiteral(123)))))])])"
        self.assertTrue(TestAST.test(input,expect,336))

    def test_expression_16(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return -1 and then true[1] - ("ab"=8)[123] * 1 = 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,UnaryOp(-,IntLiteral(1)),BinaryOp(=,BinaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)),BinaryOp(*,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123)),IntLiteral(1))),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,337))

    def test_expression_17(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return 1 >= false[23] + da(1[2],3) mod 1.3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(>=,IntLiteral(1),BinaryOp(+,ArrayCell(BooleanLiteral(False),IntLiteral(23)),BinaryOp(mod,CallExpr(Id(da),[ArrayCell(IntLiteral(1),IntLiteral(2)),IntLiteral(3)]),FloatLiteral(1.3))))))])])"
        self.assertTrue(TestAST.test(input,expect,338))

    def test_expression_18(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return -1 and -true[1] or ("ab"=8)[123] or else 1 > 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(orelse,BinaryOp(or,BinaryOp(and,UnaryOp(-,IntLiteral(1)),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123))),BinaryOp(>,IntLiteral(1),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,339))

    def test_expression_19(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return 1 - - true[1] or not ("ab"=8)[123] and then 1 = 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(andthen,BinaryOp(or,BinaryOp(-,IntLiteral(1),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),UnaryOp(not,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123)))),BinaryOp(=,IntLiteral(1),IntLiteral(3)))))])])"
        self.assertTrue(TestAST.test(input,expect,340))

    def test_expression_20(self):
        """Test expression:  complex expression"""
        input = """ Function foo():integer;                      
                        Begin
                            return - a[9] - - true[1] + foo(1,2) or not ("ab"=8)[123] ;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Return(Some(BinaryOp(or,BinaryOp(+,BinaryOp(-,UnaryOp(-,ArrayCell(Id(a),IntLiteral(9))),UnaryOp(-,ArrayCell(BooleanLiteral(True),IntLiteral(1)))),CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])),UnaryOp(not,ArrayCell(BinaryOp(=,StringLiteral(ab),IntLiteral(8)),IntLiteral(123))))))])])"
        self.assertTrue(TestAST.test(input,expect,341))

    def test_statement_1(self):
        """Test statement:  continue"""
        input = """ Function foo():integer;                      
                        Begin
                            continue;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Continue])])"
        self.assertTrue(TestAST.test(input,expect,342))

    def test_statement_2(self):
        """Test statement:  Break"""
        input = """ Function foo():integer;                      
                        Begin
                            Break;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[Break])])"
        self.assertTrue(TestAST.test(input,expect,343))

    def test_statement_3(self):
        """Test statement:  For statement"""
        input = """ Function foo():integer;                      
                        Begin
                            for i := 1 to 2 do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[For(Id(i)IntLiteral(1),IntLiteral(2),True,[Break])])])"
        self.assertTrue(TestAST.test(input,expect,344))

    def test_statement_4(self):
        """Test statement:  While statement"""
        input = """ Function foo():integer;                      
                        Begin
                            While i = 1 do break; 
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[While(BinaryOp(=,Id(i),IntLiteral(1)),[Break])])])"
        self.assertTrue(TestAST.test(input,expect,345))

    def test_statement_5(self):
        """Test statement:  If statement"""
        input = """ Function foo():integer;                      
                        Begin
                            If (1) then return 2;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(IntLiteral(1),[Return(Some(IntLiteral(2)))],[])])])"
        self.assertTrue(TestAST.test(input,expect,346))

    def test_statement_6(self):
        """Test statement:  If statement"""
        input = """ Function foo():integer;                      
                        Begin
                            If (1) then return 2; else return 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[If(IntLiteral(1),[Return(Some(IntLiteral(2)))],[Return(Some(IntLiteral(3)))])])])"
        self.assertTrue(TestAST.test(input,expect,347))

    def test_statement_7(self):
        """Test statement:  With statement"""
        input = """ Function foo():integer;                      
                        Begin
                            with a:integer; b: boolean; do break;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[With([VarDecl(Id(a),IntType),VarDecl(Id(b),BoolType)],[Break])])])"
        self.assertTrue(TestAST.test(input,expect,348))

    def test_statement_8(self):
        """Test statement:  Call statement"""
        input = """ Function foo():integer;                      
                        Begin
                            foo(x,y,int(2,int1()));
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[CallStmt(Id(foo),[Id(x),Id(y),CallExpr(Id(int),[IntLiteral(2),CallExpr(Id(int1),[])])])])])"
        self.assertTrue(TestAST.test(input,expect,349))

    def test_statement_9(self):
        """Test statement:  Assignment statement"""
        input = """ Function foo():integer;                      
                        Begin

                            a := de := d := 3;
                        END
                """
        expect = "Program([FuncDecl(Id(foo),[],IntType,[],[AssignStmt(Id(d),IntLiteral(3)),AssignStmt(Id(de),Id(d)),AssignStmt(Id(a),Id(de))])])"
        self.assertTrue(TestAST.test(input,expect,350))
