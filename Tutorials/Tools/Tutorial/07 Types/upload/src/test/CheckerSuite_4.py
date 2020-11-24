import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_TMIS_PROCEDURE_1(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,460))
        
    def test_TMIS_PROCEDURE_2(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi2, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi2),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_TMIS_PROCEDURE_3(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:integer; conbocuoi6:real; conbocuoi8:boolean);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi, conbocuoi2, conbocuoi1);
    conbocuoi6(conbocuoi, conbocuoi, conbocuoi1);
    conbocuoi6(conbocuoi1, conbocuoi2, conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi1),Id(conbocuoi2),Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_TMIS_PROCEDURE_4(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi8:array [1 .. 100] of integer);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:array[1 .. 100] of integer;
    conbocuoi2:array[1 .. 100] of real;
    conbocuoi1:boolean;
begin
    conbocuoi6(conbocuoi);
    conbocuoi6(conbocuoi2);
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi2)])"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_TMIS_PROCEDURE_5(self):
        input = """
var conbocuoi4:integer;
    conbocuoi5:boolean;

procedure conbocuoi6(conbocuoi5:string);
var conbocuoi, conbocuoi7:integer;
    conbocuoi3:boolean;
begin

    return;
end

procedure main(); 
var conbocuoi:integer;
    conbocuoi2:real;
    conbocuoi1:boolean;
begin
    conbocuoi6("123123123");
    conbocuoi6("buon ngu qua hu hu");
    conbocuoi6(conbocuoi, "hehe");
    return;
end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(conbocuoi6),[Id(conbocuoi),StringLiteral(hehe)])"
        self.assertTrue(TestChecker.test(input,expect,464))
        
# TMIE Bin Exp: 5
    def test_TMIE_BIN_1(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 + c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 - c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,470))
        
    def test_TMIE_BIN_2(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 - c1;
    c2 := c1 * c2;
    c2 := c1 / c1;
    c2 := c2 + c2;
    c3 := c3 and c3;
    c3 := c1 / c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(/,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_TMIE_BIN_3(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 + c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 and then c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(andthen,Id(c1),Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_TMIE_BIN_4(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 div c1;
    c2 := c1 + c2;
    c2 := c1 + c1;
    c2 := c2 + c2;
    c3 := c1 > c2;
    c3 := c1 <= c2;
    c3 := c1 mod c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(mod,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_TMIE_BIN_5(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := c1 mod c1;
    c2 := c1 + c2;
    c3 := c2 <> c1;
    c3 := c1 div c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: BinaryOp(div,Id(c1),Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,474))

# TMIE Un Exp: 5
    def test_TMIE_UN_1(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := -c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_TMIE_UN_2(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := -c3;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c3))"
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_TMIE_UN_3(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not c4;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(c4))"
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_TMIE_UN_4(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not c1;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(not,Id(c1))"
        self.assertTrue(TestChecker.test(input,expect,478))
        
    def test_TMIE_UN_5(self):
        input = """
procedure main(); 
var c1:integer;
    c2:real;
    c3:boolean;
    c4:string;
begin
    c1 := -c1;
    c2 := -c2;
    c3 := not c3;
    c1 := not - not False;
    return;
end
"""
        expect = "Type Mismatch In Expression: UnaryOp(-,UnaryOp(not,BooleanLiteral(False)))"
        self.assertTrue(TestChecker.test(input,expect,479))

# TMIE Function Call: 5
    def test_TMIE_FUNC_1(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi1(c2);
    return;
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(conbocuoi1),[Id(c2)])"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_TMIE_FUNC_2(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi2(c3);
    return;
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(conbocuoi2),[Id(c3)])"
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_TMIE_FUNC_3(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi3(c4);
    return;
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(conbocuoi3),[Id(c4)])"
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_TMIE_FUNC_4(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi4(c4)[10];
    c2 := conbocuoi3(c4);
    return;
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(conbocuoi3),[Id(c4)])"
        self.assertTrue(TestChecker.test(input,expect,483))
        
    def test_TMIE_FUNC_5(self):
        input = """
function conbocuoi1(conbocuoi:integer):integer;
begin
    return 1;
end

function conbocuoi2(conbocuoi:real):real;
begin
    return 1.0;
end

function conbocuoi3(conbocuoi:string):string;
begin
    return "conbocuoi";
end

function conbocuoi4(conbocuoi:array[1 .. 100] of integer):array[1 .. 100] of integer;
begin
    return conbocuoi;
end

function conbocuoi5(conbocuoi:boolean):boolean;
begin
    return True;
end

procedure main(); 
var c1:integer;
    c2:real;
    c5:boolean;
    c3:string;
    c4:array[1 .. 100] of integer;
begin
    c1 := conbocuoi1(c1);
    c2 := conbocuoi2(c2);
    c5 := conbocuoi5(c5);
    c1 := conbocuoi1(c2);
    return;
end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(conbocuoi1),[Id(c2)])"
        self.assertTrue(TestChecker.test(input,expect,484))
