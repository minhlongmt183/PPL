import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

    def test_wrong_miss_close(self):
        input = """Var: x ;"""
        expect = " on line 1 col 5: ;"
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_case_3(self):
        """Simple program: int main() {} """
        input = """Var: x;
        Function: main
        Body:
        Return 0;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_case4(self):
        input = """
            Var: x, y; 
            Function: main 
                Parameter: n 
                Body: 
                x = 7;
                If n == 0 Then 
                    Return 1; 
                Else
                    Return n * x;
                EndIf.
                EndBody. 
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_case_5(self):
        input = """
        Var: x, y, z;
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_case_6(self):
        input = """
        Function: foo 
        Parameter: n 
        Body: 
            x = f[n+3];
        EndBody.
        """
        expect = " on line 5 col 16: ["
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_case_7(self):
        input = """
        Var: x = {1,  3,{5  ,  7}};
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_case_8(self):
        input = """
        Var: x[2][3] = {1,  3,{5  ,  7}};
        Function: main
        Body:
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_case_9(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            value = a + 5 *.9;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_case_10(self):
        input = """ 
        Function: foo 
        Parameter: n 
        Body: 
            Var: x = 12;
            value = a + 13 *.9;
        EndBody.
        """
        expect = " on line 6 col 12: Var"
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_case_11(self):
        input = """
        Var: x[10][1 - (5 * 9 + 12 + func(12))];
        Function: main
        Parameter: a, b
        Body:
            Var: i = 0;
            While (i < 10) Do
                i = i + 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_case_12(self):
        """ test empty body function """
        input = """Function: foo 
        Parameter: x,y,z
        Body: 



        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_case_13(self):
        """ test empty body, list parameter function """
        input = """Function: foo 
        Parameter: n, arr[100]
        Body: 

        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_case_14(self):
        """ test return_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            If (n == 0) Then
                Return 1;
            ElseIf n == 1 Then
                Return 1;
            Else
                Return fibo(n-1) + fibo (n - 2);
            EndIf.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_case_15(self):
        """ test return_stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            If (n == 0) Then
                Return 1;
            ElseIf n == 1 Then
                Return 1;
            Else
                Return fibo(n-1) + fibo (n - 2);
            EndIf.
        EndBody."""
        expect = " on line 7 col 23: 1"
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_case_16(self):
        """ test call function """
        input = """Function: foo 
         Parameter: n
         Body: 
             x = 1.e-12412;
             func(x);
         EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_case_17(self):
        """ test call function """
        input = """Function: foo 
         Parameter: n
         Body: 
             x = 1.e-12412;
             func    (x);
         EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_case_18(self):
        """ test call function """
        input = """
        Function: foo
        Parameter: a[10], b
        Body:
            f[3] = 5 == 12 ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_case_19(self):
        input = """
        Function: foo
        Parameter: a[10][34]
        Body:
            f(8 == 4) = foo(foo2(x("hello", "ages", name)));
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_case_20(self):
        input = """
        Function: foo
        Parameter: a[10][34], b
        Body:
            c = f1(111**just comment**) * f(abcd);
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_case_21(self):
        input = """
        Function: main
        Body:
            func = func + ffffffffff(); 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_case_22(self):
        input = """
        Function: main
        Parameter: f
        Body:
            print("Hello World!'"");
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_case_23(self):
        input = """
        Function: main
        Body:
            Var: x;
            writeLn();
            Return;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_case_24(self):
        """ test index operator function """
        input = """Function: foo 
        Parameter: n
        Body: 
            a[10+foo(8)] = x[y[2][n]] + 99;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_case_25(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: a[20];
           a[9 + foo(10, 15)] = a[b[3][0]] + foo();
           Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_case_26(self):
        input = """
        Var: a, b= 1, c = 2;
        Function: helloFunc
        Body:
            Var: hello_msg = "H3ll0 W0rld";
            Return hello_msg;
        EndBody.
        Function: main
        Body:
            print(helloFunc());
            Return;  
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_case_27(self):
        input = """
        Var: a = 0, b = 1, c = 2;
        Function: func
        Body:
            Return "H3ll0 W0rld";
        EndBody.
        Function: main
        Body:
            print(func());
            Return;  
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_case_28(self):
        input = """
        Function: main
        Body:
            Var: x = {121 , 8374598, foo1, foo2};
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_case_29(self):
        input = """
        Function: fibo
        Parameter: a[100], n
        Body:
            Return a[fibo(n)];   
        EndBody.
        Function: main
        Body:
            print(fibo({1,2,3,4,5,121,2143,13,6145,13512}, 6));
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_case_30(self):
        input = """
        Function: main
        Body:
            Var: array[10][10];
            array[3][4] = foo(3. *. 8.0e-12134, a *. b);
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))

    def test_case_31(self):
        input = """
        Function: fibo
        Parameter: a[100], n
        Body:
            Return a[fibo(n)];   
        EndBody.
        Function: main
        Body:
            Var: x;
            print(fibo({1,2,3,4,5,121,2143,13,6145,13512}, 6));
            x = 1423;
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_case_32(self):
        input = """
        Function: fibo
        Parameter: a[100], n
        Body:
            Return a[fibo(n)];   
        EndBody.
        Function: main
        Body:
            print(fibo({6145,13512}, 6));
            x = 1423;
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_case_33(self):
        input = """
        Var: y = {1,2,3};
        Function: main
        Body:
            Var: x;
            print(fibo({1,2,3,4,5,121,2143,13,6145,13512}, 6));
            x = 1423;
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_case_34(self):
        input = """
        Function: main
        Body:
            Var: x;
        Var: y = {0x1,0o112,3};
            print(fibo({1,2,3,4,5,121,2143,13,6145,13512}, 6));
            x = 1423;
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_case_35(self):
        input = """
        Function: main
        Body:
            x = f[20] + 1432;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    def test_case_36(self):
        input = """
        Function: main
        Body:
            x = (123 + f() + g(12, abc*xd-r) *. g[54])[2] *. 5.03e-1232;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_case_37(self):
        input = """
        Function: main
        Body:
            x = y+ 5 == 10+256;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_case_38(self):
        input = """
        Function: main
        Body:
           value[12] =  info("name", "age") + arr[9][6];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_case_39(self):
        input = """        
        Function: foo
        Body:
        Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_case_40(self):
        input = """
        Function: main
        Body:
            Var: x[123741313413];
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_case_41(self):
        """ test do while stmt """
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: x = 0;
            Do
                x= x+1;
            While x < n 
            EndDo.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_case_42(self):
        input = """
        Function: main
        Parameter: n, arr[5][5]
        Body:
            Var: i = 10, arr[5][2] = {{}, {}};
            Do
                Break;
            While i <= n EndDo.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_case_43(self):
        input = """
        Function: foo
        Body:
        Do
            If x == 5 Then
                printLn();
            ElseIf x == 2 Then
                readLn();
            EndIf.
            x= x + 1;
        While x < 100.e-2
        EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_case_44(self):
        input = """
        Function: main
        Body:
            Do
            If x == 5 Then
                printLn();
            ElseIf x == 2 Then
                readLn();
            EndIf.
            x= x + 1;
        While (1)
        EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_case_45(self):
        input = """
        Function: main
        Body:
            Do
                print_Numb3r(12);
                While x Do
                    Var: x;
                    If x == 5 Then
                        printLn();
                    ElseIf x == 2 Then
                        readLn();
                    EndIf.
                    x= x + 1;
                EndWhile.
            While True EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_case_46(self):
        input = """
        Function: foo
        Parameter: arr[10], n
        Body:
            Do
                Var: x = 1;
                For (x = 1, x < n, 0x11) Do
                EndFor.
            While (foo()) EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_case_47(self):
        input = """
        Function: main
        Body:
            Do
                Var: arr[1134][4] = False;
            While True EndDo.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_case_48(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            While x < 100 Do
                If x==n Then Break;
                Else Continue;
                EndIf.
            EndWhile.
            Return;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_case_49(self):
        input = """
        Function: main
        Parameter: d
        Body:
            Var: i = 0;
            While (i < 100) Do
                i = i + 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_case_50(self):
        input = """
        Function: main
        Body:
            Var: x = 1.e-12373, y = 2.34134;
            While (x =/= y) Do
                If x > y Then
                    x = x -. y;
                Else 
                    y = y -. x;
                EndIf.
            EndWhile.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_case_51(self):
        input = """
         Function: main
         Body:
             Var: count = 0;
             Var: x[23];
             While True Do
                 count = count + 1;
                 x[icount] = count;
                 print(count);
             EndWhile.
             Return 0;
         EndBody.
         """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_case_52(self):
        input = """
        Function: main
        Body:
            Var: x = False;
           While x == True Do
           EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_case_53(self):
        input = """
        Function: main
        Parameter: x, y, z
        Body:
            While x == 5 Do
                print(x);
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_case_54(self):
        input = """
        Function: main
        Body:
            While (0o12) Do
                Var: x = 15;
                print("Error on line 4 col 12: While");
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_case_55(self):
        input = """
        Function: main
        Parameter: arr[10], n
        Body:
            Var: i = 0;
            While (i < n) Do
                arr[i] = n +. 5.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_case_56(self):
        input = """
        Function: arry
        Body:
        Var: x = 10;
            While x > 1 Do
                inp = arr[2][fsfsg] + 20 *. 124;
                If inp == 123 Then 
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_case_57(self):
        input = """
        Function: arry
        Body:
        Var: x = 10;
            While x > 1 Do
                inp = a[fsfsg] + 20 *. 124;
                If inp == 123 Then 
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_case_58(self):
        input = """
        Function: main
        Body:
            arr = 1234 * a \ b -.--.- d +. 12.e-123;
            While (print(arr[1]) == 1) Do
                Continue;
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_case_59(self):
        input = """
        Function: arry
        Body:
        Var: x = 10;
            While x > 1 Do
                inp = arr[2][fsfsg] + 20 *. 124;
                If inp == 123 Then 
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_case_60(self):
        input = """
        Function: arry
        Body:
        Var: x = {{1,2,3}, {4,5,**abcd**6}};
            While x > 1 Do
                inp = arr[2][fsfsg] + 20 *. 124;
                If inp == 123 Then 
                    Break;
                EndIf.
            EndWhile.
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_case_61(self):
        input = """
    
        Function: arry
        Body:
            While x > 1 Do
                inp = arr[2][fsfsg] + 20 *. 124;
                If inp == 123 Then 
                    Break;
                EndIf.
            EndWhile.
        EndBody.
    
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_case_62(self):
        input = """
        Var: a = 10;
        Var: b[2][3] = {{1,2,3},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_case_63(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: x = 3, y, i;
            y = (5. \. 6) *. 314.12 *. x *. x *. x;
            For (i = 0, i < y, i ) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_case_64(self):
        input = """
        Function: main
        Body:
            Var: sum = 0;
            For (i = 0, i < 10, i + f(2)) Do
                sum = i *.2;
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_case_65(self):
        input = """
        Function: main
        Body:
            Var: x = 1, y = {1,2}, c = 6.0e-12131;
            Var: sum = 0;
            For (i = 0, i < 10, i + f(2)) Do
                sum = i *.2;
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_case_66(self):
        input = """
        Function: main
        Body:
            Var: i;
            For(i = 0, i < 10, 1) Do
                If i == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_case_67(self):
        input = """
        Function: main
        Body:
            Var: i;
            For(i = 0, i < 10, 1) Do
                If i == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_case_68(self):
        input = """
        Function: main
        Body:
            Var: i;  
            For(i = 0, i < 10, 1) Do
                If i == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_case_69(self):
        input = """
        Function: main
        Parameter: n , m
        Body:
            Var: i;
            For(i = 0, i < n, 1) Do
                If i == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_case_70(self):
        input = """
        Function: main
        Parameter: n , a, b, c, d, e, f
        Body:
            Var: i;  
            For(i = 0, i < n, 1) Do
                If i == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_case_71(self):
        input = """
        Function: main
        Body:
            For(i=0, i < n, 2) Do
                foo();
            EndFor.
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_case_72(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            For(i = 0, i[0] < i[4], 1) Do
                If i[2] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_case_73(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            For(j = 0, j < 5, 1) Do
                If i[j] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_case_74(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            For(i = 0, i <= 100 , i+1  ) Do
                If i[j] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_case_75(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            For(j = 0, j < 5, 1) Do
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_case_76(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            For(j = 0, j < 5, j == 1) Do
                print(i);
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_case_77(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            For(j = 0., foo1() * i[23] == 2, "writeSomething") Do
                print(i);
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_case_78(self):
        input = """
         Function: main
         Body:
             Var: i[5]={1,2,3,4};
             Var: j = 0;
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                bool_value =  (arr)[i];
             EndFor.  
             Return 0;
         EndBody.
         """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_case_79(self):
        input = """
         Function: main
         Body:
             Var: i[5]={1,2,3,4};
             Var: j = 0;
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                bool_value =  (arr)[i][i][i];
             EndFor.  
             Return 0;
         EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_case_80(self):
        input = """
         Function: main
         Body:
             Var: i[5]={1,2,3,4};
             Var: j = 4;
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                bool_value =  (arr)[i][i][i];
             EndFor.  
             Return 0;
         EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_case_81(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[j] == 10 Then
                    Break;
                ElseIf i[0] == 9 Then
                    Return 1;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_case_82(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            i[0] = foo(f1(0))[4][5];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[j] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_case_83(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            i[0] = foo(f1(0))[45];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[jj] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_case_84(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 5;
            i[0] = foo(f1(0))[45];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[1] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_case_85(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[j] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_case_86(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[j] == 10 Then
                    Break;
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_case_87(self):
        input = """
        Function: main
        Body:
            Var: i[5]={1,2,3,4};
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
             For(j = "1", foo1() * i[2] == 2, "writeSomething") Do
                If i[j] == 10 Then
                Else
                    Continue;
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_case_88(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]={1,2,3,4};
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
            Return ;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_case_89(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]={1,2,3,4};
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_case_90(self):
        input = """
        Function: main
        Body:
            Var: x = 12, y = 16;
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_case_91(self):
        input = """
        Var: x;
        Function: main
     
        Body:
            Var: x = 3, y, i;
            y = (5. \. 6) *. 314.12 *. x *. x *. x;
            For (i = 0, i < y, i ) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_case_92(self):
        input = """
        Function: foo
        Body:
            print("Hello");
        EndBody.

        Function: main
        Body:
            Var: j = 0;
            j = "3" + "1";
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_case_93(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]={1,2,3,4};
            Var: j = 0;
            Var: x = {{{113,  23 ,4.3123e-12414, "hello" , 114 }, {  hello , **functions**  5}  },  {{ 6   ,  7  }}};
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_case_94(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]=0x56124;
            Var: j = 0;
            j = "3" + "1";
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test95(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            If (x == y) || (x =/= y) Then
                x = ((n <=. 3e-173) && (x == 27e-375));
            EndIf.
            bool = (x < n) && (y > n);
            value = (x - z);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test96(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: x[4] = {1,2,3,4};
            If (x == y) || (x =/= y) Then
                x = ((n <=. 4.3e-173) && (x == 27e-375));
            EndIf.
            bool = (x < n) && (y > n);
            value = (x - z);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test97(self):
        input = """Function: foo 
        Parameter: n
        Body: 
            Var: x[4] = {};
            Var: y[7][7] = {{{}}};
            If (x == y) || (x =/= y) Then
                x = ((n <=. 4.3e-173) && (x == 27e-375));
            EndIf.
            bool = (x < n) && (y > n);
            value = (x - z);
        EndBody."""
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_case_98(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]={1,2,3,4};
            Var: j = 0;
            i = {1,2,3} + {4,5,6};
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_case_99(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]="function";
            Var: j = 0;
            i = {1,2,3} + {4,5,6};
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_case_100(self):
        input = """
        Function: main
        Body:
            Var: i[0o65]={1,2,3,4};
            Var: j = 0;
            i = {} + {} * "function";
            i[0] = foo(f1(0))[4][5];
            Return 0;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))









