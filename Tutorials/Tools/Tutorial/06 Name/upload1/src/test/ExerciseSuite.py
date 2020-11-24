import unittest
from TestUtils import TestChecker
from AST import *

class ExerciseSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("xaa"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("xaa"),IntType())],[])])
        expect = 'Duplicate: Id(xaa)'
        self.assertTrue(TestChecker.test(input,expect,300))
    
    def test_simple_program_1(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),FloatType())],[])])
        expect = '[VarDecl(Id(x),FloatType),VarDecl(Id(y),FloatType)]'
        self.assertTrue(TestChecker.test(input,expect,301))
        
    def test_simple_program_2(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[],[VarDecl(Id("xaa"),FloatType()),VarDecl(Id("y"),FloatType()),VarDecl(Id("xaa"),IntType())],[])])
        expect = 'Duplicate: Id(xaa)'
        self.assertTrue(TestChecker.test(input,expect,302))
        
    def test_simple_program_3(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id("main"),[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),IntType()),VarDecl(Id("z"),FloatType()),VarDecl(Id("t"),FloatType())],[],[]), FuncDecl(Id("main"),[VarDecl(Id("x"),FloatType()),VarDecl(Id("y"),IntType()),VarDecl(Id("z"),FloatType()),VarDecl(Id("x"),FloatType())],[],[])])
        expect = '[]'
        self.assertTrue(TestChecker.test(input,expect,303))
