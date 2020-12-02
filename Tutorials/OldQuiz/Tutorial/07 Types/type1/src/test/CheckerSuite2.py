import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclared_variable_1(self):
        """Simple program: int main() {} """
        input = """
var a, b, a:integer; 

procedure main();
begin 
    foo();
end
"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_function_2(self):
        """Simple program: int main() {} """
        input = """
var a, b, c:integer; 

function a():integer;
begin
    b := 10;
end

procedure main();
begin 
    foo();
end
"""
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_redeclared_parameter_3(self):
        """Simple program: int main() {} """
        input = """
var a, b, d:integer; 

function c(a:integer; b:integer; c:integer):integer;
begin
end

procedure main();
begin 
    foo();
end
"""
        expect = "Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_redeclared_procedure_4(self):
        """Simple program: int main() {} """
        input = """
var a, b, c:integer; 

function foo():integer;
begin
    abcxyz();
end

procedure foo();
begin 
    foo();
end
"""
        expect = "Redeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_variable_5(self):
        """Simple program: int main() {} """
        input = """
var a, b, c:integer; 

function foo(b:integer):integer;
var a, b:integer;
begin
    abcxyz();
end

procedure main();
begin

end

"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    
    