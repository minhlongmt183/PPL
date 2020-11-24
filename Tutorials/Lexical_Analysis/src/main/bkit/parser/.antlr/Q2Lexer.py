# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/lexical_analysis/parser/Q2.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\25\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\r\n\2")
        buf.write("\f\2\16\2\20\13\2\3\3\3\3\3\4\3\4\2\2\5\3\3\5\2\7\2\3")
        buf.write("\2\4\3\2c|\3\2\62;\2\24\2\3\3\2\2\2\3\t\3\2\2\2\5\21\3")
        buf.write("\2\2\2\7\23\3\2\2\2\t\16\5\5\3\2\n\r\5\5\3\2\13\r\5\7")
        buf.write("\4\2\f\n\3\2\2\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3\2\2")
        buf.write("\2\16\17\3\2\2\2\17\4\3\2\2\2\20\16\3\2\2\2\21\22\t\2")
        buf.write("\2\2\22\6\3\2\2\2\23\24\t\3\2\2\24\b\3\2\2\2\5\2\f\16")
        buf.write("\2")
        return buf.getvalue()


class Q2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Identifier = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "Identifier" ]

    ruleNames = [ "Identifier", "LOWER_LETTER", "DIGIT" ]

    grammarFileName = "Q2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


