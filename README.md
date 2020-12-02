# PPL

## Project Structure
```
.
├── Assignment1
│   ├── Ass1.md
│   ├── assignment1
│   │   ├── gen
│   │   │   ├── BKIT.interp
│   │   │   ├── BKITLexer.interp
│   │   │   ├── BKITLexer.py
│   │   │   ├── BKITLexer.tokens
│   │   │   ├── BKITListener.py
│   │   │   ├── BKITParser.py
│   │   │   ├── BKIT.tokens
│   │   │   └── BKITVisitor.py
│   │   ├── README.txt
│   │   ├── src
│   │   │   ├── gen
│   │   │   │   ├── BKIT.interp
│   │   │   │   ├── BKITLexer.interp
│   │   │   │   ├── BKITLexer.py
│   │   │   │   ├── BKITLexer.tokens
│   │   │   │   ├── BKITListener.py
│   │   │   │   ├── BKITParser.py
│   │   │   │   ├── BKIT.tokens
│   │   │   │   └── BKITVisitor.py
│   │   │   ├── main
│   │   │   │   └── bkit
│   │   │   │       ├── astgen
│   │   │   │       ├── checker
│   │   │   │       ├── parser
│   │   │   │       │   ├── BKIT.g4
│   │   │   │       │   ├── lexererr.py
│   │   │   │       │   └── __pycache__
│   │   │   │       │       ├── lexererr.cpython-36.pyc
│   │   │   │       │       ├── lexererr.cpython-37.pyc
│   │   │   │       │       └── lexererr.cpython-38.pyc
│   │   │   │       └── utils
│   │   │   ├── run.py
│   │   │   └── test
│   │   │       ├── LexerSuite.py
│   │   │       ├── ParserSuite.py
│   │   │       ├── __pycache__
│   │   │       │   ├── LexerSuite.cpython-36.pyc
│   │   │       │   ├── LexerSuite.cpython-37.pyc
│   │   │       │   ├── LexerSuite.cpython-38.pyc
│   │   │       │   ├── ParserSuite.cpython-36.pyc
│   │   │       │   ├── ParserSuite.cpython-37.pyc
│   │   │       │   ├── ParserSuite.cpython-38.pyc
│   │   │       │   ├── TestUtils.cpython-36.pyc
│   │   │       │   ├── TestUtils.cpython-37.pyc
│   │   │       │   └── TestUtils.cpython-38.pyc
│   │   │       ├── solutions
│   │   │       ├── testcases
│   │   │       └── TestUtils.py
│   │   └── target
│   │       └── main
│   │           └── bkit
│   │               └── parser
│   │                   ├── BKIT.interp
│   │                   ├── BKITLexer.interp
│   │                   ├── BKITLexer.py
│   │                   ├── BKITLexer.tokens
│   │                   ├── BKITParser.py
│   │                   ├── BKIT.tokens
│   │                   ├── BKITVisitor.py
│   │                   └── __pycache__
│   │                       ├── BKITLexer.cpython-38.pyc
│   │                       └── BKITParser.cpython-38.pyc
│   ├── assignment1.pdf
│   ├── initial.zip
│   ├── lib
│   │   └── antlr-4.8-complete.jar
│   └── __MACOSX
│       └── initial
│           └── src
│               ├── main
│               │   └── bkit
│               │       └── parser
│               │           └── __pycache__
│               └── test
│                   ├── __pycache__
│                   ├── solutions
│                   └── testcases
├── assignment2
│   ├── assignment2.pdf
│   ├── assignment2.zip
│   ├── genTestCase
│   │   ├── README.txt
│   │   ├── src
│   │   │   ├── expect.txt
│   │   │   ├── main
│   │   │   │   └── bkit
│   │   │   │       ├── astgen
│   │   │   │       │   ├── ASTGeneration.py
│   │   │   │       │   └── __pycache__
│   │   │   │       │       ├── ASTGeneration.cpython-37.pyc
│   │   │   │       │       └── ASTGeneration.cpython-38.pyc
│   │   │   │       ├── checker
│   │   │   │       ├── parser
│   │   │   │       │   ├── BKIT.g4
│   │   │   │       │   ├── lexererr.py
│   │   │   │       │   └── __pycache__
│   │   │   │       │       ├── lexererr.cpython-36.pyc
│   │   │   │       │       ├── lexererr.cpython-37.pyc
│   │   │   │       │       └── lexererr.cpython-38.pyc
│   │   │   │       └── utils
│   │   │   │           ├── AST.py
│   │   │   │           ├── __pycache__
│   │   │   │           │   ├── AST.cpython-37.pyc
│   │   │   │           │   ├── AST.cpython-38.pyc
│   │   │   │           │   ├── Visitor.cpython-37.pyc
│   │   │   │           │   └── Visitor.cpython-38.pyc
│   │   │   │           └── Visitor.py
│   │   │   ├── run.py
│   │   │   └── test
│   │   │       ├── ASTGenSuite.py
│   │   │       ├── LexerSuite.py
│   │   │       ├── ParserSuite.py
│   │   │       ├── __pycache__
│   │   │       │   ├── ASTGenSuite.cpython-37.pyc
│   │   │       │   ├── ASTGenSuite.cpython-38.pyc
│   │   │       │   ├── LexerSuite.cpython-36.pyc
│   │   │       │   ├── LexerSuite.cpython-37.pyc
│   │   │       │   ├── LexerSuite.cpython-38.pyc
│   │   │       │   ├── ParserSuite.cpython-36.pyc
│   │   │       │   ├── ParserSuite.cpython-37.pyc
│   │   │       │   ├── ParserSuite.cpython-38.pyc
│   │   │       │   ├── TestUtils.cpython-36.pyc
│   │   │       │   ├── TestUtils.cpython-37.pyc
│   │   │       │   └── TestUtils.cpython-38.pyc
│   │   │       ├── solutions
│   │   │       ├── testcases
│   │   │       └── TestUtils.py
│   │   └── target
│   │       └── main
│   │           └── bkit
│   │               └── parser
│   │                   ├── BKIT.interp
│   │                   ├── BKITLexer.interp
│   │                   ├── BKITLexer.py
│   │                   ├── BKITLexer.tokens
│   │                   ├── BKITParser.py
│   │                   ├── BKIT.tokens
│   │                   ├── BKITVisitor.py
│   │                   └── __pycache__
│   │                       ├── BKITLexer.cpython-38.pyc
│   │                       ├── BKITParser.cpython-38.pyc
│   │                       └── BKITVisitor.cpython-38.pyc
│   ├── initial
│   │   ├── README.txt
│   │   ├── src
│   │   │   ├── _ASTGenSuite.py
│   │   │   ├── main
│   │   │   │   └── bkit
│   │   │   │       ├── astgen
│   │   │   │       │   ├── ASTGeneration.py
│   │   │   │       │   └── __pycache__
│   │   │   │       │       ├── ASTGeneration.cpython-37.pyc
│   │   │   │       │       └── ASTGeneration.cpython-38.pyc
│   │   │   │       ├── checker
│   │   │   │       ├── parser
│   │   │   │       │   ├── BKIT.g4
│   │   │   │       │   ├── lexererr.py
│   │   │   │       │   └── __pycache__
│   │   │   │       │       ├── lexererr.cpython-36.pyc
│   │   │   │       │       ├── lexererr.cpython-37.pyc
│   │   │   │       │       └── lexererr.cpython-38.pyc
│   │   │   │       └── utils
│   │   │   │           ├── AST.py
│   │   │   │           ├── __pycache__
│   │   │   │           │   ├── AST.cpython-37.pyc
│   │   │   │           │   ├── AST.cpython-38.pyc
│   │   │   │           │   ├── Visitor.cpython-37.pyc
│   │   │   │           │   └── Visitor.cpython-38.pyc
│   │   │   │           └── Visitor.py
│   │   │   ├── README.md
│   │   │   ├── run.py
│   │   │   ├── test
│   │   │   │   ├── ASTGenSuite.py
│   │   │   │   ├── LexerSuite.py
│   │   │   │   ├── ParserSuite.py
│   │   │   │   ├── __pycache__
│   │   │   │   │   ├── ASTGenSuite.cpython-37.pyc
│   │   │   │   │   ├── ASTGenSuite.cpython-38.pyc
│   │   │   │   │   ├── LexerSuite.cpython-36.pyc
│   │   │   │   │   ├── LexerSuite.cpython-37.pyc
│   │   │   │   │   ├── LexerSuite.cpython-38.pyc
│   │   │   │   │   ├── ParserSuite.cpython-36.pyc
│   │   │   │   │   ├── ParserSuite.cpython-37.pyc
│   │   │   │   │   ├── ParserSuite.cpython-38.pyc
│   │   │   │   │   ├── TestUtils.cpython-36.pyc
│   │   │   │   │   ├── TestUtils.cpython-37.pyc
│   │   │   │   │   └── TestUtils.cpython-38.pyc
│   │   │   │   ├── solutions
│   │   │   │   ├── testcases
│   │   │   │   └── TestUtils.py
│   │   │   └── toolkit.py
│   │   └── target
│   │       └── main
│   │           └── bkit
│   │               └── parser
│   │                   ├── BKIT.interp
│   │                   ├── BKITLexer.interp
│   │                   ├── BKITLexer.py
│   │                   ├── BKITLexer.tokens
│   │                   ├── BKITParser.py
│   │                   ├── BKIT.tokens
│   │                   ├── BKITVisitor.py
│   │                   └── __pycache__
│   │                       ├── BKITLexer.cpython-38.pyc
│   │                       ├── BKITParser.cpython-38.pyc
│   │                       └── BKITVisitor.cpython-38.pyc
│   ├── __MACOSX
│   │   └── initial
│   │       └── src
│   │           ├── main
│   │           │   └── bkit
│   │           │       ├── astgen
│   │           │       ├── parser
│   │           │       │   └── __pycache__
│   │           │       └── utils
│   │           └── test
│   │               ├── __pycache__
│   │               ├── solutions
│   │               └── testcases
│   └── Submit
│       ├── ASTGeneration.py
│       ├── ASTGenSuite.py
│       └── BKIT.g4
├── assignment3
│   ├── assignment3.zip
│   ├── initial
│   │   ├── README.txt
│   │   └── src
│   │       ├── main
│   │       │   └── bkit
│   │       │       ├── astgen
│   │       │       │   ├── ASTGeneration.py
│   │       │       │   └── __pycache__
│   │       │       │       ├── ASTGeneration.cpython-37.pyc
│   │       │       │       └── ASTGeneration.cpython-38.pyc
│   │       │       ├── checker
│   │       │       │   ├── __pycache__
│   │       │       │   │   ├── StaticCheck.cpython-37.pyc
│   │       │       │   │   ├── StaticCheck.cpython-38.pyc
│   │       │       │   │   ├── StaticError.cpython-37.pyc
│   │       │       │   │   └── StaticError.cpython-38.pyc
│   │       │       │   ├── StaticCheck.py
│   │       │       │   └── StaticError.py
│   │       │       ├── parser
│   │       │       │   ├── BKIT.g4
│   │       │       │   ├── lexererr.py
│   │       │       │   └── __pycache__
│   │       │       │       ├── lexererr.cpython-36.pyc
│   │       │       │       ├── lexererr.cpython-37.pyc
│   │       │       │       └── lexererr.cpython-38.pyc
│   │       │       └── utils
│   │       │           ├── AST.py
│   │       │           ├── __pycache__
│   │       │           │   ├── AST.cpython-37.pyc
│   │       │           │   ├── AST.cpython-38.pyc
│   │       │           │   ├── Utils.cpython-37.pyc
│   │       │           │   ├── Visitor.cpython-37.pyc
│   │       │           │   └── Visitor.cpython-38.pyc
│   │       │           └── Visitor.py
│   │       ├── run.py
│   │       └── test
│   │           ├── ASTGenSuite.py
│   │           ├── CheckSuite.py
│   │           ├── LexerSuite.py
│   │           ├── ParserSuite.py
│   │           ├── __pycache__
│   │           │   ├── ASTGenSuite.cpython-37.pyc
│   │           │   ├── CheckSuite.cpython-37.pyc
│   │           │   ├── CheckSuite.cpython-38.pyc
│   │           │   ├── LexerSuite.cpython-36.pyc
│   │           │   ├── LexerSuite.cpython-37.pyc
│   │           │   ├── ParserSuite.cpython-36.pyc
│   │           │   ├── ParserSuite.cpython-37.pyc
│   │           │   ├── TestUtils.cpython-36.pyc
│   │           │   ├── TestUtils.cpython-37.pyc
│   │           │   └── TestUtils.cpython-38.pyc
│   │           ├── solutions
│   │           │   ├── 400.txt
│   │           │   ├── 401.txt
│   │           │   ├── 402.txt
│   │           │   ├── 403.txt
│   │           │   ├── 404.txt
│   │           │   └── 405.txt
│   │           ├── testcases
│   │           │   ├── 400.txt
│   │           │   ├── 401.txt
│   │           │   ├── 402.txt
│   │           │   ├── 403.txt
│   │           │   ├── 404.txt
│   │           │   └── 405.txt
│   │           └── TestUtils.py
│   └── __MACOSX
│       └── initial
│           └── src
│               ├── main
│               │   └── bkit
│               │       ├── astgen
│               │       ├── checker
│               │       ├── parser
│               │       │   └── __pycache__
│               │       └── utils
│               └── test
│                   ├── __pycache__
│                   ├── solutions
│                   └── testcases
└── BKIT2009_Specification-2.1.pdf

119 directories, 191 files

```