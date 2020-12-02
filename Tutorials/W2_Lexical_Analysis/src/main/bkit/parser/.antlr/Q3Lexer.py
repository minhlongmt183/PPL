# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/lexical_analysis/parser/Q3.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2\5\2\30\n\2\3\3\5\3\33")
        buf.write("\n\3\3\3\3\3\7\3\37\n\3\f\3\16\3\"\13\3\3\3\5\3%\n\3\3")
        buf.write("\4\3\4\6\4)\n\4\r\4\16\4*\3\5\3\5\3\5\3\5\6\5\61\n\5\r")
        buf.write("\5\16\5\62\3\6\3\6\3\7\3\7\3\7\7\7:\n\7\f\7\16\7=\13\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\2\2\t\3\3\5\2\7\2\t\2\13\2\r\4\17")
        buf.write("\2\3\2\5\3\2\63;\3\2\62;\3\2))\2F\2\3\3\2\2\2\2\r\3\2")
        buf.write("\2\2\3\21\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2\t,\3\2\2\2\13")
        buf.write("\64\3\2\2\2\r\66\3\2\2\2\17@\3\2\2\2\21\27\5\5\3\2\22")
        buf.write("\30\5\7\4\2\23\30\5\t\5\2\24\25\5\7\4\2\25\26\5\t\5\2")
        buf.write("\26\30\3\2\2\2\27\22\3\2\2\2\27\23\3\2\2\2\27\24\3\2\2")
        buf.write("\2\30\4\3\2\2\2\31\33\7/\2\2\32\31\3\2\2\2\32\33\3\2\2")
        buf.write("\2\33\34\3\2\2\2\34 \t\2\2\2\35\37\5\13\6\2\36\35\3\2")
        buf.write("\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!%\3\2\2\2\" \3")
        buf.write("\2\2\2#%\7\62\2\2$\32\3\2\2\2$#\3\2\2\2%\6\3\2\2\2&(\7")
        buf.write("\60\2\2\')\5\13\6\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3")
        buf.write("\2\2\2+\b\3\2\2\2,-\7g\2\2-.\7/\2\2.\60\3\2\2\2/\61\5")
        buf.write("\13\6\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\n\3\2\2\2\64\65\t\3\2\2\65\f\3\2\2\2\66;\7")
        buf.write(")\2\2\67:\5\17\b\28:\n\4\2\29\67\3\2\2\298\3\2\2\2:=\3")
        buf.write("\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7)\2")
        buf.write("\2?\16\3\2\2\2@A\7)\2\2AB\7)\2\2B\20\3\2\2\2\13\2\27\32")
        buf.write(" $*\629;\2")
        return buf.getvalue()


class Q3Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REAL = 1
    STR = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "REAL", "STR" ]

    ruleNames = [ "REAL", "INT_PART", "DEC_PART", "EPX_PART", "DIGIT", "STR", 
                  "DOUBLE_QUOTE" ]

    grammarFileName = "Q3.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


