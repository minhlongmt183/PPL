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
    foo(1, 1, 1 + True);
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_2(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c:integer);
begin
end

procedure main();
begin 
    foo(1, 1, 1 * True);
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(*,IntLiteral(1),BooleanLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_3(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c: real);
begin
end

procedure main();
begin 
    foo(1, 1, 2 + 10);
    foo(1, 1, -1 mod 0.2);
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(mod,UnaryOp(-,IntLiteral(1)),FloatLiteral(0.2))"
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_4(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c: real);
begin
end

function foo2(a:integer):integer;
begin
end

procedure main();
begin 
    foo(1, 1, foo2(10));
    foo(1, 1, -1 div False);
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(div,UnaryOp(-,IntLiteral(1)),BooleanLiteral(False))"
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_5(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c: real);
begin
end

function foo2(a:integer):integer;
begin
end

function foo1(a:boolean):boolean;
begin
end

procedure foo3(a:boolean);
begin
end

procedure main();
begin 
    foo(1, 1, foo2(10));
    foo3(foo1(foo1(True)));
    foo(1, 1, "conbocuoi");
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(1),IntLiteral(1),StringLiteral(conbocuoi)])"
        self.assertTrue(TestChecker.test(input,expect,404))

        
    def test_5(self):
        """Simple program: int main() {} """
        input = """
var a, b ,c:integer;

procedure foo(a:integer; b:integer; c: real);
begin
end

function foo2(a:integer):integer;
begin
end

function foo1(a:boolean):boolean;
begin
end

procedure foo3(a:boolean);
begin
end

procedure main();
begin 
    foo(1, 1, foo2(10) + a + b);
    foo3(foo1(foo1(True)));
    foo(1, 1, "conbocuoi");
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(1),IntLiteral(1),StringLiteral(conbocuoi)])"
        self.assertTrue(TestChecker.test(input,expect,400))
        

        
        