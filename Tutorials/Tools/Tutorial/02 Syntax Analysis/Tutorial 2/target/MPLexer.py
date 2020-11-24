# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\u0099\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\6\2/\n\2\r\2\16")
        buf.write("\2\60\3\2\3\2\3\3\6\3\66\n\3\r\3\16\3\67\3\4\6\4;\n\4")
        buf.write("\r\4\16\4<\3\4\3\4\7\4A\n\4\f\4\16\4D\13\4\5\4F\n\4\3")
        buf.write("\4\5\4I\n\4\3\4\3\4\6\4M\n\4\r\4\16\4N\5\4Q\n\4\3\4\3")
        buf.write("\4\6\4U\n\4\r\4\16\4V\3\4\5\4Z\n\4\3\4\3\4\6\4^\n\4\r")
        buf.write("\4\16\4_\5\4b\n\4\5\4d\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\7\23\u008f")
        buf.write("\n\23\f\23\16\23\u0092\13\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27\3\2\b\5\2\13\f\17\17\"\"\3\2\62;\3\2//\4\2GGgg\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\2\u00a6\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\3.\3\2\2\2\5\65\3\2\2\2\7c\3\2\2")
        buf.write("\2\te\3\2\2\2\13i\3\2\2\2\ro\3\2\2\2\17v\3\2\2\2\21x\3")
        buf.write("\2\2\2\23z\3\2\2\2\25|\3\2\2\2\27~\3\2\2\2\31\u0080\3")
        buf.write("\2\2\2\33\u0082\3\2\2\2\35\u0084\3\2\2\2\37\u0086\3\2")
        buf.write("\2\2!\u0088\3\2\2\2#\u008a\3\2\2\2%\u008c\3\2\2\2\'\u0093")
        buf.write("\3\2\2\2)\u0095\3\2\2\2+\u0097\3\2\2\2-/\t\2\2\2.-\3\2")
        buf.write("\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2")
        buf.write("\2\62\63\b\2\2\2\63\4\3\2\2\2\64\66\t\3\2\2\65\64\3\2")
        buf.write("\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\6\3\2\2")
        buf.write("\29;\t\3\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=")
        buf.write("E\3\2\2\2>B\7\60\2\2?A\t\3\2\2@?\3\2\2\2AD\3\2\2\2B@\3")
        buf.write("\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2E>\3\2\2\2EF\3\2\2")
        buf.write("\2FP\3\2\2\2GI\t\4\2\2HG\3\2\2\2HI\3\2\2\2IJ\3\2\2\2J")
        buf.write("L\t\5\2\2KM\t\3\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3")
        buf.write("\2\2\2OQ\3\2\2\2PH\3\2\2\2PQ\3\2\2\2Qd\3\2\2\2RT\7\60")
        buf.write("\2\2SU\t\3\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2")
        buf.write("Wa\3\2\2\2XZ\t\4\2\2YX\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[]\t")
        buf.write("\5\2\2\\^\t\3\2\2]\\\3\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2")
        buf.write("\2\2`b\3\2\2\2aY\3\2\2\2ab\3\2\2\2bd\3\2\2\2c:\3\2\2\2")
        buf.write("cR\3\2\2\2d\b\3\2\2\2ef\7k\2\2fg\7p\2\2gh\7v\2\2h\n\3")
        buf.write("\2\2\2ij\7h\2\2jk\7n\2\2kl\7q\2\2lm\7c\2\2mn\7v\2\2n\f")
        buf.write("\3\2\2\2op\7t\2\2pq\7g\2\2qr\7v\2\2rs\7w\2\2st\7t\2\2")
        buf.write("tu\7p\2\2u\16\3\2\2\2vw\7}\2\2w\20\3\2\2\2xy\7\177\2\2")
        buf.write("y\22\3\2\2\2z{\7=\2\2{\24\3\2\2\2|}\7.\2\2}\26\3\2\2\2")
        buf.write("~\177\7?\2\2\177\30\3\2\2\2\u0080\u0081\7*\2\2\u0081\32")
        buf.write("\3\2\2\2\u0082\u0083\7+\2\2\u0083\34\3\2\2\2\u0084\u0085")
        buf.write("\7-\2\2\u0085\36\3\2\2\2\u0086\u0087\7/\2\2\u0087 \3\2")
        buf.write("\2\2\u0088\u0089\7,\2\2\u0089\"\3\2\2\2\u008a\u008b\7")
        buf.write("\61\2\2\u008b$\3\2\2\2\u008c\u0090\t\6\2\2\u008d\u008f")
        buf.write("\t\7\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091&\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0093\u0094\13\2\2\2\u0094(\3\2\2\2\u0095")
        buf.write("\u0096\13\2\2\2\u0096*\3\2\2\2\u0097\u0098\13\2\2\2\u0098")
        buf.write(",\3\2\2\2\21\2\60\67<BEHNPVY_ac\u0090\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    INTLIT = 2
    FLOATLIT = 3
    INT = 4
    FLOAT = 5
    RETURN = 6
    LB = 7
    RB = 8
    SM = 9
    CM = 10
    EQ = 11
    LP = 12
    RP = 13
    ADD = 14
    SUB = 15
    MUL = 16
    DIV = 17
    ID = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "INTLIT", "FLOATLIT", "INT", "FLOAT", "RETURN", "LB", 
            "RB", "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", 
            "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "INTLIT", "FLOATLIT", "INT", "FLOAT", "RETURN", 
                  "LB", "RB", "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", 
                  "MUL", "DIV", "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


