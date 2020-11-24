import re, sys
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    # Get all solutions
    solution_files = [f for f in listdir('test/solutions/') if isfile(join('test/solutions', f)) and f.endswith('.txt')]
    print(solution_files)
    dic = {}
    for f in solution_files:
        with open('test/solutions/' + f, 'r', encoding='windows-1252') as fileSolution:
            dic[f[:-4]] = fileSolution.read()[1:-1]

# Program
    # Read old ASTGenSuite
    with open('test/ASTGenSuite.py','r') as astgensuite:
        ASTGenSuite = astgensuite.read()
    defList = ASTGenSuite.split("def ")

    # Change expect
    for i in range(1,len(defList)):
        testcaseid = re.findall(r'self.assertTrue\(TestAST.checkASTGen\(input, expect,(.+)\)\)',defList[i])
        if testcaseid:
            testcaseid = testcaseid[0].replace(' ','')
        defList[i] = re.sub(r'(?is)expect =(.+?)\n', 'expect = ' + dic[testcaseid] + '\n', defList[i])
        # Change
        if len(sys.argv) == 2 and sys.argv[1] == '--fix-index':
            defList[i] = re.sub(r'(?is)self.assertTrue\(TestAST.checkASTGen\(input, expect,(.+)\)\)\n', "self.assertTrue(TestAST.checkASTGen(input, expect,{index}))\n".format(index=str(int(testcaseid)+100)), defList[i])

    # Fix somethings
    newASTGenSuite = 'def '.join(defList)
    newASTGenSuite = re.sub(r'(?is)\\\'', "\\\\'", newASTGenSuite)
    newASTGenSuite = re.sub(r'(?is)<AST.Break(.+?)>', "Break()", newASTGenSuite)
    newASTGenSuite = re.sub(r'(?is)<AST.Continue(.+?)>', "Continue()", newASTGenSuite)
    # print(newASTGenSuite)
    with open('_ASTGenSuite.py','w') as _ASTGenSuite:
        _ASTGenSuite.write(newASTGenSuite)
    print("[*] ASTGenSuite generated: _ASTGenSuite")