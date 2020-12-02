import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclared_function_function_1(self):
        """Simple program: int main() {} """
        input = Program([
                VarDecl(Id("a"), IntType()),
                VarDecl(Id("b"), FloatType()),
                FuncDecl(Id("main"),[VarDecl(Id("a"), IntType()), VarDecl(Id("b"), FloatType())], [], [], IntType()),
                FuncDecl(Id("main"), [], [], [])
                ])
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_redeclared_variable_variable_2(self):
        """Simple program: int main() {} """
        input = Program([
                VarDecl(Id("b"), IntType()),
                VarDecl(Id("b"), FloatType()),
                FuncDecl(Id("foo"),[VarDecl(Id("a"), IntType()), VarDecl(Id("b"), FloatType())], [], [], IntType()),
                FuncDecl(Id("main"), [], [], [])
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_redeclared_function_variable_3(self):
        """Simple program: int main() {} """
        input = Program([
                VarDecl(Id("b"), IntType()),
                VarDecl(Id("c"), FloatType()),
                FuncDecl(Id("b"),[VarDecl(Id("a"), IntType()), VarDecl(Id("b"), FloatType())], [], [], IntType()),
                FuncDecl(Id("main"), [], [], [])
                ])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,402))


    
    