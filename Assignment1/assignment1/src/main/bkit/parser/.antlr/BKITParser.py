# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Assignments/Assignment1/assignment1/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\24\2\2\5\6\7-\2\2\6\7\7\3\2\2\7\b")
        buf.write("\7*\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Body'", "'Break'", "'Continue'", 
                     "'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", 
                     "'EndFor'", "'EndWhile'", "'For'", "'Function'", "'If'", 
                     "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'+'", "'-'", "'*'", 
                     "'/'", "'='", "'<>'", "'<'", "'<='", "'>='", "'>'", 
                     "':='", "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", 
                     "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "IDENT", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", 
                      "EndDO", "PLUS", "MINUS", "STAR", "SLASH", "EQUAL", 
                      "NOT_EQUAL", "LT", "LE", "GE", "GT", "ASSIGN", "LCURLY", 
                      "RCURLY", "LR", "RR", "LB", "RB", "SEMI", "DOT", "COMMA", 
                      "COLON", "INT_LIT", "DEC", "OCT", "HEX", "FLOAT_LIT", 
                      "INT_PART", "DEC_PART", "EXP_PART", "BOOL_LIT", "STRING_LIT", 
                      "UNCLOSE_STRING", "ARRAY_LIT", "ELEM_LIT", "SUB_ARRAY", 
                      "ELEM_VAL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    IDENT=1
    BODY=2
    BREAK=3
    CONTINUE=4
    DO=5
    ELSE=6
    ELSEIF=7
    ENDBODY=8
    ENDIF=9
    ENDFOR=10
    ENDWHILE=11
    FOR=12
    FUNCTION=13
    IF=14
    PARAMETER=15
    RETURN=16
    THEN=17
    VAR=18
    WHILE=19
    TRUE=20
    FALSE=21
    EndDO=22
    PLUS=23
    MINUS=24
    STAR=25
    SLASH=26
    EQUAL=27
    NOT_EQUAL=28
    LT=29
    LE=30
    GE=31
    GT=32
    ASSIGN=33
    LCURLY=34
    RCURLY=35
    LR=36
    RR=37
    LB=38
    RB=39
    SEMI=40
    DOT=41
    COMMA=42
    COLON=43
    INT_LIT=44
    DEC=45
    OCT=46
    HEX=47
    FLOAT_LIT=48
    INT_PART=49
    DEC_PART=50
    EXP_PART=51
    BOOL_LIT=52
    STRING_LIT=53
    UNCLOSE_STRING=54
    ARRAY_LIT=55
    ELEM_LIT=56
    SUB_ARRAY=57
    ELEM_VAL=58
    WS=59
    ERROR_CHAR=60
    ILLEGAL_ESCAPE=61
    UNTERMINATED_COMMENT=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.IDENT)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





