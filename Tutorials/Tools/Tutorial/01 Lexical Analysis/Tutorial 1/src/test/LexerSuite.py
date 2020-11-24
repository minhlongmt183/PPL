import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test( "abc",
                                        "abc,<EOF>",
                                        101))
                                        
        self.assertTrue(TestLexer.test( "conbo con ga concasac",
                                        "conbo,con,ga,concasac,<EOF>",
                                        102))
                                        
        self.assertTrue(TestLexer.test( "cSOcnsmak0326Os1Q12",
                                        "c,S,O,cnsmak0326,O,s1,Q,12,<EOF>",
                                        103))
                                        
        self.assertTrue(TestLexer.test( "Losp0)jM",
                                        "L,osp0,),j,M,<EOF>",
                                        104))
                                        
        self.assertTrue(TestLexer.test( "&*928MksoazMsM",
                                        "&,*,928,M,ksoaz,M,s,M,<EOF>",
                                        105))
                                        
        print("test_identifier passed")

    def test_real(self):
        self.assertTrue(TestLexer.test( "1.0",
                                        "1.0,<EOF>",
                                        110))
                                        
        self.assertTrue(TestLexer.test( "1E-12",
                                        "1E-12,<EOF>",
                                        111))
                                        
        self.assertTrue(TestLexer.test( "1.0e-12",
                                        "1.0e-12,<EOF>",
                                        112))
                                        
        self.assertTrue(TestLexer.test( "12.04Sconca1.2E+15",
                                        "12.04,S,conca1,.2E+15,<EOF>",
                                        113))
                                        
        self.assertTrue(TestLexer.test( "c12C10.2E-12E123E+1+1",
                                        "c12,C,10.2E-12,E,123E+1,+,1,<EOF>",
                                        114))
                                        
        print("test_real passed");

    def test_string(self):
        self.assertTrue(TestLexer.test( "'c'",
                                        "'c',<EOF>",
                                        120))
                                        
        self.assertTrue(TestLexer.test( "'conbocuoi'",
                                        "'conbocuoi',<EOF>",
                                        121))
                                        
        self.assertTrue(TestLexer.test("'can'c't'",
                                        "'can',c,'t',<EOF>",
                                        122))
                                        
        self.assertTrue(TestLexer.test("'hehe'conbo0z9123C0.105",
                                        "'hehe',conbo0z9123,C,0.105,<EOF>",
                                        123))
                                        
        self.assertTrue(TestLexer.test("alo123'ss'alo567S0",
                                        "alo123,'ss',alo567,S,0,<EOF>",
                                        124))
                                        

    def test_integer(self):
        """test integers"""
#        self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))
        print("test_integer passed")
#    def test_conbocuoi(self):
#        print('789')