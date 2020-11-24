import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var: x;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,201))
    
    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_case_1(self):
        """Successful program"""
        input = """float a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2001))

    def test_case_2(self):
        """Successful program"""
        input = """int a, b, c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2002))

    def test_case_3(self):
        """Successful program"""
        input = """int a, b; float c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2003))

    def test_case_4(self):
        """Successful program"""
        input = """float foo(int a; float c, d) {\n\tint e;\n\te = a + 4 ;\n\tc = a * d / 2.0;\n\treturn c + 1;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2004))
    
    def test_case_5(self):
        """Successful program"""
        input = """int temp(int c) {\n\treturn c + 1;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2005))

    def test_case_6(self):
        """Successful program"""
        input = """float calculateSum(int a, b) {\n\tint result; \n\t result = a + b;\n\treturn result;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2006))
    
    def test_case_7(self):
        """Successful program"""
        input = """int a, b; float c, d; int temp, result"""
        expect = "Error on line 1 col 38: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,2007))

    def test_case_8(self):
        """Successful program"""
        input = """int returnValue(int a) {\n\treturn a;\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2008))

    def test_case_9(self):
        """Successful program"""
        input = """float foo(float a, b) {\n\t return foo(1, a, b);\n}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2009))

    def test_case_10(self):
        """Successful program"""
        input = """int abc, def, xzy;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,2010))