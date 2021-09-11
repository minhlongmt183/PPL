import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def testcase_undeclared_function(self):
        """Simple program: main"""
        input = r"""Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def testcase_diff_numofparam_stmt(self):
        """Complex program"""
        input = r"""Function: main  
                   Body:
                        printStrLn();
                    EndBody."""
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def testcase_diff_numofparam_expr(self):
        """More complex program"""
        input = r"""Function: main 
                    Body:
                        printStrLn(read(4));
                    EndBody."""
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def testcase_undeclared_function_use_ast(self):
        """Simple program: main """
        input = Program([FuncDecl(Id("main"), [], ([], [
            CallExpr(Id("foo"), [])]))])
        expect = str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def testcase_diff_numofparam_expr_use_ast(self):
        """More complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [
                    CallExpr(Id("read"), [IntLiteral(4)])
                ])]))])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"), [IntLiteral(4)])))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def testcase_diff_numofparam_stmt_use_ast(self):
        """Complex program"""
        input = Program([
            FuncDecl(Id("main"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def testcase_6(self):
        """test case description """
        input = r"""
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 406))

    def testcase_7(self):
        """test case description """
        input = r"""
            Var: x;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 407))

    def testcase_8(self):
        """test case description """
        input = r"""
            Var: x,y;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 408))

    def testcase_9(self):
        """test case description """
        input = r"""
            Var:x,y,z,t,f;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 409))

    def testcase_10(self):
        """test case description """
        input = r"""
            Var: x=5,y,z,t,f;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 410))

    def testcase_11(self):
        """test case description """
        input = r"""
            Var: x=5,y=5e-1,z,t,f;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 411))

    def testcase_12(self):
        """test case description """
        input = r"""
            Var: x=5,y=5e-1,z=True,t,f;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 412))

    def testcase_13(self):
        """test case description """
        input = r"""
            Var: x=0o234,y=7e-1,z=True,t="askdaksldalpoqwe\\n\\tasdlasd",f;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 413))


    def testcase_15(self):
        """test case description """
        input = r"""
            Var: x[738];
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 415))

    
    

    def testcase_16(self):
        """test case description """
        input = r"""
            Var: x[10], y = 10, z =1., t = "12315";
            Function: main
            Parameter: a
            Body:
                Return 1;

            EndBody.
            """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 416))

    def testcase_17(self):
        """test case description """
        input = r"""
            Var: x[10], y = 10, z =1., t = "784";
            Function: main
            Parameter: x
            Body:
                Return 1;
            EndBody.
            """[1:-1]   
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 417))

    def testcase_18(self):
        """test case description """
        input = r"""
            Var: x[10], y = 10, z =1., t = "13141341234";
            Function: main
            Parameter: a
            Body:
                Var: b;
                Return 1;
            EndBody.
            """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 418))

    def testcase_19(self):
        """test case description """
        input = r"""
            Var: x[10], y = 10, z =1., t = "31233";
            Function: main
            Parameter: a
            Body:
                Var: b;
                a = x[1];
                a = 1+ 1+ 1;

                Return 1;
            EndBody.
            """[1:-1]
        expect = str(TypeCannotBeInferred(
            stmt=Assign(lhs=Id(name='a'), rhs=ArrayCell(arr=Id(name='x'), idx=[IntLiteral(value=1)]))))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def testcase_20(self):
        """test case description """
        input = r"""
            Var: x[10], y = 10, z =1., t = "12313";
            Function: main
            Parameter: a
            Body:
                Var: b;
                a = 1+ 1+ 1;
                a = x[1];
                Return 1;
            EndBody.
            """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 420))

    def testcase_21(self):
        """test case description """
        input = r"""
            Var: x;
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 421))

    def testcase_22(self):
        """test case description """
        input = r"""
        Var: x[1234][456];
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 422))

    def testcase_23(self):
        """test case description """
        input = r"""
            Var: x ,y = "hkjsdhkjadsfad adshcasd c\\f";
            """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 423))

    def testcase_24(self):
        """test case description """
        input = r"""
        Function: test
        Body:
        Break;
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 424))

    def testcase_25(self):
        """test case description """
        input = r"""
        Function: test
        Body:
        Continue;
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 425))

    

    def testcase_26(self):
        """test case description
        """
        input = r"""
        Var: x,a,a;
        """[1:-1]
        expect = str(Redeclared(k=Variable(), n='a'))
        self.assertTrue(TestChecker.test(input, expect, 426))

    def testcase_27(self):
        input = r"""
        Function: func
        Body:
        EndBody.
        Function: main
        Body:
            Var: x = 5;
            x = func();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(Assign(Id('x'),CallExpr(Id('func'),[]))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def testcase_28(self):
        input = r"""
        Function: main
        Body:
            Var: x;
            x = test();
        EndBody.
        Function: test
        Body:
            Return 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('x'),CallExpr(Id('test'),[]))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def testcase_29(self):
        input = r"""
        Var: arr1[10][10];
        Function: main
        Parameter: param
        Body:
            f("s")[2][3] = 500;
            If f("a")[0][1] == foo()[1][2] Then
                f(param)[1][3] = 0o10;
            EndIf.
            param = 12;
        EndBody.
        Function: f
        Parameter: x
        Body:
            Return foo();
        EndBody.
        Function: foo
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id('f'),[StringLiteral("""s""")])))
        self.assertTrue(TestChecker.test(input,expect,429))

    

    def testcase_30(self):
        input = r"""
        Var: x,a;
        Var: a,x;
        """[1:-1]
        expect = str(Redeclared(k=Variable(), n='a'))
        self.assertTrue(TestChecker.test(input, expect, 430))


    def testcase_31(self):
        input = r"""
        Var: x,a, x[5][2];
        """[1:-1]
        expect = str(Redeclared(k=Variable(), n='x'))
        self.assertTrue(TestChecker.test(input, expect, 431))

    def testcase_32(self):
        input = r"""
        Var: x;
        Function: main
        Parameter: x
        Body:
            Return;
        EndBody.
        """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 432))

    def testcase_33(self):
        input = r"""
        Var: x;
        Function: main
        Parameter: x ,y
        Body:
            Return;
        EndBody.

        Function: main
        Parameter: x ,y
        Body:
            Return;
        EndBody.
        """[1:-1]
        expect = str(Redeclared(k=Function(), n='main'))
        self.assertTrue(TestChecker.test(input, expect, 433))


    def testcase_34(self):
        input = r"""
        Function: main
        Parameter: x
        Body:
            foo(foo());
            Return;
        EndBody.

        Function: foo
        Body:
            Return;
        EndBody.
        """[1:-1]
        expect = str(TypeMismatchInStatement(
            stmt=CallStmt(method=Id(name='foo'), param=[CallExpr(method=Id(name='foo'), param=[])])))
        self.assertTrue(TestChecker.test(input, expect, 434))


    def testcase_35(self):
        input = r"""
        Function: main
        Parameter: x
        Body:
            x = foo(foo());
            Return;
        EndBody.

        Function: foo
        Body:
            Return;
        EndBody.
        """[1:-1]
        expect = str(TypeMismatchInExpression(
            exp=CallExpr(method=Id(name='foo'), param=[CallExpr(method=Id(name='foo'), param=[])])))
        self.assertTrue(TestChecker.test(input, expect, 435))

    def testcase_36(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,436))


    def testcase_37(self):
        input = r"""
        Var: x,y;
        Function: testcase
        Parameter: a,b
        Body:
            If x == b Then  x = y;
            ElseIf a == b Then Var: x; x = y;
            Else Var: x; x = y;
            EndIf.
            Return x;
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 437))


    def testcase_38(self):
        input = r"""
        Function: power
        Parameter: value ,power
        Body:
            Var: res =1, i;
            For (i=power,i>0,-1) Do
                res = res * value;
            EndFor.
            Return res;
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 438))

    def testcase_39(self):
        """test case description """
        input = r"""
        Function: foo
        Parameter: n1,n2
        Body:
            If n2==0 Then Return --n1;
            Else Return foo(n2,n1%n2);
            EndIf.
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 439))

    def testcase_40(self):
        input = r"""
        Function: sum
        Parameter: x
        Body:
            If x < 0 Then Return --x;
            Else Return x;
            EndIf.
            Return x;
        EndBody.

        Function: check
        Parameter: board[8],index
        Body:
            Var: i;
                For (i=0,i<index,1) Do
                    If (i!=index) && (sum(i-index) == sum(board[i]-board[index])) Then
                        Return True;
                    ElseIf i ==-1 Then Return False;
                    EndIf.
                EndFor.

            Return False;
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 440))
    def testcase_41(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        Function: test
        Parameter: x
        Body:
            x = 1;
            test(1.4);
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'),[FloatLiteral(1.4)])))
        self.assertTrue(TestChecker.test(input,expect,441))
    

    def testcase_42(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,442))

    def testcase_43(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,443))


    def testcase_44(self):
        input = r"""
        Function: main
        Body:
            Var: main;
            main();
        EndBody.
        """
        expect = str(TypeMismatchInStatement(CallStmt(Id('main'),[])))
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def testcase_45(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,445))

    def testcase_46(self):
        input = r"""
        Var: arr1[10];
        Function: main
        Body:
            test()[0] = 1;
            test()[1] = "s";
        EndBody.
        Function: test
        Body:
            Return x;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(ArrayCell(CallExpr(Id('test'),[]),[IntLiteral(0)]),IntLiteral(1))))
        self.assertTrue(TestChecker.test(input,expect,446))
    def testcase_47(self):
        input = r"""
        Function: init
        Parameter: param
        Body:
            If param > 0 Then
                Var : board[1000];
                Var: i;
                For (i=0,i<param,1) Do
                    board[i]=-1;
                EndFor.
                Return board;
            EndIf.
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 447))

    def testcase_48(self):
        input = r"""
        Var: x[20];
        Function: main
        Body:
        While x[1] && ! x[2] Do
            Do
                Var: x;
                x = 1;
            While x[1] EndDo.
        EndWhile.
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 448))

    def testcase_49(self):
        input = r"""
        Function: main
        Body:
            Var: x;
            x = foo()[x];

        EndBody.


        Function:foo
        Body:
            Return {1,2,3,4,5};
        EndBody.
        """[1:-1]
        expect = str(TypeCannotBeInferred(stmt=Assign(lhs=Id(name='x'),
                                                      rhs=ArrayCell(arr=CallExpr(method=Id(name='foo'), param=[]),
                                                                    idx=[Id(name='x')]))))
        self.assertTrue(TestChecker.test(input, expect, 449))
    def testcase_50(self):
        input = r"""
        Function: foo
        Body:
            Return False;
        EndBody.

        Function: main
        Body:
            Return 1;
            Return int_of_float(43.e5233);
            Return foo();
            Return False;
        EndBody.

        """[1:-1]
        expect = str(TypeMismatchInStatement(stmt=Return(expr=CallExpr(method=Id(name='foo'), param=[]))))
        self.assertTrue(TestChecker.test(input, expect, 450))

    def testcase_51(self):
        input = r"""
        Var: x[10], y;
        Function: main
        Body:
            x[1] = y;
            Return x;
        EndBody.
        """[1:-1]
        expect = str(TypeCannotBeInferred(
            stmt=Assign(lhs=ArrayCell(arr=Id(name='x'), idx=[IntLiteral(value=1)]), rhs=Id(name='y'))))
        self.assertTrue(TestChecker.test(input, expect, 451))
    def testcase_52(self):
        input = r"""
        Var: x[10], y;
        Function: foo
        Body:
            x[1] = !y;
            Return x;
        EndBody.

        Function: main
        Body:
            x[8] = foo()[1];
            Return y && x;
        EndBody.
        """[1:-1]
        expect = str(TypeMismatchInExpression(exp=BinaryOp(op='&&', left=Id(name='y'), right=Id(name='x'))))
        self.assertTrue(TestChecker.test(input, expect, 452))
    def testcase_53(self):
        input = r"""
        Function: funct
        Body:
            printLn();
        EndBody.

        Function: while
        Body:
        Var: i;
        While i < 12345 Do
            funct();
        EndWhile.
        EndBody.
        """[1:-1]
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 453))

    def testcase_54(self):
        input = r"""
        Function: main
        Body:
            Var: x,y,z;
            If x Then
                y = "55555";
            ElseIf !x Then
                z = True;
            ElseIf z Then
            EndIf.
            Return y;
        EndBody.
        """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 454))
    def testcase_55(self):
        input = r"""
        Function: main
        Body:
            Var: x,y,z;
            If x Then
                y = "7384";
            ElseIf !x Then
                z = True;
            ElseIf z Then
                Var: d;
                For (d = 0x738, !z, 1100) Do
                    d = int_of_string(y);
                EndFor.
            EndIf.
            Return y;
        EndBody.
        """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 455))
    def testcase_56(self):
        input = r"""
        Function: main
        Body:
            Var: x,y,z,f, arr[5];
            If x Then
                y = "7384";
            ElseIf !x Then
                z = True;
            ElseIf z Then
                Var: d;
                For (d = 0x738, !z, 1100) Do
                    d = int_of_string(y);
                    While f <. 1.12 Do
                        Var: t;
                        z = !z;
                        arr[1] = -t;
                        Do
                            Var: n;
                            n = t;
                        While z EndDo.
                    EndWhile.
                EndFor.
            EndIf.
            Return n;
        EndBody.
        """[1:-1]
        expect = str(Undeclared(k=Identifier(), n='n'))
        self.assertTrue(TestChecker.test(input, expect, 456))

    def testcase_57(self):
        input = r"""
        Function: main
        Body:
            Var: x,y,z;
        EndBody.

        Function: x
        Body:
        EndBody.
        """[1:-1]
        expect = str()
        self.assertTrue(TestChecker.test(input, expect, 457))

    def testcase_58(self):
        input = r"""
        Function: main
        Body:
            Var: x, y;
            x = y;
            Return;
        EndBody.
        """[1:-1]
        expect = str(TypeCannotBeInferred(stmt=Assign(lhs=Id(name='x'), rhs=Id(name='y'))))
        self.assertTrue(TestChecker.test(input, expect, 458))

    def testcase_59(self):
        input = r"""
        Function: main
        Body:
            Var: x,y,z;
            x = (x && y) && False || (z > 3);
            z = x;
            Return;
        EndBody.
        """[1:-1]
        expect = str(TypeMismatchInStatement(stmt=Assign(lhs=Id(name='z'), rhs=Id(name='x'))))
        self.assertTrue(TestChecker.test(input, expect, 459))
    def testcase_60(self):
        input = r"""
        Function: main
        Parameter: x
        Body:
            x = (x + 3) * (x - 2.1);
            Return;
        EndBody.
        """[1:-1]
        expect = str(TypeMismatchInExpression(exp=BinaryOp(op='-', left=Id(name='x'), right=FloatLiteral(value=2.1))))
        self.assertTrue(TestChecker.test(input, expect, 460))

    def testcase_61(self):
        input = r"""
        Var: arr1[10];
        Function: main
        Body:
        EndBody.
        Function: test
        Body:
            Var: x, y;
            If foo()[1] Then
                Return 1;
            EndIf.
            Return y;
        EndBody.
        Function: foo
        Body:
            Return 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),[],[Return(IntLiteral(1))])], ([],[]))))
        self.assertTrue(TestChecker.test(input,expect,461))

    def testcase_63(self):
        input = r"""
        Var: arr1[10];
        Function: test
        Parameter: y
        Body:
            Var: x;
            If foo()[1] Then
                Return 1;
            ElseIf f(1) Then
            EndIf.
            Return y;
        EndBody.
        Function: main
        Body:
            Var: k;
            k = test(1.5);
        EndBody.
        Function: foo
        Body:
            Return {True, False, True};
        EndBody.
        Function: f
        Parameter: k
        Body:
            Return k == 1;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(If([(ArrayCell(CallExpr(Id('foo'),[]),[IntLiteral(1)]),[],[Return(IntLiteral(1))]),(CallExpr(Id('f'),[IntLiteral(1)]),[],[])], ([],[]))))
        self.assertTrue(TestChecker.test(input,expect,463))
  
    def testcase_64(self):
        input = r"""
        Function: main
        Body:
            Var: a, b, c;
            Var: x, y, b;
        EndBody.
        """
        expect = str(Redeclared(Variable(), 'b'))
        self.assertTrue(TestChecker.test(input,expect,464))

    def testcase_65(self):
        input = r"""
        Function: main
        Body:
            Var: a, b, c;
            Var: x, y, z;
            Var: g, h, y[2];
        EndBody.
        """
        expect = str(Redeclared(Variable(), 'y'))
        self.assertTrue(TestChecker.test(input,expect,465))

    def testcase_66(self):
        input = r"""
        Function: main
        Body:
            Var: a, b, c;
            Var: x, y, z;
            Var: g, h, t[2];
        EndBody.

        Function: main
        Body:
        EndBody.
        """
        expect = str(Redeclared(Function(), 'main'))
        self.assertTrue(TestChecker.test(input,expect,466))
    def testcase_67(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,467))

    def testcase_68(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,468))

    def testcase_69(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,469))

    def testcase_70(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,470))

    def testcase_71(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,471))

    def testcase_72(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,472))

    def testcase_73(self):
        input = r"""
        Function: main
        Body:
        EndBody.
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,473))

    

    def testcase_74(self):
        input = r"""
        Function: main
        Body:
            Var: a, b;
            a = b;
        EndBody.
        """
        expect = str(TypeCannotBeInferred(Assign(Id('a'), Id('b'))))
        self.assertTrue(TestChecker.test(input,expect,474))

   

    def testcase_75(self):
        input = r"""
        Function: main
        Body:
            Var: i;
            Do
                printLn();
            While i > 20 EndDo.
            i = 22 + i;
            b = i;
        EndBody.
        """
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input,expect,475))

   
    def testcase_76(self):
        input = r"""
        Function: main
        Body:
            foo();
        EndBody.
        """
        expect = str(Undeclared(Function(), 'foo'))
        self.assertTrue(TestChecker.test(input,expect,76))

    def testcase_77(self):
        input = r"""
        Function: main
        Body:
            Var: a, b, c, a;
        EndBody.
        """
        expect = str(Redeclared(Variable(), 'a'))
        self.assertTrue(TestChecker.test(input,expect,477))



