import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_1(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c:integer);
begin
end

procedure main();
begin 
    foo(1, 1, 1.0);
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(1),IntLiteral(1),FloatLiteral(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_2(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c:real);
begin
end

procedure foo2(a:integer; b:integer; c:integer);
begin
end

procedure main();
begin 
    foo(1, 1, 1);
    foo2(1.0, 1, 1);
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2),[FloatLiteral(1.0),IntLiteral(1),IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_3(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c:real);
begin
end

procedure foo2(a:boolean; b:integer; c:integer);
begin
end

function foo3(c:boolean):boolean;
begin
end

procedure main();
begin 
    foo2(foo3(True), 1, 1);
    foo2(1.0);
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo2),[FloatLiteral(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,400))
        