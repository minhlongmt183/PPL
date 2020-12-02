# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/lexical_analysis/parser/Q4.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\13\n\2\f\2\16\2")
        buf.write("\16\13\2\3\2\3\2\3\2\3\2\6\2\24\n\2\r\2\16\2\25\3\3\3")
        buf.write("\3\7\3\32\n\3\f\3\16\3\35\13\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3%\n\3\3\3\3\3\7\3)\n\3\f\3\16\3,\13\3\3\4\3\4\3\4")
        buf.write("\3\4\7\4\62\n\4\f\4\16\4\65\13\4\3\4\3\4\2\2\5\3\3\5\4")
        buf.write("\7\5\3\2\2\2>\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\f")
        buf.write("\3\2\2\2\5\33\3\2\2\2\7-\3\2\2\2\t\13\7c\2\2\n\t\3\2\2")
        buf.write("\2\13\16\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\17\3\2\2\2")
        buf.write("\16\f\3\2\2\2\17\20\7d\2\2\20\21\7d\2\2\21\23\3\2\2\2")
        buf.write("\22\24\7d\2\2\23\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\4\3\2\2\2\27\30\7c\2\2\30\32\7c\2")
        buf.write("\2\31\27\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34$\3\2\2\2\35\33\3\2\2\2\36\37\7c\2\2\37%\7c\2\2")
        buf.write(" !\7c\2\2!%\7d\2\2\"#\7d\2\2#%\7d\2\2$\36\3\2\2\2$ \3")
        buf.write("\2\2\2$\"\3\2\2\2%*\3\2\2\2&\'\7d\2\2\')\7d\2\2(&\3\2")
        buf.write("\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\6\3\2\2\2,*\3\2\2")
        buf.write("\2-\63\7c\2\2./\7c\2\2/\60\7c\2\2\60\62\7c\2\2\61.\3\2")
        buf.write("\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3")
        buf.write("\2\2\2\65\63\3\2\2\2\66\67\7d\2\2\67\b\3\2\2\2\t\2\f\25")
        buf.write("\33$*\63\2")
        return buf.getvalue()


class Q4Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    A = 1
    B = 2
    C = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "A", "B", "C" ]

    ruleNames = [ "A", "B", "C" ]

    grammarFileName = "Q4.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


