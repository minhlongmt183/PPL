import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

# Redeclared Variable: 5
    def test_redeclared_variable_1(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi1, conbocuoi2:integer;

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,400))
        
    def test_redeclared_variable_2(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi1, conbocuoi2:integer;

function conbocuoi4(conbocuoi5:integer):integer;
var conbocuoi1:integer;
    conbocuoi1:real;
begin
    return 0;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_variable_3(self):
        """Simple program: int main() {} """
        input = """
        
var conbocuoi3, conbocuoi2:integer;
    conbocuoi3:array [1 .. 10] of real;
procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,402))
        
    def test_redeclared_variable_5(self):
        input = """
        
var conbocuoi5, conbocuoi2, conbocuoi3, conbocuoi5:integer;

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Variable: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,404))
        
    
# Redeclared Function: 5
    def test_redeclared_function_1(self):
        input = """
var conbocuoi1, conbocuoi2:integer;

function conbocuoi1(hihi:integer):integer;
begin
    return 10;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin 
    conbocuoi1();
end
"""
        expect = "Redeclared Function: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,405))
        
    def test_redeclared_function_2(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi2():integer;
begin
    return 10;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Function: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_function_3(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

function conbocuoi3():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin 
    return;
end
"""
        expect = "Redeclared Function: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,407))
        
    def test_redeclared_function_4(self):
        input = """
        
var conbocuoi4:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

function conbocuoi4():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin
    return;
end

procedure conbocuoi4();
begin
    return;
end
"""
        expect = "Redeclared Function: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_redeclared_function_5(self):
        input = """
        
var conbocuoi4:integer;

function conbocuoi3():integer;
begin
    return conbocuoi4();
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure conbocuoi5();
begin
    return;
end

function conbocuoi5():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi2:string;
begin
    return;
end
"""
        expect = "Redeclared Function: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,409))
        
# Redeclared Procedure: 5
    def test_redeclared_procedure_1(self):
        input = """
        
var conbocuoi1, conbocuoi2:integer;

procedure conbocuoi1(hihi:integer);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
begin 
    conbocuoi1();
end
"""
        expect = "Redeclared Procedure: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_redeclared_procedure_2(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

procedure conbocuoi2();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin 
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_procedure_3(self):
        input = """
        
var conbocuoi1:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

procedure conbocuoi3();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin 
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,412))
        
    def test_redeclared_procedure_4(self):
        input = """
        
var conbocuoi4:integer;

procedure conbocuoi2();
begin
    return;
end

function conbocuoi3():integer;
begin
    return 10;
end

procedure conbocuoi4();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end

function conbocuoi4():integer;
begin
    return 100;
end
"""
        expect = "Redeclared Procedure: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_redeclared_procedure_5(self):
        input = """
        
var conbocuoi4:integer;

function conbocuoi3():integer;
begin
    return conbocuoi4();
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure conbocuoi5();
begin
    return;
end

procedure conbocuoi5();
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Procedure: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,414))
        

# Redeclared Parameter: 5
    def test_redeclared_parameter_1(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi1:integer):integer;
begin
    return conbocuoi4;
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi1"
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_redeclared_parameter_2(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi6(1, "conbocuoi");
end

function conbocuoi6(conbocuoi2:integer; conbocuoi2:string):integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi2"
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_redeclared_parameter_3(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi3:integer; conbocuoi3:real):integer;
begin
    return conbocuoi4;
end

function conbocuoi6():integer;
begin
    return 100;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi3"
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_redeclared_parameter_4(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi4:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi4:array [1 .. 100] of real; conbocuoi4:string);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi4"
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_redeclared_parameter_5(self):
        input = """
var conbocuoi4:integer;

function conbocuoi3(conbocuoi1:string; conbocuoi2:integer):integer;
begin
    return conbocuoi4;
end

procedure conbocuoi6(conbocuoi5:integer; conbocuoi5:boolean);
begin
    return;
end

procedure main(); 
var conbocuoi1:integer;
    conbocuoi2:real;
    conbocuoi3:string;
begin
    return;
end
"""
        expect = "Redeclared Parameter: conbocuoi5"
        self.assertTrue(TestChecker.test(input,expect,419))
        