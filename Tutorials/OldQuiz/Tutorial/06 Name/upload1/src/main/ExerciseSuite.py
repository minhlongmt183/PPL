import unittest
from TestUtils import TestChecker
from AST import *

class ExerciseSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[],[])])
        expect = '[]'
        self.assertTrue(TestChecker.test(input,expect,300))

    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id("x"),FloatType()),FuncDecl(Id("main"),[],[],[])])
        expect = '[' + str(VarDecl(Id("x"),FloatType())) + ']'
        self.assertTrue(TestChecker.test(input,expect,301))

    def test_simple_program_2(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),IntType()), VarDecl(Id("a"),StringType()), FuncDecl(Id("main"),[],[],[])])
        varArr = [VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),IntType()), VarDecl(Id("a"),StringType())]
        expect = '[' + ",".join (str(x) for x in varArr) + ']'
        self.assertTrue(TestChecker.test(input,expect,302))

   