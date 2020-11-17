import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;
        """
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """Var:x =5 ;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """Var:x[12];"""
        expect = Program([VarDecl(Id("x"),[12],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """Var:x[0x13];"""
        expect = Program([VarDecl(Id("x"),[19],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """Var:x[0x12][13]=5;"""
        expect = Program([VarDecl(Id("x"),[18,13],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
 
    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """Var:x;
        Var: x=12;"""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(12))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """Var: x[12]={12};"""
        expect = Program([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = """Var: arr[5][6] = {1,2}, y[1];"""
        expect = Program([VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_simple_program8(self):
        """Simple program: int main() {} """
        input = """Function: foo 
        Parameter: n 
        Body: 
            Var: x[12]={12};
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """Var: b = True, c = False;"""
        expect = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
   
    def test_func_declare(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],(([VarDecl(Id("x"),[],IntLiteral(2))],[])))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))    
    
    def test_func_declare1(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = 3;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))   
    
    def test_func_declare2(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        (3+5)[12] = 3 ;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(ArrayCell(BinaryOp("+",IntLiteral(3),IntLiteral(5)),[IntLiteral(12)]),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))   
    
    def test_func_declare3(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = 3+5 ;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),BinaryOp("+",IntLiteral(3),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_func_declare4(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        Var:a=5;
                        x = 3*5 ;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("a"),[],IntLiteral(5))],[Assign(Id("x"),BinaryOp("*",IntLiteral(3),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    
    def test_func_declare5(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = 3 && 5 ;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),BinaryOp("&&",IntLiteral(3),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    
    def test_func_declare6(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = -3;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),UnaryOp("-",IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    
    def test_func_declare7(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = !3 ;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),UnaryOp("!",IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    
    def test_assign_statement1(self):
        """Simple program: int main() {} """
        input = """Function: foo 
        Parameter: n 
        Body: 
            n = (9 + 2\\2);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("n"),BinaryOp("+",IntLiteral(9),BinaryOp("\\",IntLiteral(2),IntLiteral(2))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    
    def test_assign_statement2(self):
        """Simple program: int main() {} """
        input = """Function: foo 
        Parameter: n 
        Body: 
            n[3][4] = {1,2,{3,4,5}};
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("n"),[IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(1),IntLiteral(2),ArrayLiteral([IntLiteral(3),IntLiteral(4),IntLiteral(5)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    
    def test_if_statement2(self):
        input = """Function: foo 
        Body:
            If True Then
                x = 3;
            Else 
                x = 2;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[],[Assign(Id("x"),IntLiteral(3))])],([],[Assign(Id("x"),IntLiteral(2))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_if_statement1(self):
        input = """Function: foo 
        Body:
            If True Then
                Var: a;
                Var: x;
                Var: y;
                x = 1;
                y = 2;
                z = 3;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[VarDecl(Id("a"),[],None),VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None)],[Assign(Id("x"),IntLiteral(1)),Assign(Id("y"),IntLiteral(2)),Assign(Id("z"),IntLiteral(3))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_while_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While i < 5 Do
                a= b +. 1.0;
            EndWhile.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[Assign(Id("a"),BinaryOp("+.",Id("b"),FloatLiteral(1.0)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_for_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_for_statement1(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 6*9,True, i-1) Do
            Var:x=5;
            a=3;
        EndFor.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),BinaryOp("*",IntLiteral(6),IntLiteral(9)),BooleanLiteral(True),BinaryOp("-",Id("i"),IntLiteral(1)),([VarDecl(Id("x"),[],IntLiteral(5))],[Assign(Id("a"),IntLiteral(3))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_while_statement1(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: i = 0;
            While i < 5 Do

            EndWhile.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    
    def test_if_and_while_statement1(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                EndIf.
            EndWhile.
        EndBody."""

        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("x"),IntLiteral(1)),([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Return(None)])],([],[]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

   
    def test_Do_while_statement2(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                Do
                While(b!=4)
                EndDo.
            While(a!=3)                
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[Dowhile(([],[]),BinaryOp("!=",Id("b"),IntLiteral(4)))]),BinaryOp("!=",Id("a"),IntLiteral(3)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_Do_while_statement3(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Do  
                Return foo(x,y);
            While True
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[Return(CallExpr(Id("foo"),[Id("x"),Id("y")]))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_Break_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Break;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_Break_statement1(self):
        input = """Function: foo 
        Parameter: n
        Body:
            If a<3 Then
                Break;
            EndIf.
        EndBody."""
        #expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("<",Id("a"),IntLiteral(3)),[],[Break()])],())]))])
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("<",Id("a"),IntLiteral(3)),[],[Break()])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    
    def test_Continue_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                Continue;
            While True
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[Continue()]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_Return_statement(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Do
                Return a+3;
            While True
            EndDo.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Dowhile(([],[Return(BinaryOp("+",Id("a"),IntLiteral(3)))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_Return_statement2(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Return foo(x +3,y);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Return(CallExpr(Id("foo"),[BinaryOp("+",Id("x"),IntLiteral(3)),Id("y")]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    
    def test_CallStmt(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            foo(x +3,y +. 10.2);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[CallStmt(Id("foo"),[BinaryOp("+",Id("x"),IntLiteral(3)),BinaryOp("+.",Id("y"),FloatLiteral(10.2))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    
    def test_CallStmt1(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            test(a,3*7, a+ 5,"string",True);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[CallStmt(Id("test"),[Id("a"),BinaryOp("*",IntLiteral(3),IntLiteral(7)),BinaryOp("+",Id("a"),IntLiteral(5)),StringLiteral("string"),BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    
    def test_Expr(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            a= (a==b)!= c +3;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("a"),BinaryOp("!=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("+",Id("c"),IntLiteral(3))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    
    def test_if_statement10(self):
        """Simple program: int main() {} """
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    If n!=0 Then
                        a=5;
                    EndIf.
                EndIf.
            EndIf.
        EndBody."""   
        #expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[Assign(Id("a"),IntLiteral(5))])],())])],())])],())]))])
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[If([(BinaryOp("!=",Id("n"),IntLiteral(0)),[],[Assign(Id("a"),IntLiteral(5))])],([],[]))])],([],[]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    
    def test_if_statement12(self):
        input = """Function: foo 
        Body:
            If True Then
            ElseIf True Then
                x = 2;
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[],[]),(BooleanLiteral(True),[],[Assign(Id("x"),IntLiteral(2))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    
    
    
    def test_1(self):
        """ test_ for_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
        For (i = 0, i < 10, 2) Do
            writeln(i);
        EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    
    def test_2(self):
        input = """Function: foo 
        Parameter: n
        Body: 
        EndBody.
        Function: goo 
        Parameter: n
        Body: 
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[])),FuncDecl(Id("goo"),[VarDecl(Id("n"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    
    def test_3(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            c = -.a;
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("c"),UnaryOp("-.",Id("a")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_4(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x>1 Do
                If x==1 Then Return;
                Else Continue;
                EndIf.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("x"),IntLiteral(1)),([],[If([(BinaryOp("==",Id("x"),IntLiteral(1)),[],[Return(None)])],([],[Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_100(self):
        input = """Var: x;
                    Var: a,b,c;
                    Var: a[100];
                """
        expect =Program([VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("a"),[100],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_5(self):
        input = """ Function: testIfStatement
                        Parameter: x, a, b, c
                        Body:
                            If(x == ((False||True) && (a > b + c))) Then
                                a = b - c;
                            Else
                                a = b + c;
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("testIfStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],([],[If([(BinaryOp("==",Id("x"),BinaryOp("&&",BinaryOp("||",BooleanLiteral(False),BooleanLiteral(True)),BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),Id("c"))))),[],[Assign(Id("a"),BinaryOp("-",Id("b"),Id("c")))])],([],[Assign(Id("a"),BinaryOp("+",Id("b"),Id("c"))),Assign(Id("x"),BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_6(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While(1) Do
                While(!x) Do
                    x = True;
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(IntLiteral(1),([],[While(UnaryOp("!",Id("x")),([],[Assign(Id("x"),BooleanLiteral(True))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_7(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            foo(2 + x, 4. \. y); 
            goo ();
        EndBody.
        """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\.",FloatLiteral(4.0),Id("y"))]),CallStmt(Id("goo"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    
    def test_8(self):
        input = """Function: foo 
        Parameter: n, a[10]
        Body: 
        
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None),VarDecl(Id("a"),[10],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    
    def test_9(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    
    def test_10(self):
        """ test_ index operator function """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[3+foo(3)] = a[b[2][3]] + 4;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(3)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    
    def test_11(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("r"),[],FloatLiteral(10.0)),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    
    def test_12(self):
        input = """
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    
    def test_13(self):
        input = """Function: foo 
        Parameter: n
        Body: ** Xin chao**
        string = "Xin chao";
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("string"),StringLiteral("Xin chao"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    
    def test_14(self):
        input = """
        Var: b[2][3]={{1,2,3},{4,5,6}};
        Var: a[5] = {1,2,3};
        """
        expect = Program([VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("a"),[5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    
    def test_15(self):
        """ test_ assign_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            x1 = a[3-foo(3)];
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("x1"),ArrayCell(Id("a"),[BinaryOp("-",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(3)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_16(self):
        input = """
        Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
        Function: foo 
        Parameter: n
        Body: 
        EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])])),FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    
    def test_17(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            For (ctx = 10,(foo()+3)[5],i+1) Do x=6; EndFor.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[For(Id("ctx"),IntLiteral(10),ArrayCell(BinaryOp("+",CallExpr(Id("foo"),[]),IntLiteral(3)),[IntLiteral(5)]),BinaryOp("+",Id("i"),IntLiteral(1)),([],[Assign(Id("x"),IntLiteral(6))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_18(self):
        input = """Function: foo
                        Parameter: x
                        Body:
                            For (i = 1, i <= x*x*x,i + x ) Do
                                writeln(i);
                            EndFor.
                        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None)],([],[For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x"))),BinaryOp("+",Id("i"),Id("x")),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    
    def test_19(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While((x > a) && (x < b)) Do
                While((x >= b) || (x >= a)) Do
                    While((x > c * b) && (x < b*b)) Do
                        x = x - 1;
                        c = 2 * c;
                        While( !False ) Do
                            a = a * 1;
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),Id("a")),BinaryOp("<",Id("x"),Id("b"))),([],[While(BinaryOp("||",BinaryOp(">=",Id("x"),Id("b")),BinaryOp(">=",Id("x"),Id("a"))),([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),BinaryOp("*",Id("c"),Id("b"))),BinaryOp("<",Id("x"),BinaryOp("*",Id("b"),Id("b")))),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("c"),BinaryOp("*",IntLiteral(2),Id("c"))),While(UnaryOp("!",BooleanLiteral(False)),([],[Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(1)))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_20(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            test(a,3*7, 5,"string",True);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[CallStmt(Id("test"),[Id("a"),BinaryOp("*",IntLiteral(3),IntLiteral(7)),IntLiteral(5),StringLiteral("string"),BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    
    def test_21(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            x= (y+3)+. 0.e3 - (z -. -9);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("x"),BinaryOp("-",BinaryOp("+.",BinaryOp("+",Id("y"),IntLiteral(3)),FloatLiteral(0.0)),BinaryOp("-.",Id("z"),UnaryOp("-",IntLiteral(9)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    
    def test_22(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            x= (x*3)*. 0x3E \ (y \. 0.123) % 5;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("x"),BinaryOp("%",BinaryOp("\\",BinaryOp("*.",BinaryOp("*",Id("x"),IntLiteral(3)),IntLiteral(62)),BinaryOp("\.",Id("y"),FloatLiteral(0.123))),IntLiteral(5)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_23(self):
        """ test__ index operator """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(3),CallExpr(Id("foo"),[IntLiteral(2)])),BinaryOp("||",Id("b"),BooleanLiteral(True))]),ArrayCell(Id("b"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(1),IntLiteral(873))])])]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),BinaryOp("*",ArrayCell(Id("b"),[FloatLiteral(1.2e-08)]),IntLiteral(3))])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    
    def test_24(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            a= foo(a,b) + goo (x);
        EndBody."""
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("a"),BinaryOp("+",CallExpr(Id("foo"),[Id("a"),Id("b")]),CallExpr(Id("goo"),[Id("x")])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    
    def test_25(self):
        input = """ Function: foo 
                        Parameter: n[1][2][3], abc
                        Body:
                        n[1][0x2AB][0o12] = abc * abc;
                        EndBody.                    

                    Function: exp
                        Parameter: a,b,c,e,d,f
                        Body:
                        a = b+c-e*d\\f;
                        EndBody.
                    
                    Function: justforfun5
                        Parameter: a[10], b[10], c[10], d[10]
                        Body:
                        a[10] = 12.e4;
                        b[10] = 0.e4;
                        c[10] = 12.e4 -. 1;

                        EndBody.         
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[1,2,3],None),VarDecl(Id("abc"),[],None)],([],[Assign(ArrayCell(Id("n"),[IntLiteral(1),IntLiteral(683),IntLiteral(10)]),BinaryOp("*",Id("abc"),Id("abc")))])),FuncDecl(Id("exp"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("e"),[],None),VarDecl(Id("d"),[],None),VarDecl(Id("f"),[],None)],([],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",Id("b"),Id("c")),BinaryOp("\\",BinaryOp("*",Id("e"),Id("d")),Id("f"))))])),FuncDecl(Id("justforfun5"),[VarDecl(Id("a"),[10],None),VarDecl(Id("b"),[10],None),VarDecl(Id("c"),[10],None),VarDecl(Id("d"),[10],None)],([],[Assign(ArrayCell(Id("a"),[IntLiteral(10)]),FloatLiteral(120000.0)),Assign(ArrayCell(Id("b"),[IntLiteral(10)]),FloatLiteral(0.0)),Assign(ArrayCell(Id("c"),[IntLiteral(10)]),BinaryOp("-.",FloatLiteral(120000.0),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
        
    def test_26(self):
        input = """ Function: testIfStatement
                        Parameter: a, b, c, d
                        Body:
                            If (a == True) Then a = False;
                            ElseIf (b == True) Then b = False;
                            ElseIf (c == True) Then c = False;
                            Else d = False;
                            EndIf.
                        EndBody.
                    """

        expect = Program([FuncDecl(Id("testIfStatement"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None)],([],[If([(BinaryOp("==",Id("a"),BooleanLiteral(True)),[],[Assign(Id("a"),BooleanLiteral(False))]),(BinaryOp("==",Id("b"),BooleanLiteral(True)),[],[Assign(Id("b"),BooleanLiteral(False))]),(BinaryOp("==",Id("c"),BooleanLiteral(True)),[],[Assign(Id("c"),BooleanLiteral(False))])],([],[Assign(Id("d"),BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    
    def test_27(self):
        input = """ Function: testIfStatement
                        Parameter: x, y, z
                        Body:
                            If(x == True) Then 
                                If(y == False) Then
                                    If(z == False) Then
                                        x = foo();
                                    Else
                                        x = !a;
                                    EndIf.
                                Else
                                    Break;
                                EndIf.
                            ElseIf((x || y || z ) == True) Then
                                Continue;
                                z = egoo(x *. 3);
                                Return x+y;
                            Else
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("testIfStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[If([(BinaryOp("==",Id("x"),BooleanLiteral(True)),[],[If([(BinaryOp("==",Id("y"),BooleanLiteral(False)),[],[If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("foo"),[]))])],([],[Assign(Id("x"),UnaryOp("!",Id("a")))]))])],([],[Break()]))]),(BinaryOp("==",BinaryOp("||",BinaryOp("||",Id("x"),Id("y")),Id("z")),BooleanLiteral(True)),[],[Continue(),Assign(Id("z"),CallExpr(Id("egoo"),[BinaryOp("*.",Id("x"),IntLiteral(3))])),Return(BinaryOp("+",Id("x"),Id("y")))])],([],[Assign(Id("x"),BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_28(self):
        input = """ Function: testForStatement
                        Parameter: x, array[10][10][10][10]
                        Body:
                            For (i = 1, i < x*x , i + 1 ) Do
                                For( j = 1, j < x*x ,j + 1) Do
                                    For( k = 1, k < x*x , k + 1 ) Do
                                        For( l = 1 , l < x*x ,l + 1) Do
                                            r = 3.14;
                                            s = r*r + 2;
                                            t = s && !foo(2) || r =/= 9. && (2+3)*.5.;
                                            t = t \\. 3.;
                                        EndFor.
                                    EndFor.
                                EndFor.    
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        expect = Program([FuncDecl(Id("testForStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("array"),[10,10,10,10],None)],([],[For(Id("i"),IntLiteral(1),BinaryOp("<",Id("i"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("i"),IntLiteral(1)),([],[For(Id("j"),IntLiteral(1),BinaryOp("<",Id("j"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("j"),IntLiteral(1)),([],[For(Id("k"),IntLiteral(1),BinaryOp("<",Id("k"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("k"),IntLiteral(1)),([],[For(Id("l"),IntLiteral(1),BinaryOp("<",Id("l"),BinaryOp("*",Id("x"),Id("x"))),BinaryOp("+",Id("l"),IntLiteral(1)),([],[Assign(Id("r"),FloatLiteral(3.14)),Assign(Id("s"),BinaryOp("+",BinaryOp("*",Id("r"),Id("r")),IntLiteral(2))),Assign(Id("t"),BinaryOp("=/=",BinaryOp("||",BinaryOp("&&",Id("s"),UnaryOp("!",CallExpr(Id("foo"),[IntLiteral(2)]))),Id("r")),BinaryOp("&&",FloatLiteral(9.0),BinaryOp("*.",BinaryOp("+",IntLiteral(2),IntLiteral(3)),FloatLiteral(5.0))))),Assign(Id("t"),BinaryOp("\.",Id("t"),FloatLiteral(3.0)))]))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_29(self):
        input = """ Function: testWhileStatement
                        Parameter: x,a,b,c,d
                        Body:
                            While(x > a) Do
                                While(x > b) Do
                                    While(x > c) Do
                                        While(x > d) Do
                                            x = "True";
                                        EndWhile.
                                        x = {"True"};
                                    EndWhile.
                                    x = **True** False;
                                EndWhile.
                                x = (True)&&False;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        expect = Program([FuncDecl(Id("testWhileStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],None)],([],[While(BinaryOp(">",Id("x"),Id("a")),([],[While(BinaryOp(">",Id("x"),Id("b")),([],[While(BinaryOp(">",Id("x"),Id("c")),([],[While(BinaryOp(">",Id("x"),Id("d")),([],[Assign(Id("x"),StringLiteral("True"))])),Assign(Id("x"),ArrayLiteral([StringLiteral("True")]))])),Assign(Id("x"),BooleanLiteral(False))])),Assign(Id("x"),BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_30(self):
        input = """ Function: testWhileStatement
                        Parameter: x
                        Body:
                            While((x > a) && (x < b)) Do
                                While((x >= b) || (x >= a)) Do
                                    While((x > c * b) && (x < b*b)) Do
                                        While(x > d) Do
                                            x = x - 1;
                                            d = d + 1;
                                        EndWhile.
                                    If(y == False) Then
                                        If(z == False) Then
                                            x = foo();
                                        Else
                                            x = !a;
                                        EndIf.
                                    Else
                                        Break;
                                    EndIf.
                                    EndWhile.
                                    
                                If(z == False) Then
                                    x = foo();
                                EndIf.
                                EndWhile.
                                x = x - 1;
                                a = a + 1;
                                While( !False ) Do
                                    a = a * 1;
                                EndWhile.
                            EndWhile.
                        EndBody.
                    """

        #expect = Program([FuncDecl(Id("testWhileStatement"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),Id("a")),BinaryOp("<",Id("x"),Id("b"))),([],[While(BinaryOp("||",BinaryOp(">=",Id("x"),Id("b")),BinaryOp(">=",Id("x"),Id("a"))),([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),BinaryOp("*",Id("c"),Id("b"))),BinaryOp("<",Id("x"),BinaryOp("*",Id("b"),Id("b")))),([],[While(BinaryOp(">",Id("x"),Id("d")),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1)))])),If([(BinaryOp("==",Id("y"),BooleanLiteral(False)),[],[If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("foo"),[]))])],([],[Assign(Id("x"),UnaryOp("!",Id("a")))]))])],([],[Break()]))])),If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("foo"),[]))])],())])),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),While(UnaryOp("!",BooleanLiteral(False)),([],[Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(1)))]))]))]))])
        expect = Program([FuncDecl(Id("testWhileStatement"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),Id("a")),BinaryOp("<",Id("x"),Id("b"))),([],[While(BinaryOp("||",BinaryOp(">=",Id("x"),Id("b")),BinaryOp(">=",Id("x"),Id("a"))),([],[While(BinaryOp("&&",BinaryOp(">",Id("x"),BinaryOp("*",Id("c"),Id("b"))),BinaryOp("<",Id("x"),BinaryOp("*",Id("b"),Id("b")))),([],[While(BinaryOp(">",Id("x"),Id("d")),([],[Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("d"),BinaryOp("+",Id("d"),IntLiteral(1)))])),If([(BinaryOp("==",Id("y"),BooleanLiteral(False)),[],[If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("foo"),[]))])],([],[Assign(Id("x"),UnaryOp("!",Id("a")))]))])],([],[Break()]))])),If([(BinaryOp("==",Id("z"),BooleanLiteral(False)),[],[Assign(Id("x"),CallExpr(Id("foo"),[]))])],([],[]))])),Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1))),Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1))),While(UnaryOp("!",BooleanLiteral(False)),([],[Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
        
    def test_31(self):
        input = """ Function: testDoWhileStatement
                        Parameter: x,a,b[10][10]
                        Body:
                            Do
                                x = x + 1;
                                Do
                                    a = a + 2;
                                    Do
                                        z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                                    While(!t == !(r && False || 2-2) )
                                    EndDo.
                                While( a < 50)
                                EndDo.
                            While(x < 100)
                            EndDo.
                            
                        EndBody.
                    """
        expect = "successful"
        expect = Program([FuncDecl(Id("testDoWhileStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("a"),[],None),VarDecl(Id("b"),[10,10],None)],([],[Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),Dowhile(([],[Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(2))),Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[])))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]),BinaryOp("<",Id("a"),IntLiteral(50)))]),BinaryOp("<",Id("x"),IntLiteral(100)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))


    def test_32(self):
        input = """ """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))        

    def test_33(self):
        input = """
            Function: test
            Parameter: n
            Body:
                Var: x;   
                For (i = 0, i < sqrt(n)*2, 1) Do
                    x = i + n;
                    writeln(x\\2);
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[],None)],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),BinaryOp("*",CallExpr(Id("sqrt"),[Id("n")]),IntLiteral(2))),IntLiteral(1),([],[Assign(Id("x"),BinaryOp("+",Id("i"),Id("n"))),CallStmt(Id("writeln"),[BinaryOp("\\",Id("x"),IntLiteral(2))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))  
        
    def test_34(self):
        input = """
            Function: test
            Body:
                Var: flag = False, c;
                c = !False;
                For (i = 0, flag == c, 1) Do
                    flag = True;
                    Do
                        z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                    While(!t == !(r && False || 2-2) )
                    EndDo.
                EndFor.
            EndBody.
        """
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("flag"),[],BooleanLiteral(False)),VarDecl(Id("c"),[],None)],[Assign(Id("c"),UnaryOp("!",BooleanLiteral(False))),For(Id("i"),IntLiteral(0),BinaryOp("==",Id("flag"),Id("c")),IntLiteral(1),([],[Assign(Id("flag"),BooleanLiteral(True)),Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[])))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373)) 


    def test_35(self):
        input = """Function: test
            Body:
                foo(x+y,goo());
                a= foo(x+y,goo());
                b= goo(print(f)) + "String";
                Return foo();
            EndBody. """
        expect = Program([FuncDecl(Id("test"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("goo"),[])]),Assign(Id("a"),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("goo"),[])])),Assign(Id("b"),BinaryOp("+",CallExpr(Id("goo"),[CallExpr(Id("print"),[Id("f")])]),StringLiteral("String"))),Return(CallExpr(Id("foo"),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))      

    def test_36(self):
        input = """
            Function: test
            Body:
                foo(x+y,goo());
                a= foo(x+y,goo());
                b= goo(print(f)) + "String";
                Return foo();
            EndBody. """
        expect = Program([FuncDecl(Id("test"),[],([],[CallStmt(Id("foo"),[BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("goo"),[])]),Assign(Id("a"),CallExpr(Id("foo"),[BinaryOp("+",Id("x"),Id("y")),CallExpr(Id("goo"),[])])),Assign(Id("b"),BinaryOp("+",CallExpr(Id("goo"),[CallExpr(Id("print"),[Id("f")])]),StringLiteral("String"))),Return(CallExpr(Id("foo"),[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))     

    def test_37(self):
        input = """
            Var: x[12]={12};
            Var: arr[5][6] = {1,2}, y[1];
            Var:x[0x12][13]=5; 
            Function: foo 
            Body:
            If True Then
                Var: x[12]={12};
                Var: arr[5][6] = {1,2}, y[1];
                Var:x[0x12][13]=5; 
                x = 1;
                y = 2;
                z = 3;
                z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                If (a == True) Then a = False;
                ElseIf (b == True) Then b = False;
                ElseIf (c == True) Then c = False;
                Else d = False;
                EndIf.
            EndIf.
        EndBody."""
        expect = Program([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)])),VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None),VarDecl(Id("x"),[18,13],IntLiteral(5)),FuncDecl(Id("foo"),[],([],[If([(BooleanLiteral(True),[VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)])),VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None),VarDecl(Id("x"),[18,13],IntLiteral(5))],[Assign(Id("x"),IntLiteral(1)),Assign(Id("y"),IntLiteral(2)),Assign(Id("z"),IntLiteral(3)),Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[]))),If([(BinaryOp("==",Id("a"),BooleanLiteral(True)),[],[Assign(Id("a"),BooleanLiteral(False))]),(BinaryOp("==",Id("b"),BooleanLiteral(True)),[],[Assign(Id("b"),BooleanLiteral(False))]),(BinaryOp("==",Id("c"),BooleanLiteral(True)),[],[Assign(Id("c"),BooleanLiteral(False))])],([],[Assign(Id("d"),BooleanLiteral(False))]))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_38(self):
        input = """
        Function: test
        Body:
            Return 1 +. 3e-14 - "ABC" + {1,2,3} \\. 2.;
        EndBody.
        """        
        expect = Program([FuncDecl(Id("test"),[],([],[Return(BinaryOp("+",BinaryOp("-",BinaryOp("+.",IntLiteral(1),FloatLiteral(3e-14)),StringLiteral("ABC")),BinaryOp("\.",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),FloatLiteral(2.0))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_39(self):
        input = """
            Var: x= "Stringasdfa";
            Function: test
            Body:
                a= "bc" +"bc" +"bc" +"bc" +"bc" + **abd** "bc";
                a= "bc" +"bc" +"bc" +"bc" +"bc" +"bc";
                a= "bc" +"bc" +"bc" +"bc" +"bc" +"bc";
                a= "bc" +"bc" +"bc" +"bc" +"bc" +"bc";
                a= "bc" +"bc" +"bc" +"bc" +"bc" +"bc";
                Break;
            EndBody.
            """
        expect = Program([VarDecl(Id("x"),[],StringLiteral("Stringasdfa")),FuncDecl(Id("test"),[],([],[Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("bc"),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc"))),Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("bc"),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc"))),Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("bc"),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc"))),Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("bc"),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc"))),Assign(Id("a"),BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",BinaryOp("+",StringLiteral("bc"),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc")),StringLiteral("bc"))),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_40(self):
        input = """
            Function: test
            Body:
            EndBody. 
            Function: test
            Parameter: n
            Body:
            EndBody.
            Function: test
            Body:
            EndBody.
            Function: test
            Body:
            EndBody.
            Function: test
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([],[])),FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[],([],[])),FuncDecl(Id("test"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_41(self):
        input = """Function: test
            Body:
                Return a;
                Return ;
                Return "abc";
                Return none;
                Return **Comment**;
            EndBody.  """
        expect = Program([FuncDecl(Id("test"),[],([],[Return(Id("a")),Return(None),Return(StringLiteral("abc")),Return(Id("none")),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_42(self):
        input = """
            Function: test
            Body:
                Break;
                Break;
                Break;
                Break;
                Break;
            EndBody.  """
        expect = Program([FuncDecl(Id("test"),[],([],[Break(),Break(),Break(),Break(),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,381))
        
    def test_43(self):
        input = """
            Function: test
            Body:
                Continue;
                Break;
                Continue;
                Break;
                Continue;
            EndBody.  """
        expect = Program([FuncDecl(Id("test"),[],([],[Continue(),Break(),Continue(),Break(),Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_44(self):
        input = """
        Function: test
        Body:
            Var: outer = 1;
            While (outer <= 5) Do
                Var: inner = 1;
                While (inner <= 5) Do
                    print(inner);
                    inner = inner + 1;
                    Do
                        z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                    While(!t == !(r && False || 2-2) )
                    EndDo.
                EndWhile.
                outer = outer + 1;
                Do
                    z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                While(!t == !(r && False || 2-2) )
                EndDo.
            EndWhile.
        EndBody.
        """
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("outer"),[],IntLiteral(1))],[While(BinaryOp("<=",Id("outer"),IntLiteral(5)),([VarDecl(Id("inner"),[],IntLiteral(1))],[While(BinaryOp("<=",Id("inner"),IntLiteral(5)),([],[CallStmt(Id("print"),[Id("inner")]),Assign(Id("inner"),BinaryOp("+",Id("inner"),IntLiteral(1))),Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[])))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))])),Assign(Id("outer"),BinaryOp("+",Id("outer"),IntLiteral(1))),Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[])))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_45(self):
        input = """ 
            Function: test 
            Body:
                Var: x, y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                    Do
                        z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                        If n == 0 Then
                            Return 1;
                        ElseIf (b == True) Then 
                            Do
                                z = (x*x*x*x*x*x*x)\\.(2.*.y -. 2.3e12 + 23\\11 + 12%2) - test();
                            While(!t == !(r && False || 2-2) )
                            EndDo.
                        ElseIf (c == True) Then c = False;
                        Else
                            Return n * fact (n - 1);
                        EndIf.
                    While(!t == !(r && False || 2-2) )
                    EndDo.
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],None),VarDecl(Id("y"),[1,3],ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(12),IntLiteral(1)]),ArrayLiteral([FloatLiteral(12.0),FloatLiteral(12000.0)])]),ArrayLiteral([IntLiteral(23)]),ArrayLiteral([IntLiteral(13),IntLiteral(32)])]))],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")]),Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[]))),If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))]),(BinaryOp("==",Id("b"),BooleanLiteral(True)),[],[Dowhile(([],[Assign(Id("z"),BinaryOp("-",BinaryOp("\.",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",Id("x"),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),Id("x")),BinaryOp("+",BinaryOp("+",BinaryOp("-.",BinaryOp("*.",FloatLiteral(2.0),Id("y")),FloatLiteral(2300000000000.0)),BinaryOp("\\",IntLiteral(23),IntLiteral(11))),BinaryOp("%",IntLiteral(12),IntLiteral(2)))),CallExpr(Id("test"),[])))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]),(BinaryOp("==",Id("c"),BooleanLiteral(True)),[],[Assign(Id("c"),BooleanLiteral(False))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]),BinaryOp("==",UnaryOp("!",Id("t")),UnaryOp("!",BinaryOp("||",BinaryOp("&&",Id("r"),BooleanLiteral(False)),BinaryOp("-",IntLiteral(2),IntLiteral(2))))))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_46(self):
        input = """
            Function: test 
            Body:
                Var: arr[2][3] = {"Tuasfi",{"asd","asd"},{"tsas",{"caccas"},12}}; 
                e = 3 +. 10e2;
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("arr"),[2,3],ArrayLiteral([StringLiteral("Tuasfi"),ArrayLiteral([StringLiteral("asd"),StringLiteral("asd")]),ArrayLiteral([StringLiteral("tsas"),ArrayLiteral([StringLiteral("caccas")]),IntLiteral(12)])]))],[Assign(Id("e"),BinaryOp("+.",IntLiteral(3),FloatLiteral(1000.0)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_47(self):
        input = """ 
            Function: test 
            Body:
                a[foo(x)+12] = ("String" + 12.e3) *. 0x123;
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",CallExpr(Id("foo"),[Id("x")]),IntLiteral(12))]),BinaryOp("*.",BinaryOp("+",StringLiteral("String"),FloatLiteral(12000.0)),IntLiteral(291)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_48(self):
        input = """
            Function: test 
            Body:
                a[True] = (foo(a+b,c >d) + 12.e3) *. 0x123;
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"),[],([],[Assign(ArrayCell(Id("a"),[BooleanLiteral(True)]),BinaryOp("*.",BinaryOp("+",CallExpr(Id("foo"),[BinaryOp("+",Id("a"),Id("b")),BinaryOp(">",Id("c"),Id("d"))]),FloatLiteral(12000.0)),IntLiteral(291)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_49(self):
        input = """
            Function: test
            Body:
                Var: a = 2;
                For (index = foo(3*x), index < 100, "String" + {"abc","a"**A**}) Do
                    writeln("Cacon");
                    Break;
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("a"),[],IntLiteral(2))],[For(Id("index"),CallExpr(Id("foo"),[BinaryOp("*",IntLiteral(3),Id("x"))]),BinaryOp("<",Id("index"),IntLiteral(100)),BinaryOp("+",StringLiteral("String"),ArrayLiteral([StringLiteral("abc"),StringLiteral("a")])),([],[CallStmt(Id("writeln"),[StringLiteral("Cacon")]),Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_50(self):
        input = """
            Function: test
            Parameter: n
            Body:
                While n >0 Do
                    If n==0 Then Break;
                    Else n= toInt(sqrt(n)); 
                    EndIf. 
                EndWhile.
            EndBody.
            """
        expect =Program([FuncDecl(Id("test"),[VarDecl(Id("n"),[],None)],([],[While(BinaryOp(">",Id("n"),IntLiteral(0)),([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Break()])],([],[Assign(Id("n"),CallExpr(Id("toInt"),[CallExpr(Id("sqrt"),[Id("n")])]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_51(self):
        input = """
            Function: sum
            Parameter: lst
            Body:
                func = x+y;
                rs = reduce(func,lst[1],lst[0]);
            EndBody.
            """
        expect =Program([FuncDecl(Id("sum"),[VarDecl(Id("lst"),[],None)],([],[Assign(Id("func"),BinaryOp("+",Id("x"),Id("y"))),Assign(Id("rs"),CallExpr(Id("reduce"),[Id("func"),ArrayCell(Id("lst"),[IntLiteral(1)]),ArrayCell(Id("lst"),[IntLiteral(0)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_52(self):
        input = """ 
            Function: sum
            Parameter: lst
            Body:
                For (i = 0, i<len(sum), i+1) Do
                    rs = rs + sum[i];
                EndFor.
            EndBody.
            """
        expect = Program([FuncDecl(Id("sum"),[VarDecl(Id("lst"),[],None)],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),CallExpr(Id("len"),[Id("sum")])),BinaryOp("+",Id("i"),IntLiteral(1)),([],[Assign(Id("rs"),BinaryOp("+",Id("rs"),ArrayCell(Id("sum"),[Id("i")])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_53(self):
        input = """
            Function:  test
            Parameter: var,x
            Body:
                var = (x - 1)\\2 && True;
            EndBody.
            """       
        expect = Program([FuncDecl(Id("test"),[VarDecl(Id("var"),[],None),VarDecl(Id("x"),[],None)],([],[Assign(Id("var"),BinaryOp("&&",BinaryOp("\\",BinaryOp("-",Id("x"),IntLiteral(1)),IntLiteral(2)),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_54(self):
        input = """
            Function: test 
            Body:
                Var: x = 10, a[10][12][0x12]; 
                var = (x - 1)\\2 && True;
            EndBody.
            """        
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],IntLiteral(10)),VarDecl(Id("a"),[10,12,18],None)],[Assign(Id("var"),BinaryOp("&&",BinaryOp("\\",BinaryOp("-",Id("x"),IntLiteral(1)),IntLiteral(2)),BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_55(self):
        input = """ Function: foo
                        Parameter: x,y[3],z[4][5]
                        Body:
                            z = 5;
                            test(x,y[1],z[2][2],"string",True);
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[3],None),VarDecl(Id("z"),[4,5],None)],([],[Assign(Id("z"),IntLiteral(5)),CallStmt(Id("test"),[Id("x"),ArrayCell(Id("y"),[IntLiteral(1)]),ArrayCell(Id("z"),[IntLiteral(2),IntLiteral(2)]),StringLiteral("string"),BooleanLiteral(True)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_56(self):
        input = """ Function: testCallStatement
                        Parameter: x,y,z
                        Body:
                            If(x > y) Then
                                sub(x,1);
                            Else
                                add(x,2);
                            EndIf.
                        EndBody.
                    """
        expect = Program([FuncDecl(Id("testCallStatement"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[If([(BinaryOp(">",Id("x"),Id("y")),[],[CallStmt(Id("sub"),[Id("x"),IntLiteral(1)])])],([],[CallStmt(Id("add"),[Id("x"),IntLiteral(2)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_57(self):
        input = """ Function: testCallExpr
                        Parameter: x,y,z
                        Body:
                            If bool_of_string("True") Then
                            a = int_of_string (read ());
                            b = float_of_int (a) +. 2.0;
                            EndIf.
                        EndBody.
        """
        #expect = Program([FuncDecl(Id("testCallExpr"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],())]))])
        expect = Program([FuncDecl(Id("testCallExpr"),[VarDecl(Id("x"),[],None),VarDecl(Id("y"),[],None),VarDecl(Id("z"),[],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))])],([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_58(self):
        input = """ Function: testCallStatement
                        Parameter: arg
                        Body:
                            printLn();
                            print(arg);
                            printStrLn(arg);
                            read();
                        EndBody.
        """
        expect = Program([FuncDecl(Id("testCallStatement"),[VarDecl(Id("arg"),[],None)],([],[CallStmt(Id("printLn"),[]),CallStmt(Id("print"),[Id("arg")]),CallStmt(Id("printStrLn"),[Id("arg")]),CallStmt(Id("read"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_59(self):
        input = """ 
                Var: x;
                Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                            a = int_of_string (read ());
                    Else
                            b = float_of_int (a) +. 2.0;
                    EndIf.
                EndBody.
                Function: main
                Body:
                    x = 10;
                    fact (x);
                    printStrLn(arg);
                    read();
                EndBody."""
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])]))])],([],[Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")]),CallStmt(Id("printStrLn"),[Id("arg")]),CallStmt(Id("read"),[])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_60(self):
        input = """ Var: a = 5;
                    Var: b[2][3] = {{2,3,4},{4,5,6}};
                    Var: c, d = 6, e, f;
                    Var: m, n[10];"""
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,399))
    
