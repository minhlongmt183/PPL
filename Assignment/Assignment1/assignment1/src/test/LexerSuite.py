import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):


    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn", "ab,Error Token ?", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_case_8(self):
        input = "Square"
        self.assertTrue(TestLexer.checkLexeme(input, "Error Token S", 108))

    def test_case_9(self):
        input = "3nglish_For_fUn"
        self.assertTrue(TestLexer.checkLexeme(input, """3,nglish_For_fUn,<EOF>""", 109))

    def test_case_10(self):
        input = "0_day"
        self.assertTrue(TestLexer.checkLexeme(input, """0,Error Token _""", 110))

    def test_case_11(self):
        input = "zer0 111ab Download"
        self.assertTrue(TestLexer.checkLexeme(input, """zer0,111,ab,Do,wnload,<EOF>""", 111))

    def test_case_12(self):
        input = "Var: x"
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,<EOF>""", 112))
    def test_case_13(self):
        input = "Var: x = 5e-9;"
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,5e-9,;,<EOF>""", 113))
    def test_case_14(self):
        input = "Var: x = {1,2,3};"
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,{,1,,,2,,,3,},;,<EOF>""", 114))
    def test_case_15(self):
        input = "Var: x = {1,2,3;"
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,{,1,,,2,,,3,;,<EOF>""", 115))
    def test_case_16(self):
        input = "Var: x:@;"
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,:,Error Token @""", 116))
    def test_case_17(self):
        input = "Var: array[2][4]={{1,2,3,4},{5,6, 7,8}};"
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,array,[,2,],[,4,],=,{,{,1,,,2,,,3,,,4,},,,{,5,,,6,,,7,,,8,},},;,<EOF>", 117))
    def test_case_18(self):
        input = "Var# x = 0;"
        self.assertTrue(TestLexer.checkLexeme(input, "Var,Error Token #", 118))
    def test_case_19(self):
        input = "Var: x; x >= 1;"
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,;,x,>=,1,;,<EOF>", 119))
    def test_case_20(self):
        input = """
        Var: x = 123.e45;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,123.e45,;,<EOF>", 120))
    def test_case_21(self):
        input = """
        Var: isEqual = False;
        isEqual = !isEqual;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,isEqual,=,False,;,isEqual,=,!,isEqual,;,<EOF>", 121))

    def test_case_22(self):
        input = """
        Var: str = 'hEll0';
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,str,=,Error Token '", 122))
    def test_case_23(self):
        input = """
        Var: f_number = -5e+;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,f_number,=,-,5,e,+,;,<EOF>", 123))
    def test_case_24(self):
        input = """Var: h3ello-@ll;"""
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,h3ello,-,Error Token @", 124))
    def test_case_25(self):
        input = """
        If (a == b != c < d)
            Var: hello;
        EndIf.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "If,(,a,==,b,!=,c,<,d,),Var,:,hello,;,EndIf,.,<EOF>", 125))
    def test_case_26(self):
        input = """
        Var: arr[5] = 34;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,arr,[,5,],=,34,;,<EOF>", 126))
    def test_case_27(self):
        input = """
        Var: Arr[5] = 34;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,Error Token A", 127))
    def test_case_28(self):
        input = """
        Var: x = 12.e+-+-+++---456;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,12.,e,+,-,+,-,+,+,+,-,-,-,456,;,<EOF>", 128))
    def test_case_29(self):
        input = """
        Var: x = e-- + 12.0e++;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,e,-,-,+,12.0,e,+,+,;,<EOF>", 129))

    def test_case_30(self):
        input = """
          Var: x = 1 + 2*3 -4 /5 << 7 ^ 2;
          """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,1,+,2,*,3,-,4,Error Token /", 130))
    def test_case_31(self):
        input = """
        Var: x = new int[100];
        Do
        *(x + i) = i % 65 + int('a');
        i = i + 1;
        While i < 100 EndDo.
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                """Var,:,x,=,new,int,[,100,],;,Do,*,(,x,+,i,),=,i,%,65,+,int,(,Error Token '""", 131))
    def test_case_32(self):
        input = """
        Var: x = new int[100];
        Do
        *(x + i) = i % 65 + int(a);
        i = i + 1;
        While i < 100 EndDo.
        """
        self.assertTrue(TestLexer.checkLexeme(input,
            """Var,:,x,=,new,int,[,100,],;,Do,*,(,x,+,i,),=,i,%,65,+,int,(,a,),;,i,=,i,+,1,;,While,i,<,100,EndDo,.,<EOF>""",
            132))
    def test_case_33(self):
        input = """
        Var: arr = {1 { 2    { 3{4{  "       "}} } }    };
        """
        self.assertTrue(TestLexer.checkLexeme(input,
            "Var,:,arr,=,{,1,{,2,{,3,{,4,{,       ,},},},},},;,<EOF>", 133))
    def test_case_34(self):
        input = """
        Var: x = "hello"; {123, 456, **hello***}[99 "aaa"] = 12*4 \.55 -.-.;
        """
        self.assertTrue(TestLexer.checkLexeme(input,
            """Var,:,x,=,hello,;,{,123,,,456,,,*,},[,99,aaa,],=,12,*,4,\.,55,-.,-.,;,<EOF>""", 134))

    def test_case_35(self):
        input = """
        x = 213e,145.136e-9809,04524.4344, .1444,  0.+e565, 656.e, ; 
        , 1.e-13,123.e+, 165.e134 
        """
        self.assertTrue(TestLexer.checkLexeme(input,
            "x,=,213,e,,,145.136e-9809,,,04524.4344,,,.,1444,,,0.,+,e565,,,656.,e,,,;,,,1.e-13,,,123.,e,+,,,165.e134,<EOF>",
                135))

    def test_case_36(self):
        input = """
        "Good morningg'"\o"
        """
        self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: Good morningg'"\o""", 136))
    def test_case_37(self):
        input = """
        bool isEqual = (12 -4) == 13-5);
        If (isEqual)
            print("Equal\g\d");
        EndIf.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "bool,isEqual,=,(,12,-,4,),==,13,-,5,),;,If,(,isEqual,),print,(,Illegal Escape In String: Equal\g", 137))
    def test_case_38(self):
        input = """
        Var: a = "test illegal string \\a\\b\\c";"""
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,a,=,Illegal Escape In String: test illegal string \\a", 138))
    def test_case_39(self):
        input ="""
        "String \\t with"**comment\\a\\k**" and not in comment \\a\\k"""
        self.assertTrue(TestLexer.checkLexeme(input, """String \\t with,Illegal Escape In String:  and not in comment \\a""", 139))
    def test_case_40(self):
        input = """ "mix\\'ab'" test\\t gi \\normal's" """
        self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: mix\\'ab'" test\\t gi \\normal's""", 140))
    def test_case_41(self):
        input = """
        "Illegdddd''error
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Illegal Escape In String: Illegdddd''", 141))
    def test_case_42(self):
        input = """
        "thkahsedfyaefasdfadsdfg\\b\\\\\\asdfkyuoe dgaisdgfasdf"
        """
        self.assertTrue(TestLexer.checkLexeme(input, """Illegal Escape In String: thkahsedfyaefasdfadsdfg\\b\\\\\\a""", 142))
    def test_case_43(self):
        input = """
            array = "\\\' \\b\\f \\\\ adksjflakdjf '!#%"
            x = [123];
        """
        self.assertTrue(TestLexer.checkLexeme(input, """array,=,Illegal Escape In String: \\' \\b\\f \\\\ adksjflakdjf '!""", 143))
    def test_case_44(self):
        input = """
            If True Then
            ElseIf False
            Then
            Else
            Then
            print("win\\\\'"\\0");
        """
        self.assertTrue(TestLexer.checkLexeme(input, """If,True,Then,ElseIf,False,Then,Else,Then,print,(,Illegal Escape In String: win\\\\'"\\0""", 144))
    def test_case_45(self):
        input ="""
        ** Test
        * multi-line
        * comment
        * asdjlkajsdflkajefoihaweiofhasdfihasdfsd
        **"""
        self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 145))
    def test_case_46(self):
        input = "**test comment with special char(*$^*%&#^&**"
        self.assertTrue(TestLexer.checkLexeme(input, "<EOF>", 146))
    def test_case_47(self):
        input = "**test unterminated comment *&^23762783"
        self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 147))
    def test_case_48(self):
        input = "**more than comments !@#$%*(&^%&*"
        self.assertTrue(TestLexer.checkLexeme(input, "Unterminated Comment", 148))
    def test_case_49(self):
        input = "*normal comment**"
        self.assertTrue(TestLexer.checkLexeme(input, "*,normal,comment,Unterminated Comment", 149))
    def test_case_50(self):
        input ="""**randome anthing *jhs\\r"""
        self.assertTrue(TestLexer.checkLexeme(input, """Unterminated Comment""", 150))
    def test_case_51(self):
        input = """
        Var: x = 4367;
        ** command
        * in
        * function
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,4367,;,Unterminated Comment", 151))
    def test_case_52(self):
        input = """
        ** " Illegal escape \\a \\b 
        * \\e '"
        **
        Var: abc = {1,2,,3};
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,abc,=,{,1,,,2,,,,,3,},;,<EOF>", 152))
    def test_case_53(self):
        input = """
        print(**comment
        #     in print function* "hello world!")
        """
        self.assertTrue(TestLexer.checkLexeme(input, "print,(,Unterminated Comment", 153))
    def test_case_54(self):
        input = """
        Var: i = 0;
        While (i < 5)
            print(toString(i *. 10));
            ** comment in while statement**
            x = int(x);
        EndWhile.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,i,=,0,;,While,(,i,<,5,),print,(,toString,(,i,*.,10,),),;,x,=,int,(,x,),;,EndWhile,.,<EOF>", 154))

    def test_case_55(self):
        input = """
        * unterminated comment **
        """
        self.assertTrue(TestLexer.checkLexeme(input, """*,unterminated,comment,Unterminated Comment""", 155))

    def test_case_56(self):
        input = """
        For (i = 0, i < 100, i ** i) Do
            print(chr(ord(i)+a)));
        EndFor.
        """
        self.assertTrue(TestLexer.checkLexeme(input, """For,(,i,=,0,,,i,<,100,,,i,Unterminated Comment""", 156))
    def test_case_57(self):
        input = """
        For( i = 0, i < 100, i ++)
            sum_of_square_root = i ** .5;
        EndFor.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "For,(,i,=,0,,,i,<,100,,,i,+,+,),sum_of_square_root,=,i,Unterminated Comment", 157))
    def test_case_58(self):
        input = """
        **\\b " ** "AUIFq3r9aseifjasidf" .1324q3;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "AUIFq3r9aseifjasidf,.,1324,q3,;,<EOF>", 158))
    def test_case_59(self):
        input = """
       ***haidyfiaufhiuahefiuawefawef*reajefoiayeoifhawefhaiweuf***
        """
        self.assertTrue(TestLexer.checkLexeme(input, "*,<EOF>", 159))
    def test_case_60(self):
        input = """
        ***haidyfiaufhiuahefiuawefawef*reajefoiayeoifhawefhaiweuf**
       "agadg\\'\\t\\n";
       "'"Helloworld'"";
        """
        self.assertTrue(TestLexer.checkLexeme(input, """agadg\\'\\t\\n,;,'"Helloworld'",;,<EOF>""", 160))

    def test_case_61(self):
        input = """
            add_sub = +-+....-.-.-----.+-.+.;
            mul_div = *.*.* \\.\\.\\..*.*.;
            strr = "abcd{35}" ***abcdeAhadsad123\\n\\a\\b**;
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """add_sub,=,+,-,+.,.,.,.,-.,-.,-,-,-,-,-.,+,-.,+.,;,mul_div,=,*.,*.,*,\.,\.,\.,.,*.,*.,;,strr,=,abcd{35},;,<EOF>""",
                                              161))

    def test_case_62(self):
        input = """
            x = {     **string*** ***number1234***   13134    } + 1234230X12313+ 4798132;
        """
        self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,*,*,13134,},+,1234230,Error Token X""", 162))

    def test_case_63(self):
        input = """
        ** **
        Function: main
        Body:
            Var: x = {{{1 **2243245029450924**,  2 ,1e-2323, "strings" , -113413 }, {  132413 , **commend in here**  5}  }}};
        EndBody.
        ** **
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              "Function,:,main,Body,:,Var,:,x,=,{,{,{,1,,,2,,,1e-2323,,,strings,,,-,113413,},,,{,132413,,,5,},},},},;,EndBody,.,<EOF>",
                                              163))


    def test_case_64(self):
        input = """
            ** comment ***
            x = a + a -. 1230x123as87349874ahads && 1 || 1.e+13;
        """
        self.assertTrue(TestLexer.checkLexeme(input, """*,x,=,a,+,a,-.,1230,x123as87349874ahads,&&,1,||,1.e+13,;,<EOF>""", 164))
    def test_case_65(self):
        input = """
            x = {     **string*** ***number1234*** "special key: \\t\\b\\f\\r\\\'\\n"   13134    } + 123423Ox12313+ 4798132;
        """
        self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,*,*,special key: \\t\\b\\f\\r\\'\\n,13134,},+,123423,Error Token O""", 165))
    def test_case_66(self):
        input = """
        "Unclosed
        Strinsg
        or
        Normal
        String"
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Unclosed String: Unclosed\n", 166))
    def test_case_67(self):
        input = """
         print("hello World!
         welcome to PPL")
         """
        self.assertTrue(TestLexer.checkLexeme(input, "print,(,Unclosed String: hello World!\n", 167))
    def test_case_68(self):
        input = """
        "'"'"!@#$%^&*()\\'\\r\\f\\b~!@#$%^&/?|*('"
        """
        self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: '"'"!@#$%^&*()\\'\\r\\f\\b~!@#$%^&/?|*('"\n""", 168))
    def test_case_69(self):
        input = """
            x = {abc, 313*123, 1.4134 *. 23[1231],b**3***, 13 -. 2}["asdja'"'"'"'"];
        """
        self.assertTrue(TestLexer.checkLexeme(input, """x,=,{,abc,,,313,*,123,,,1.4134,*.,23,[,1231,],,,b,*,,,13,-.,2,},[,Unclosed String: asdja'"'"'"'"];\n""", 169))
    def test_case_70(self):
        input = """
        "unclosed
        string
        multiple lines"
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Unclosed String: unclosed\n", 170))
    def test_case_71(self):
        input = """
        "string with'"quote'\""""
        self.assertTrue(TestLexer.checkLexeme(input, """Unclosed String: string with'"quote'\"""", 171))
    def test_case_72(self):
        input = """
        Var: x = 10, y[100], str = "string'", v@raribl3;"""
        self.assertTrue(TestLexer.checkLexeme(input, """Var,:,x,=,10,,,y,[,100,],,,str,=,Unclosed String: string'", v@raribl3;""", 172))
    def test_case_73(self):
        input = """
        Var: x = "string\\rwith\\tnumber:98";
        Var: y = "this is unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,x,=,string\\rwith\\tnumber:98,;,Var,:,y,=,Unclosed String: this is unclosed string", 173))
    def test_case_74(self):
        input = """
        hello = "Hellw0rd!;"""
        self.assertTrue(TestLexer.checkLexeme(input, "hello,=,Unclosed String: Hellw0rd!;" ,174))

    def test_case_75(self):
        input = """
        Function: fibo
        Parameter: n
        Body:
            If (n < 0) Then
                Return -1;
            ElseIf (n == 0 || n == 1) Then
                Return 1;
            Else
                Return fibo(n-1) + fibo (n - 2);
            EndIf.
        EndBody."""
        self.assertTrue(TestLexer.checkLexeme(input,
                                              "Function,:,fibo,Parameter,:,n,Body,:,If,(,n,<,0,),Then,Return,-,1,;,ElseIf,(,n,==,0,||,n,==,1,),Then,Return,1,;,Else,Return,fibo,(,n,-,1,),+,fibo,(,n,-,2,),;,EndIf,.,EndBody,.,<EOF>",
                                              175))
    def test_case_76(self):
        input = """
        Function: sum
        Parameter: elem[10], sumElem
        Body:
            Var: i = 0;
            sumElem = 0;
            While (i < 10)
                sumElem += elem[i];
                i += 1;
            EndWhile.
        EndBody."""
        self.assertTrue(TestLexer.checkLexeme(input, "Function,:,sum,Parameter,:,elem,[,10,],,,sumElem,Body,:,Var,:,i,=,0,;,sumElem,=,0,;,While,(,i,<,10,),sumElem,+,=,elem,[,i,],;,i,+,=,1,;,EndWhile,.,EndBody,.,<EOF>", 176))
    def test_case_77(self):
        input = """
        Function: main
        ** this is the normal function**
        Body:
            x = 5;
            foo(x + 5);
        EndBody.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Function,:,main,Body,:,x,=,5,;,foo,(,x,+,5,),;,EndBody,.,<EOF>", 177))

    def test_case_78(self):
        input = "0xCA0xbe0o0213"
        self.assertTrue(TestLexer.checkLexeme(input, "0xCA0,xbe0o0213,<EOF>", 178))
    def test_case_79(self):
        input = """
            isTrue = False;
            If (isTrue == True)
                number = 0o123459;
            EndIf."""
        self.assertTrue(TestLexer.checkLexeme(input, "isTrue,=,False,;,If,(,isTrue,==,True,),number,=,0o12345,9,;,EndIf,.,<EOF>", 179))
    def test_case_80(self):
        input = """
        func_to_Ch3ck = (4 < 2) && (2. > 9.);
        """
        self.assertTrue(TestLexer.checkLexeme(input, "func_to_Ch3ck,=,(,4,<,2,),&&,(,2.,>,9.,),;,<EOF>", 180))
    def test_case_81(self):
        input = """
        x = ((x - 1) && 5) || !(x - func(1));
        """
        self.assertTrue(TestLexer.checkLexeme(input, "x,=,(,(,x,-,1,),&&,5,),||,!,(,x,-,func,(,1,),),;,<EOF>", 181))
    def test_case_82(self):
        input = """
        print(**comments
        multiple line** "Hello W0rld!")
        """
        self.assertTrue(TestLexer.checkLexeme(input, "print,(,Hello W0rld!,),<EOF>", 182))

    def test_case_83(self):
        input = """
        0x_bc + 0o7136999 * 0x0o9999;
        """
        self.assertTrue(TestLexer.checkLexeme(input, "0,x_bc,+,0o7136,999,*,0,x0o9999,;,<EOF>", 183))

    def test_case_84(self):
        input = """
        Function: cacl
        Parameter: a, n
        Body:
            func(num + f1() + arr[0][a+b*c-d+1.4]) = 9 + f("my name");
        EndBody.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Function,:,cacl,Parameter,:,a,,,n,Body,:,func,(,num,+,f1,(,),+,arr,[,0,],[,a,+,b,*,c,-,d,+,1.4,],),=,9,+,f,(,my name,),;,EndBody,.,<EOF>", 184))
    def test_case_85(self):
        input = """
        If (func_var_ == 08231)
            *x = (x * 6 - 2 =/= 4) >> 3 + some_number *. float_numb3r;
        EndIf.
        """
        self.assertTrue(TestLexer.checkLexeme(input, "If,(,func_var_,==,0,8231,),*,x,=,(,x,*,6,-,2,=/=,4,),>,>,3,+,some_number,*.,float_numb3r,;,EndIf,.,<EOF>", 185))

    def test_case_86(self):
        input = """
        Var: ipaddr = "1.1.234.45552.213123";
        """
        self.assertTrue(TestLexer.checkLexeme(input, "Var,:,ipaddr,=,1.1.234.45552.213123,;,<EOF>", 186))

    def test_case_87(self):
        input = """
        "'"* Try to hack me !!! ** wel  ocome *** **"
        """
        self.assertTrue(TestLexer.checkLexeme(input, """'"* Try to hack me !!! ** wel  ocome *** **,<EOF>""", 187))

    def test_case_88(self):
        input = """
        Var: checkValue = False;
        If checkValue:
            a[1 , .2, 3., :6] = arr[:9].plot(hihihi)
        EndIf.
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              "Var,:,checkValue,=,False,;,If,checkValue,:,a,[,1,,,.,2,,,3.,,,:,6,],=,arr,[,:,9,],.,plot,(,hihihi,),EndIf,.,<EOF>",
                                              188))
    def test_case_89(self):
        input = """
        **call function**
        foo(a + 7. *. .e-123 \\. 2.231e+--4 + arr[.2 != 5.][funct(1)]);
        """
        self.assertTrue(TestLexer.checkLexeme(input, "foo,(,a,+,7.,*.,.,e,-,123,\.,2.231,e,+,-,-,4,+,arr,[,.,2,!=,5.,],[,funct,(,1,),],),;,<EOF>", 189))

    def test_case_90(self):
        input = """
       "I have a pen, I have a apple ... Uh ...Apple-Pen\\'s  '"Pineapple-Pen'"'" \\b \\n \\f \\r \\t Pen-Pineapple-Apple-Pen"
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """I have a pen, I have a apple ... Uh ...Apple-Pen\\'s  '"Pineapple-Pen'"'" \\b \\n \\f \\r \\t Pen-Pineapple-Apple-Pen,<EOF>""",
                                              190))

    def test_case_91(self):
        input = """
        mother - father * 113 (False || True){children1, chldren2, a + .3424, 2.e-12 *. 2.1212e.2}
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              "mother,-,father,*,113,(,False,||,True,),{,children1,,,chldren2,,,a,+,.,3424,,,2.e-12,*.,2.1212,e,.,2,},<EOF>",
                                              191))

    def test_case_92(self):
        input = """
        While x = 1: acb.{1,2,3,  5, 6}[0][fucnt(124, "String " +. 1287 +. -. *. 0o123)];
        """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """While,x,=,1,:,acb,.,{,1,,,2,,,3,,,5,,,6,},[,0,],[,fucnt,(,124,,,String ,+.,1287,+.,-.,*.,0o123,),],;,<EOF>""",
                                              192))

    def test_case_93(self):
        input = """
           Function: check_numer
           x = 0x124;
           y = 0o11413;
           z = 0xFD0o12439999asdha;
           Var: ch3ck1 = check(x);
           Var: ch3ck2 = check(y);
           Var: ch3ck3 = check(z);
           EndFor.
           """
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """Function,:,check_numer,x,=,0x124,;,y,=,0o11413,;,z,=,0xFD0,o12439999asdha,;,Var,:,ch3ck1,=,check,(,x,),;,Var,:,ch3ck2,=,check,(,y,),;,Var,:,ch3ck3,=,check,(,z,),;,EndFor,.,<EOF>""",
                                              193))

    def test_case_94(self):
        input = """
            arr = {77, "HELLO"   98,    @233, 12#498, "''"};
        """
        self.assertTrue(TestLexer.checkLexeme(input, """arr,=,{,77,,,HELLO,98,,,Error Token @""", 194))

    def test_case_95(self):
        input = """
            x = 123 + 888.abcdef + {456, {{{{"fucntion namer"}}}}};
            x = !(&& || 9&&) ;
            x =/= (145 < .10) >. 123 != 124 <=. djkfa;"""
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """x,=,123,+,888.,abcdef,+,{,456,,,{,{,{,{,fucntion namer,},},},},},;,x,=,!,(,&&,||,9,&&,),;,x,=/=,(,145,<,.,10,),>.,123,!=,124,<=.,djkfa,;,<EOF>""",
                                              195))
    def test_case_96(self):
        input = """
            0.34243E-3 001230e3827400 .8e11423 0.e.0 3.123.2135.5"""
        self.assertTrue(TestLexer.checkLexeme(input,
                                              """0.34243E-3,001230e3827400,.,8e11423,0.,e,.,0,3.123,.,2135.5,<EOF>""",
                                              196))

    def test_case_97(self):
        input = "x = (.9 +. 3.e-124) \. 2.931 *. x *. x \. y;"
        self.assertTrue(TestLexer.checkLexeme(input, "x,=,(,.,9,+.,3.e-124,),\.,2.931,*.,x,*.,x,\.,y,;,<EOF>", 197))
    def test_case_98(self):
        input = "Sum(3 + x, .8 \. y.e-128);"
        self.assertTrue(TestLexer.checkLexeme(input, "Error Token S", 198))
    def test_case_99(self):
        input = "+---++aldjfaiweabc<>fahksdjf>cv **134714jkdhfkajf<>dasad==(*rrr*)*)**"
        self.assertTrue(TestLexer.checkLexeme(input,"+,-,-,-,+,+,aldjfaiweabc,<,>,fahksdjf,>,cv,<EOF>",199))
    def test_case_100(self):
        input = """***** *NorMALL F0r 3x@mpl3*"""
        self.assertTrue(TestLexer.checkLexeme(input,"*,*,Error Token N",200))
