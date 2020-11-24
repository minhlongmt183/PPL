import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("int main() {},int,main,(),{},<EOF>",101))
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
        self.assertTrue(TestLexer.test("a=(b==2)\nconbocuoi=100\nint c=1;","a,=,(,b,=,=,2,),conbocuoi,=,100,int,c,=,1,;,<EOF>",105))
        print("test_identifier passed")
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))
        
        self.assertTrue(TestLexer.test("var a:integer;","var,a,:,integer,;,<EOF>",105))
        print("test_integer passed")
#    def test_conbocuoi(self):
#        print('789')
