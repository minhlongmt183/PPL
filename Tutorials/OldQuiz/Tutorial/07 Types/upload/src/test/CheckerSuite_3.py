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
        
