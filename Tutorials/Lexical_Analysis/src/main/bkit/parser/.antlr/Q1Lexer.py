# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/lexical_analysis/parser/Q1.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\f\b\1\4\2\t\2\3\2\3\2\7\2\b\n\2\f\2\16\2\13\13\2\2\2")
        buf.write("\3\3\3\3\2\4\3\2c|\4\2\62;c|\2\f\2\3\3\2\2\2\3\5\3\2\2")
        buf.write("\2\5\t\t\2\2\2\6\b\t\3\2\2\7\6\3\2\2\2\b\13\3\2\2\2\t")
        buf.write("\7\3\2\2\2\t\n\3\2\2\2\n\4\3\2\2\2\13\t\3\2\2\2\4\2\t")
        buf.write("\2")
        return buf.getvalue()


class Q1Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT" ]

    ruleNames = [ "INT" ]

    grammarFileName = "Q1.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


