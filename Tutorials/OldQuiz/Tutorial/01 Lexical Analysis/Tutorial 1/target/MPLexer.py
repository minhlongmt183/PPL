# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("~\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\7\5-\n\5\f\5\16\5\60\13\5\3\6\3\6\3")
        buf.write("\7\6\7\65\n\7\r\7\16\7\66\3\7\3\7\6\7;\n\7\r\7\16\7<\5")
        buf.write("\7?\n\7\3\7\3\7\3\7\5\7D\n\7\3\7\6\7G\n\7\r\7\16\7H\5")
        buf.write("\7K\n\7\3\b\3\b\6\bO\n\b\r\b\16\bP\3\b\3\b\3\b\5\bV\n")
        buf.write("\b\3\b\6\bY\n\b\r\b\16\bZ\5\b]\n\b\3\t\3\t\5\ta\n\t\3")
        buf.write("\n\3\n\3\13\3\13\7\13g\n\13\f\13\16\13j\13\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\6\16s\n\16\r\16\16\16t\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\2\2\22\3\2\5\2\7\2\t\3")
        buf.write("\13\2\r\2\17\2\21\4\23\2\25\5\27\6\31\7\33\b\35\t\37\n")
        buf.write("!\13\3\2\b\3\2c|\3\2C\\\3\2\62;\4\2GGgg\3\2\"\u0080\5")
        buf.write("\2\13\f\17\17\"\"\2\u0085\2\t\3\2\2\2\2\21\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7")
        buf.write("\'\3\2\2\2\t)\3\2\2\2\13\61\3\2\2\2\r\64\3\2\2\2\17L\3")
        buf.write("\2\2\2\21`\3\2\2\2\23b\3\2\2\2\25d\3\2\2\2\27m\3\2\2\2")
        buf.write("\31o\3\2\2\2\33r\3\2\2\2\35x\3\2\2\2\37z\3\2\2\2!|\3\2")
        buf.write("\2\2#$\t\2\2\2$\4\3\2\2\2%&\t\3\2\2&\6\3\2\2\2\'(\t\4")
        buf.write("\2\2(\b\3\2\2\2).\5\3\2\2*-\5\3\2\2+-\5\7\4\2,*\3\2\2")
        buf.write("\2,+\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\n\3\2\2")
        buf.write("\2\60.\3\2\2\2\61\62\t\5\2\2\62\f\3\2\2\2\63\65\5\7\4")
        buf.write("\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\67>\3\2\2\28:\7\60\2\29;\5\7\4\2:9\3\2\2\2;<\3\2")
        buf.write("\2\2<:\3\2\2\2<=\3\2\2\2=?\3\2\2\2>8\3\2\2\2>?\3\2\2\2")
        buf.write("?J\3\2\2\2@C\5\13\6\2AD\5\27\f\2BD\5\31\r\2CA\3\2\2\2")
        buf.write("CB\3\2\2\2DF\3\2\2\2EG\5\7\4\2FE\3\2\2\2GH\3\2\2\2HF\3")
        buf.write("\2\2\2HI\3\2\2\2IK\3\2\2\2J@\3\2\2\2JK\3\2\2\2K\16\3\2")
        buf.write("\2\2LN\7\60\2\2MO\5\7\4\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2")
        buf.write("\2PQ\3\2\2\2Q\\\3\2\2\2RU\5\13\6\2SV\5\27\f\2TV\5\31\r")
        buf.write("\2US\3\2\2\2UT\3\2\2\2VX\3\2\2\2WY\5\7\4\2XW\3\2\2\2Y")
        buf.write("Z\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2\\R\3\2\2\2\\]")
        buf.write("\3\2\2\2]\20\3\2\2\2^a\5\r\7\2_a\5\17\b\2`^\3\2\2\2`_")
        buf.write("\3\2\2\2a\22\3\2\2\2bc\t\6\2\2c\24\3\2\2\2dh\7)\2\2eg")
        buf.write("\5\23\n\2fe\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3")
        buf.write("\2\2\2jh\3\2\2\2kl\7)\2\2l\26\3\2\2\2mn\7-\2\2n\30\3\2")
        buf.write("\2\2op\7/\2\2p\32\3\2\2\2qs\t\7\2\2rq\3\2\2\2st\3\2\2")
        buf.write("\2tr\3\2\2\2tu\3\2\2\2uv\3\2\2\2vw\b\16\2\2w\34\3\2\2")
        buf.write("\2xy\13\2\2\2y\36\3\2\2\2z{\13\2\2\2{ \3\2\2\2|}\13\2")
        buf.write("\2\2}\"\3\2\2\2\22\2,.\66<>CHJPUZ\\`ht\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    REALLIT = 2
    STRINGLIT = 3
    ADD_OP = 4
    SUB_OP = 5
    WS = 6
    ERROR_CHAR = 7
    UNCLOSE_STRING = 8
    ILLEGAL_ESCAPE = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "REALLIT", "STRINGLIT", "ADD_OP", "SUB_OP", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "LOWERCASE", "UPPERCASE", "DIGIT", "IDENTIFIER", "E", 
                  "Real_type_1", "Real_type_2", "REALLIT", "CHAR", "STRINGLIT", 
                  "ADD_OP", "SUB_OP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


