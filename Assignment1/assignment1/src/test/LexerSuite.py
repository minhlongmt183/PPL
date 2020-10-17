import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_identifier3(self):
        self.assertTrue(TestLexer.checkLexeme("rdad 40oBhenK292aWfTSFLt6", "rdad,40,oBhenK292aWfTSFLt6,<EOF>", 103))

    def test_identifier4(self):
        self.assertTrue(TestLexer.checkLexeme("kK a10 1AbCd naA", "kK,a10,1,Error Token A", 104))

    def test_identifier5(self):
        self.assertTrue(TestLexer.checkLexeme("asf aso Dowoad ", "asf,aso,Do,woad,<EOF>", 105))

    def test_identifier6(self):
        self.assertTrue(TestLexer.checkLexeme("tuoitre chuwa trai su doi", "tuoitre,chuwa,trai,su,doi,<EOF>", 106))

    def test_identifier7(self):
        self.assertTrue(TestLexer.checkLexeme("dem123 123dem 1a an han", "dem123,123,dem,1,a,an,han,<EOF>", 107))

    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("yud al gnaht ugn 12Ads", "yud,al,gnaht,ugn,12,Error Token A", 108))

    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("Var: x", "Var,:,x,<EOF>", 109))

    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("1 cOn viT xOE rA HAi caI canh", "1,cOn,viT,xOE,rA,Error Token H", 110))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 111))

    def test_integer_real1(self):
        self.assertTrue(
            TestLexer.checkLexeme("12.e5 10.e-3 10.e+3 10.e 0.e", "12.e5,10.e-3,10.e+3,10.,e,0.,e,<EOF>", 112))

    def test_integer_real2(self):
        self.assertTrue(TestLexer.checkLexeme("01 10 001 100", "0,1,10,0,0,1,100,<EOF>", 113))

    def test_integer_real3(self):
        self.assertTrue(TestLexer.checkLexeme("Var x0.12e51.2", "Var,x0,.,12e51,.,2,<EOF>", 114))

    def test_integer_real4(self):
        self.assertTrue(
            TestLexer.checkLexeme("-0 -1 -10 -.e3 -10.e -10.e3", "-,0,-,1,-,10,-.,e3,-,10.,e,-,10.e3,<EOF>", 115))

    def test_integer_real5(self):
        self.assertTrue(TestLexer.checkLexeme("0.3 0.123 .123 123. .", "0.3,0.123,.,123,123.,.,<EOF>", 116))

    def test_integer_real6(self):
        self.assertTrue(TestLexer.checkLexeme("0.0 12.. 1..e.3 ..1..e", "0.0,12.,.,1.,.,e,.,3,.,.,1.,.,e,<EOF>", 117))

    def test_integer_real7(self):
        self.assertTrue(
            TestLexer.checkLexeme("0X12A 0x12B 0XFA 0XABC 0o567 0o2", "0X12A,0x12B,0XFA,0XABC,0o567,0o2,<EOF>", 118))

    def test_integer_real8(self):
        self.assertTrue(TestLexer.checkLexeme("0B123 0BFA", "0,Error Token B", 119))

    def test_integer_real9(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3 12e3 12.e5 12.0e3 12000. 120000e-1",
                                              "12.0e3,12e3,12.e5,12.0e3,12000.,120000e-1,<EOF>", 120))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 121))

    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bac\\ma" abc""", """Illegal Escape In String: bac\\m""", 122))

    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bad game toDay\\How\\na win" """,
                                              """Illegal Escape In String: bad game toDay\\H""", 123))

    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ",dls\\F12" """, """Illegal Escape In String: ,dls\\F""", 124))

    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ado\\mado" """, """Illegal Escape In String: ado\\m""", 125))

    def test_illegal_escape5(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" 123abc "xyz\\k" 456""", """123,abc,Illegal Escape In String: xyz\\k""", 126))

    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aa\\" """, """Illegal Escape In String: aa\\" """, 127))

    def test_illegal_escape7(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "This is ' illegal" """, """Illegal Escape In String: This is ' """, 128))

    def test_illegal_escape8(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "This is \\W illegal""", """Illegal Escape In String: This is \\W""", 129))

    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a test '" asdsadasd ' \\f asdasd " """,
                                              """Illegal Escape In String: This is a test '" asdsadasd ' """, 130))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  """, """Unclosed String: abc def  """, 131))

    def test_unclose_String1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "bac""xyc """, """bac,Unclosed String: xyc """, 132))

    def test_unclose_String2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "adsfa \n" """, """Unclosed String: adsfa \n""", 133))

    def test_unclose_String3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "acnv EOF """, """Unclosed String: acnv EOF """, 134))

    def test_unclose_String4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\n """, """Unclosed String: abc\\n """, 135))

    def test_unclose_String5(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" a+11.2+"mam.123" 12 "%^&""", """a,+,11.2,+,mam.123,12,Unclosed String: %^&""",
                                  136))

    def test_unclose_String6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " "" """, """, ,Unclosed String:  """, 137))

    def test_unclose_String7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" " """, """,Unclosed String:  """, 138))

    def test_unclose_String8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ULxhskjdhfkja2""", """Unclosed String: ULxhskjdhfkja2""", 139))

    def test_unclose_String9(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "Nk8U;"rA"@Y3*"oV"bh1""", """Nk8U;,rA,@Y3*,oV,Unclosed String: bh1""", 140))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 141))

    def test_normal_string_with_escape1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t"  """,
                                              """This is a string containing tab \\t,<EOF>""", 142))

    def test_normal_string_with_escape2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'""  """,
                                              """He asked me: '"Where is John?'",<EOF>""", 143))

    def test_normal_string_with_escape3(self):
        self.assertTrue(TestLexer.checkLexeme(""" " This is a test '" asdsadasd ' \\b asdasd "  """,
                                              """Illegal Escape In String:  This is a test '" asdsadasd ' """, 144))

    def test_normal_string_with_escape4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\ def"  """, """Illegal Escape In String: ab'"c\\ """, 145))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn", "ab,Error Token ?", 146))

    def test_wrong_token1(self):
        self.assertTrue(TestLexer.checkLexeme("Tabcd", "Error Token T", 147))

    def test_wrong_token2(self):
        self.assertTrue(TestLexer.checkLexeme("Continue BreAk", "Continue,Error Token B", 148))

    def test_wrong_token3(self):
        self.assertTrue(TestLexer.checkLexeme("1++3", "1,+,+,3,<EOF>", 149))

    def test_wrong_token4(self):
        self.assertTrue(TestLexer.checkLexeme("a~bc", "a,Error Token ~", 150))

    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("For brEaK Continue km", "For,brEaK,Continue,km,<EOF>", 151))

    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("Do if thEn ElSE ", "Do,if,thEn,Error Token E", 152))

    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("Varr VaR", "Var,r,Error Token V", 153))

    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter: x", "Parameter,:,x,<EOF>", 154))

    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("BODY int 1.12INTEGER 12and", "Error Token B", 155))

    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu", "oR,diVModNTEGER,Error Token M", 156))

    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("If then else false", "If,then,else,false,<EOF>", 157))

    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("anD then false", "anD,then,false,<EOF>", 158))

    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("sTRIng False", "sTRIng,False,<EOF>", 159))

    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("EndDoEndForWhWhileileWhileWhile", "EndDo,EndFor,Error Token W", 160))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" """,
                                              """This is a string containing tab \\t,<EOF>""", 161))

    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" """,
                                              """He asked me: '"Where is John?'",<EOF>""", 162))

    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "John isn'"t me" """, """John isn'"t me,<EOF>""", 163))

    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 164))

    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """, """,<EOF>""", 165))

    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "**This is not a comment **" 12yz """,
                                              """**This is not a comment **,12,yz,<EOF>""", 166))

    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Var: x= 1+2;" """, """Var: x= 1+2;,<EOF>""", 167))

    def test_string8(self):
        self.assertTrue(
            TestLexer.checkLexeme(""" "This is a normal string" """, """This is a normal string,<EOF>""", 168))

    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string with escape \\f " """,
                                              """This is a string with escape \\f ,<EOF>""", 169))

    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme(""" \"\"\"\" """, """,,<EOF>""", 170))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("a+bas+.asdf-ddas-.", "a,+,bas,+.,asdf,-,ddas,-.,<EOF>", 171))

    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("a++bcds--cd", "a,+,+,bcds,-,-,cd,<EOF>", 172))

    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("asdf*dsf*.123/123/.321", "asdf,*,dsf,*.,123,Error Token /", 173))

    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("a *.0.123e12", "a,*.,0.123e12,<EOF>", 174))

    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("!a%5&&b||c", "!,a,%,5,&&,b,||,c,<EOF>", 175))

    def test_operator6(self):
        self.assertTrue(TestLexer.checkLexeme("a==b==01234!=43210<3>4", "a,==,b,==,0,1234,!=,43210,<,3,>,4,<EOF>", 176))

    def test_operator7(self):
        self.assertTrue(TestLexer.checkLexeme("*and<=>mod</<=", "*,and,<=,>,mod,<,Error Token /", 177))

    def test_operator8(self):
        self.assertTrue(TestLexer.checkLexeme("=/=6==5<.abd>.0", "=/=,6,==,5,<.,abd,>.,0,<EOF>", 178))

    def test_operator9(self):
        self.assertTrue(TestLexer.checkLexeme("3>.123e", "3,>.,123,e,<EOF>", 179))

    def test_operator10(self):
        self.assertTrue(TestLexer.checkLexeme("0.123/.12.e3", "0.123,Error Token /", 180))

    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("*** **", "<EOF>", 181))

    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("*****", "*,<EOF>", 182))

    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("* ****", "*,<EOF>", 183))

    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("**1.e0 - 101\n** asda", "asda,<EOF>", 184))

    def test_comment5(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0\\nabc -101", "Unterminated Comment", 185))

    def test_comment6(self):
        self.assertTrue(
            TestLexer.checkLexeme("13ek3<9**e=9e**end*das***d1.nerE", "13,ek3,<,9,end,*,das,Unterminated Comment", 186))

    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("**dasd*1.n*dm**2er*E**", "2,er,*,Error Token E", 187))

    def test_comment8(self):
        self.assertTrue(
            TestLexer.checkLexeme("+abc<>xyzb>cv **12mds<>dsd=(*dsd*)*)**", "+,abc,<,>,xyzb,>,cv,<EOF>", 188))

    def test_comment9(self):
        self.assertTrue(TestLexer.checkLexeme("""***** *sAMPLE*""", "*,*,sAMPLE,*,<EOF>", 189))

    def test_comment10(self):
        self.assertTrue(TestLexer.checkLexeme("{abc} 1.abc", "{,abc,},1.,abc,<EOF>", 190))

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("1e05 0x00.12e5 100e-10", "1e05,0,x00,.,12e5,100e-10,<EOF>", 191))

    def test_float1(self):
        self.assertTrue(TestLexer.checkLexeme("0.33123E-3", "0.33123E-3,<EOF>", 192))

    def test_float2(self):
        self.assertTrue(TestLexer.checkLexeme(".e5 .5 01e2.32 +10", ".,e5,.,5,0,1e2,.,32,+,10,<EOF>", 193))

    def test_float3(self):
        self.assertTrue(TestLexer.checkLexeme("0.e0 01e3 01.e3 ee3", "0.e0,0,1e3,0,1.e3,ee3,<EOF>", 194))

    def test_float4(self):
        self.assertTrue(TestLexer.checkLexeme("0xe123 0oe.123", "0,xe123,0,oe,.,123,<EOF>", 195))

    def test_float5(self):
        self.assertTrue(
            TestLexer.checkLexeme("123. 123.0 123.123 123.ee321", "123.,123.0,123.123,123.,ee321,<EOF>", 196))

    def test_float6(self):
        self.assertTrue(
            TestLexer.checkLexeme("000e300 e123 0.e.0 3.5.5.5", "0,0,0e300,e123,0.,e,.,0,3.5,.,5.5,<EOF>", 197))

    def test_boolean(self):
        self.assertTrue(TestLexer.checkLexeme("""True + False""", """True,+,False,<EOF>""", 198))

    def test_boolean2(self):
        self.assertTrue(TestLexer.checkLexeme("""TruE avasd""", """Error Token T""", 199))

    def test_boolean3(self):
        self.assertTrue(TestLexer.checkLexeme("0.e3 01e3 01.e3 01.0e3", "0.e3,0,1e3,0,1.e3,0,1.0e3,<EOF>", 200))