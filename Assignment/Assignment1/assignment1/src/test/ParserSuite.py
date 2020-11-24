import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;
        Function: main
        Body:
        Return 0;
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """
            Var: m, n[10]; 
            Function: main 

                Parameter: n 
                Body: 
                x = {{{1,2}, {3,4}}, {5,6}};
                If n == 0 Then 
                    Return 1; 
                Else
                    Return n * face({1,2});
                EndIf.
                EndBody. 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_case_3(self):
        input = """
        Var: x;
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 202))

    def test_case_4(self):
        input = """
        Var: x = {1,2,{2};
        Function: main
        Body:
        Return;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 25: ;", 203))

    def test_case_5(self):
        input = """
        Function: main
        Body:
            Var
            Return;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: Return", 204))

    def test_case_6(self):
        input = """
        Function: main
        Body:
            printLn();
            Var: x;
            Return;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: Var", 205))

    def test_case_6(self):
        input = """
        Function: main
        Body:
            If x == 1 Then
            Else
            Else EndIf.
            Return;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 12: Else", 206))

    def test_case_7(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: r = 10., v, i;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 206))

    def test_case_8(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: m;
           x = m = 10;
           Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 17: =", 207))

    def test_case_9(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: m;
           x = m = 10;
           Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 17: =", 207))

    def test_case_9(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: a[10];
           a[3 + foo(2)] = a[b[2][3]] + 3;
           Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 208))

    def test_case_10(self):
        input = """
        Var: x;
        Function: main
        Body:
           Var: a[10];
           a[3 + foo(2)] = a[b[2][3]] + 3;
           Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 209))

    def test_case_11(self):
        input = """
        Function: main
        Parameter:
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[0] = b +. 1.0;
                i = i + 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 8: Body", 210))

    def test_case_12(self):
        input = """
        Var: x[3][3 * (4 + f(2) - 4)];
        Function: main
        Parameter: k
        Body:
            Var: i = 0;
            While (i < 5) Do
                a[0] = b +. 1.0;
                i = i + 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 20: *", 211))

    def test_case_13(self):
        input = """
        Function: main
        Parameter: k
        Body:
            Var: i = 10, k[10][2] = {{}, {}};
            Do
                Break;
            While i <= 10 EndDo.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 212))

    def test_case_14(self):
        input = """
        Function: main
        Body:
            Var: s = 0;
            For (i = 0, i < 10, f(2)) Do
                s += i *. 2;
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 18: +", 213))

    def test_case_15(self):
        input = """
        Var: a, b, c = 10 + 2 * 4;
        Function: main
        Body:
            Var: i = 0, arr[10];
            c = arr[0];
            For (i = 1, i < 10, 1) Do
                If (c < arr[i]) Then
                    c = arr[i];
                EndIf.
            EndFor.  
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 26: +", 214))

    def test_case_16(self):
        input = """
        Var: a, b, c = 10;
        Function: func
        Body:
            Return "Hello World";
        EndBody.
        Function: main
        Body:
            print(func());
            Return;  
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 215))

    def test_case_17(self):
        input = """
        Var: a, b, c = 2;
        Function: func
        Body:
            Return "Hello World" 1967;
        EndBody.
        Function: main
        Body:
            print(func());
            Return;  
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 33: 1967", 216))

    def test_case_18(self):
        input = """
        Function: main
        Body:
            Var: i;
            For(i = 0, i < 10, 1) Do
                Continue i;
            EndFor.  
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 25: i", 217))

    def test_case_19(self):
        input = """
        Function: main
        Body:
            For(i = 0, i < 10, 1) Do
                Continue;
            EndFor.
            Var: i;  
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 12: Var", 218))

    def test_case_20(self):
        input = """
        Function: main
        Parameter: n = 10
        Body:
            Var: i;
            For(i = 0, i < 10, 1) Do
                Continue;
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 21: =", 219))

    def test_case_21(self):
        input = """
        Function: main
        Parameter: n m i k u
        Body:
            Var: i;
            For(i = 0, i < 10, 1) Do
                Continue;
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 21: m", 220))

    def test_case_22(self):
        input = """
        Function: main
        Body:
            Var: x = {2 + 1, foo(2), fact(4)};
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 24: +", 221))

    def test_case_23(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i == 10 Then
            Else
                print(i);
            ElseIf i == 2 Then
                Break;
            EndIf.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 12: ElseIf", 222))

    def test_case_24(self):
        input = """
        Function: main
        Body:
            Var: i;
            If i == 10 Then
            Else
                print(i);
            ElseIf i == 2 Then
                Break;
            EndIf.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 12: ElseIf", 223))

    def test_case_25(self):
        input = """
        Function: main
        Body:
            Var: x = 0., y = 2.;
            While (x =/= y) Do
                x = x +. 1;
                y = y -. 1;
            EndWhile.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 224))

    def test_case_26(self):
        input = """
        Function: main
        Body:
            Var: i = 0;
            For (i, i < 10, 2) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 18: ,", 225))

    def test_case_27(self):
        input = """
        Function: main
        Body:
            Var: i[10] = {0};
            For (i[0] = 12, i < 10, 2) Do
                writeln(i);
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 18: [", 226))

    def test_case_28(self):
        input = """
        Function: main
        Body:
            Var: i[10] = {0};
            Var: j;
            For(j = 0, j < 10, 2) Do
                Break j;
            EndFor.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 22: j", 227))

    def test_case_29(self):
        input = """
        Function: find_max
        Parameter: a[10]
        Body:
            Return a[random(0, 10, False)];   
        EndBody.
        Function: main
        Body:
            print(find_max({1,2,3,4,5,6,7,8,9,10}));
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 228))

    def test_case_30(self):
        input = """
        Function: main
        Body:
            Var: x[10];
            x[0] = fact(f(0))[0][4][123];
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 229))

    def test_case_31(self):
        input = """
        Function: main
        Body:
            Var: x[10];
            x[0, 1] = fact(f(0))[0][4][123];
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 15: ,", 230))

    def test_case_32(self):
        input = """
        Function: main
        Body:
            Var: x[10, 15];
            Var: count = 0;
            While True Do
                count = count + 1;
                print(count);
            EndWhile.
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 21: ,", 231))

    def test_case_33(self):
        input = """
        Function: main
        Body:
            Var: x[[10]][10]];
            goo(2. +. 4., 2 *. 10);
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: [", 232))

    def test_case_34(self):
        input = """
        Function: main
        Body:
            Var: x[[10]][10]];
            goo(2. +. 4., 2 *. 10);
            Return 0;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: [", 233))

    def test_case_35(self):
        input = """
        Function: main
        Body:
            Var: x = 10;
            goo(2. +. 4., 2 *. 10)
            x = 1;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 12: x", 234))

    def test_case_36(self):
        input = """
        Function: main
        Body:
            Var: x = 10;
            goo(2. +. 4., 2 *. 10);
            x = 1;
        EndBody.
        Var: x;
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 8 col 8: Var", 235))

    def test_case_37(self):
        input = "Function: main Body: EndBody."
        self.assertTrue(TestParser.checkParser(input, "successful", 236))

    def test_case_38(self):
        input = """
        Function: main
        Body:
            x = 5[10] + 4;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 17: [", 237))

    def test_case_39(self):
        input = """
        Function: main
        Body:
            x = (5 + f() * 3 + a[10])[2] * 5 \\ 8;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 37: [", 238))

    def test_case_40(self):
        input = """
        Function: main
        Body:
            x = (x)[2] * 5 \\ 8;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: [", 239))

    def test_case_41(self):
        input = """
        Function: main
        Body:
            Var: x = 10;
            While x < 100 Do
                print("string, hala madrid");
            EndWhile.
            If x == 10 Then
            ElseIf x < 1 Then EndIf.
            Var: kk = 12;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 10 col 12: Var", 240))

    def test_case_42(self):
        input = """
        Function: main
        Body:
            x = 9 == 20 == 6;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 24: ==", 241))

    def test_case_43(self):
        input = """
        Function: main
        Body:
            x = "1" + "1";
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 242))

    def test_case_44(self):
        input = """
        Function: main
        Body:
           x =  f("1", "194") + a[0][3] * "blu bla";
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 243))

    def test_case_45(self):
        input = """
        Function: main
        Body:
           While x == 1
           EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 11: EndWhile", 244))

    def test_case_46(self):
        input = """
        Var: x;
        Return 0;
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 8: Return", 245))

    def test_case_47(self):
        input = """
        Var: x;
        Return 0;
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 8: Return", 246))

    def test_case_48(self):
        input = """
        Var: x;
        Function: main
        Body:
            Return 1 + 2, "x";
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 24: ,", 247))

    def test_case_48(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: v;
            v = If x == 1 ElseIf x == 2 EndIf;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 16: If", 247))

    def test_case_49(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: v;
            v = If x == 1 ElseIf x == 2 EndIf;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 16: If", 248))

    def test_case_50(self):
        input = """
        Var: x;
        Function: main
        Body:
            Var: x = 5 While x EndWhile.;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 23: While", 249))

    def test_case_51(self):
        input = """
        Var: x;
        Do
            If x == 1
            ElseIf x == 2
            EndIf.
        While x == 2
        EndDo.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 8: Do", 250))

    def test_case_52(self):
        input = """
        Function: main
        Body:
            Parameter: x
            While x
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 12: Parameter", 251))

    def test_case_53(self):
        input = """
        Function: main
        Body:
            For(,,) Do
            EndFor.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 16: ,", 252))

    def test_case_54(self):
        input = """
        Function: main
        Body:
            While () Do
                print("lalala");
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: )", 253))

    def test_case_55(self):
        input = """
        Function: main
        Body:
            Do
                f_n_f(12);
            While () EndDo.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 19: )", 254))

    def test_case_56(self):
        input = """
        Function: main
        Body:
            Do
                f_n_f(12);
                While x Do
                    Var: x;
                    If x == 1 Then
                        Var: x;
                    EndIf.
                EndWhile.
            While True EndDo.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 255))

    def test_case_57(self):
        input = """
        Function: main
        Body:
            Var: x[124.3123];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: 124.3123", 256))

    def test_case_58(self):
        input = """
        Function: main
        Body:
            Var: x[0X734725];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 257))

    def test_case_59(self):
        input = """
        Function: main
        Body:
            Var: x[0O734725];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 258))

    def test_case_60(self):
        input = """
        Function: main
        Body:
            Return Break;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: Break", 259))

    def test_case_61(self):
        input = """
        Function: main
        Body:
            Var: Continue = 19, If = 22;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 17: Continue", 260))

    def test_case_62(self):
        input = """
        Function: main
        Body:
            If ((x = 2) == 1)
            ElseIf x == True
            EndIf.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: =", 261))

    def test_case_63(self):
        input = """
        Function: main
        Body:
            v = 4. *. 3 \\. e * Return();
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 31: Return", 262))

    def test_case_64(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While (i < 5)
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 16: a", 263))

    def test_case_65(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            f(1 >=. 4 == 12 < 4 + 5 *.);
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 22: ==", 264))

    def test_case_66(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Do
                Var: x = 1;
                For (x = 1; x < 10, 1)
                EndFor.
            While (foo) EndDo.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 7 col 26: ;", 265))

    def test_case_67(self):
        input = """
        Function: fo
        Parameter: a[5], b
        Body:
            Elseif Then
                x = 10;
                y = x * 10 - y + 10;
            EndIf.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: Else", 266))

    def test_case_68(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: x[123][1][4] = True;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 267))

    def test_case_69(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            f(1 >=. 4) + g(f(a("a", "af")));
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 23: +", 268))

    def test_case_70(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            c = count(**DDDDDD**) * f(214);;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 43: ;", 269))

    def test_case_71(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            c = "akf"[0] + x[{1,2, 4}];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 21: [", 270))

    def test_case_72(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            For (i = 0, i < 10, i = 2)
                print(i);
            EndFor.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 34: =", 271))

    def test_case_73(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            a = {12, 4} * "ad" + 14 ----. 12 + !!!!!!!!!!!!(!!3);
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 272))

    def test_case_74(self):
        input = """
        Parameter: a[5], b
        Function: foo
        Body:
            a = {12, 4} * "ad" + 14;
            b = ---asd + 2144 + 4.a;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 2 col 8: Parameter", 273))

    def test_case_75(self):
        input = """
        ** import test **
        ** test.test(f = 2) -> failure **
        Function: foo
        Parameter: a[5]["b" - 97]
        Body:
            a = {12, 4}["b"]
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 24: b", 274))

    def test_case_76(self):
        input = """
        Function: main
        Body:
            For(counter = 0., foo() * a[23] == 2, "asd") Do
                x = 213;
            EndFor.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 275))

    def test_case_77(self):
        input = """
        Function: main
        Body:
            f = f * ffffffff([]); 
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 29: [", 276))

    def test_case_78(self):
        input = """
        Function: main
        Body:
            kk = 123;
            123 = kk;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 12: 123", 277))

    def test_case_79(self):
        input = """
        Function: main
        Parameter: f(f(f(f())))
        Body:
            print("Hello'"");
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 3 col 20: (", 278))

    def test_case_80(self):
        input = """
        Function: main
        Parameter: none
        Body:
            print({1, 2, 3, 4}[{1, 2, 3,}]);
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 30: [", 279))

    def test_case_81(self):
        input = """
        Function: main
        Body:
            print() = 1234 || False + 22222;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 20: =", 280))

    def test_case_82(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = ----1234 || +++++++False + -+-+ 22222;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 28: +", 281))

    def test_case_83(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = {{{{}}}, {123}};
        EndBody.
        Function: ff2
        Body:
            ;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 9 col 12: ;", 282))

    def test_case_84(self):
        input = """
        Function: main
        Body:
            Var: a;
            a = "123" * "123" , - 2 == "sss";
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 30: ,", 283))

    def test_case_85(self):
        input = """
        Function: main
        Body:
            Function: foo
            Body:
                main = foo();
            EndBody.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 12: Function", 284))

    def test_case_86(self):
        input = """
        Function: main
        Body:
            Parameter: ddd
            If add Then 
            ElseIf
            EndIf.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 12: Parameter", 285))

    def test_case_87(self):
        input = """
        Function: main
        Body:
            class.class = class || False * 123 - 234 + 34 \\ 123;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 17: .", 286))

    def test_case_88(self):
        input = """
        Function: main
        Parameter: 
        Body:
            inp = 123 * daf[g132[423][2] * 132 + {13}];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 8: Body", 287))

    def test_case_89(self):
        input = """
        Function: main
        Parameter: x
        Body:
            x = "adf" * {q23, 4, "af"}[Return 45;];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 25: q23", 288))

    def test_case_90(self):
        input = """
        Function: main
        Body:
            inp = ppapa[**4235 dasfj dd 44 ** g(-----------**-----**----------------f())];
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 289))

    def test_case_91(self):
        input = """
        Function: main
        Body:
            If "" Then
                If 1 Then
                    inp = f23 + ads[2:10] +  ++++ 2 *f ** "87235jkfgshgsfg $&^# ** ;
                ElseIf 1 Then 
                EndIf.
            EndIf.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 37: :", 290))

    def test_case_92(self):
        input = """
        Function: main
        Body:
            While 1 Do
                inp = [234]fsfsg + 13 \\. 124;
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 22: [", 291))

    def test_case_93(self):
        input = """
        Function: main
        Body:
            If "" Then
            in = 123 - 4234 +. 432 || !False;
            inp = {123, 435, 423} * in;
            EndIf.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 292))

    def test_case_94(self):
        input = """
        Function: main
        Body:
            Do
                Var: arr[123][True] = True;
            While 1 EndDo.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 30: True", 293))

    def test_case_95(self):
        input = """
        Function: main
        Body:
            Var: x = 2;
            x = x =/= 12 * 412 - 4 +. -. -. -. -. "asd" + 123;
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 294))

    def test_case_96(self):
        input = """
        Function: main
        Body:
            For (i = "12", dasd < 2, 22) Do
                in = (in(in(in)))[123];
            EndFor.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 33: [", 295))

    def test_case_97(self):
        input = """
        Function: main
        Body:
            in = bli * bli - (2 + (24 -. 423 + "123" <=. 5345.));
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "successful", 296))

    def test_case_98(self):
        input = """
        Function: main
        Body:
            For(in, in < in, in)
                in = aa[23][a][a];
            EndFor.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 18: ,", 297))

    def test_case_99(self):
        input = """
        Function: main
        Body:
            blu = 123 * 23 - 123 - -.--.- "dasd";
            While (print(blu[123]) = 123, i < 10, 10)
                tttttttest();
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 35: =", 298))

    def test_case_100(self):
        input = """
        Function: main
        Body:
            While 1 Do
                Do 
                    If i = 1 Then
                        i = "daf * 1";
                    EndIf.
                While 1 EndDo.
            EndWhile.
        EndBody.
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 6 col 25: =", 299))

    def test_case_101(self):
        input = """
        ** **
        Function: main
        Body:
            Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
        EndBody.
        ** **
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 5 col 47: -", 300))

    def test_case_102(self):
        input = """
        ** **
        Function: main
        Parameter: asd[3 + 4 * f]
        Body:
            While i < 5 Do
                x = 12.32;
                Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
            EndWhile.
        EndBody.
        ** **
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 25: +", 301))

    def test_case_103(self):
        input = """
        ** **
        Function: main
        Parameter: 6425[3]
        Body:
            While i < 5 Do
                x = 12.32;
                Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
            EndWhile.
        EndBody.
        ** **
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 19: 6425", 302))

    def test_case_104(self):
        input = """
        ** **
        Function: main
        Parameter: a[size]
        Body:
            While i < 5 Do
                x = 12.32;
                Var: x = {{{1,  2 ,2e-124, "avc" , -1 }, {  4 , **erty**  5}  },  {{ 6  ,  7  },{ 8,9}}};
            EndWhile.
        EndBody.
        ** **
        """
        self.assertTrue(TestParser.checkParser(input, "Error on line 4 col 21: size", 303))

    def test105(self):
        input = """Var: x, y =1, y = "abc'" hello \\t ", m[13425], n[1053245] = {1,2,{"a534n",5.54324},5.e-145232};
            Var: a_jacj933 = 00012.21; 
        Function: fact
        Parameter: n, aca_312aAX[3][44][0x31FF], cxa[0x12][0o1][8][0]
        Body:
        Var: t, r= 10.;
        Var: thread = 0000212.3123E+3120, r= 10.;
        v = (4. \\. 3.) *.   3.14 *. r * r * a;

        object = 4123542 > 7 > 4;

        EndBody."""
        expect = "Error on line 10 col 29: >"
        self.assertTrue(TestParser.checkParser(input, expect, 307))