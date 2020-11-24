import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

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