# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36")
        buf.write("\u00e9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2P\n\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\7\21\u0081\n\21\f\21\16\21\u0084\13\21\3")
        buf.write("\22\3\22\5\22\u0088\n\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\5\23\u0090\n\23\3\24\3\24\3\25\3\25\7\25\u0096\n\25\f")
        buf.write("\25\16\25\u0099\13\25\3\26\3\26\3\27\3\27\3\30\3\30\3")
        buf.write("\31\3\31\3\31\7\31\u00a4\n\31\f\31\16\31\u00a7\13\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\5\32\u00af\n\32\3\33\3\33")
        buf.write("\7\33\u00b3\n\33\f\33\16\33\u00b6\13\33\3\33\6\33\u00b9")
        buf.write("\n\33\r\33\16\33\u00ba\5\33\u00bd\n\33\3\34\3\34\6\34")
        buf.write("\u00c1\n\34\r\34\16\34\u00c2\3\35\3\35\5\35\u00c7\n\35")
        buf.write("\3\35\6\35\u00ca\n\35\r\35\16\35\u00cb\3\36\3\36\3\36")
        buf.write("\7\36\u00d1\n\36\f\36\16\36\u00d4\13\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \6 \u00dc\n \r \16 \u00dd\3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\3$\3$\2\2%\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\2-\2/\2\61\27\63\30\65\2\67\29\2;\31=\2?\32")
        buf.write("A\33C\34E\35G\36\3\2\n\3\2$$\3\2c|\4\2\62;c|\3\2C\\\3")
        buf.write("\2\62;\3\2\63;\3\2))\5\2\13\f\17\17\"\"\2\u00f5\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2;\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\3I\3\2\2\2\5V\3\2\2\2\7Z\3\2\2\2\t`\3\2")
        buf.write("\2\2\13g\3\2\2\2\ri\3\2\2\2\17k\3\2\2\2\21m\3\2\2\2\23")
        buf.write("o\3\2\2\2\25q\3\2\2\2\27s\3\2\2\2\31u\3\2\2\2\33w\3\2")
        buf.write("\2\2\35y\3\2\2\2\37{\3\2\2\2!}\3\2\2\2#\u0087\3\2\2\2")
        buf.write("%\u0089\3\2\2\2\'\u0091\3\2\2\2)\u0093\3\2\2\2+\u009a")
        buf.write("\3\2\2\2-\u009c\3\2\2\2/\u009e\3\2\2\2\61\u00a0\3\2\2")
        buf.write("\2\63\u00a8\3\2\2\2\65\u00bc\3\2\2\2\67\u00be\3\2\2\2")
        buf.write("9\u00c4\3\2\2\2;\u00cd\3\2\2\2=\u00d7\3\2\2\2?\u00db\3")
        buf.write("\2\2\2A\u00e1\3\2\2\2C\u00e3\3\2\2\2E\u00e5\3\2\2\2G\u00e7")
        buf.write("\3\2\2\2IJ\7$\2\2JK\7$\2\2KO\3\2\2\2LP\n\2\2\2MN\7$\2")
        buf.write("\2NP\n\2\2\2OL\3\2\2\2OM\3\2\2\2PQ\3\2\2\2QR\7$\2\2RS")
        buf.write("\7$\2\2ST\3\2\2\2TU\b\2\2\2U\4\3\2\2\2VW\7k\2\2WX\7p\2")
        buf.write("\2XY\7v\2\2Y\6\3\2\2\2Z[\7h\2\2[\\\7n\2\2\\]\7q\2\2]^")
        buf.write("\7c\2\2^_\7v\2\2_\b\3\2\2\2`a\7t\2\2ab\7g\2\2bc\7v\2\2")
        buf.write("cd\7w\2\2de\7t\2\2ef\7p\2\2f\n\3\2\2\2gh\7}\2\2h\f\3\2")
        buf.write("\2\2ij\7\177\2\2j\16\3\2\2\2kl\7=\2\2l\20\3\2\2\2mn\7")
        buf.write(".\2\2n\22\3\2\2\2op\7?\2\2p\24\3\2\2\2qr\7*\2\2r\26\3")
        buf.write("\2\2\2st\7+\2\2t\30\3\2\2\2uv\7-\2\2v\32\3\2\2\2wx\7/")
        buf.write("\2\2x\34\3\2\2\2yz\7,\2\2z\36\3\2\2\2{|\7\61\2\2| \3\2")
        buf.write("\2\2}\u0082\5#\22\2~\u0081\5#\22\2\177\u0081\5/\30\2\u0080")
        buf.write("~\3\2\2\2\u0080\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\"\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0088\5+\26\2\u0086\u0088\5-\27\2")
        buf.write("\u0087\u0085\3\2\2\2\u0087\u0086\3\2\2\2\u0088$\3\2\2")
        buf.write("\2\u0089\u008f\5\65\33\2\u008a\u0090\5\67\34\2\u008b\u0090")
        buf.write("\59\35\2\u008c\u008d\5\67\34\2\u008d\u008e\59\35\2\u008e")
        buf.write("\u0090\3\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b\3\2\2\2")
        buf.write("\u008f\u008c\3\2\2\2\u0090&\3\2\2\2\u0091\u0092\5\65\33")
        buf.write("\2\u0092(\3\2\2\2\u0093\u0097\t\3\2\2\u0094\u0096\t\4")
        buf.write("\2\2\u0095\u0094\3\2\2\2\u0096\u0099\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098*\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009b\t\3\2\2\u009b,\3\2\2\2\u009c\u009d")
        buf.write("\t\5\2\2\u009d.\3\2\2\2\u009e\u009f\t\6\2\2\u009f\60\3")
        buf.write("\2\2\2\u00a0\u00a5\5+\26\2\u00a1\u00a4\5+\26\2\u00a2\u00a4")
        buf.write("\5/\30\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\62\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00ae\5\65")
        buf.write("\33\2\u00a9\u00af\5\67\34\2\u00aa\u00af\59\35\2\u00ab")
        buf.write("\u00ac\5\67\34\2\u00ac\u00ad\59\35\2\u00ad\u00af\3\2\2")
        buf.write("\2\u00ae\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab")
        buf.write("\3\2\2\2\u00af\64\3\2\2\2\u00b0\u00b4\t\7\2\2\u00b1\u00b3")
        buf.write("\5/\30\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00bd\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b7\u00b9\7\62\2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00b0\3\2\2\2")
        buf.write("\u00bc\u00b8\3\2\2\2\u00bd\66\3\2\2\2\u00be\u00c0\7\60")
        buf.write("\2\2\u00bf\u00c1\5/\30\2\u00c0\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("8\3\2\2\2\u00c4\u00c6\7g\2\2\u00c5\u00c7\7/\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00ca\5/\30\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc:")
        buf.write("\3\2\2\2\u00cd\u00d2\7)\2\2\u00ce\u00d1\5=\37\2\u00cf")
        buf.write("\u00d1\n\b\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3\u00d5\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6")
        buf.write("\7)\2\2\u00d6<\3\2\2\2\u00d7\u00d8\7)\2\2\u00d8\u00d9")
        buf.write("\7)\2\2\u00d9>\3\2\2\2\u00da\u00dc\t\t\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\b \2\2")
        buf.write("\u00e0@\3\2\2\2\u00e1\u00e2\13\2\2\2\u00e2B\3\2\2\2\u00e3")
        buf.write("\u00e4\13\2\2\2\u00e4D\3\2\2\2\u00e5\u00e6\13\2\2\2\u00e6")
        buf.write("F\3\2\2\2\u00e7\u00e8\13\2\2\2\u00e8H\3\2\2\2\25\2O\u0080")
        buf.write("\u0082\u0087\u008f\u0097\u00a3\u00a5\u00ae\u00b4\u00ba")
        buf.write("\u00bc\u00c2\u00c6\u00cb\u00d0\u00d2\u00dd\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INT = 2
    FLOAT = 3
    RETURN = 4
    LB = 5
    RB = 6
    SM = 7
    CM = 8
    EQ = 9
    LP = 10
    RP = 11
    ADD = 12
    SUB = 13
    MUL = 14
    DIV = 15
    ID = 16
    LETTER = 17
    FLOATLIT = 18
    INTLIT = 19
    Identifier1 = 20
    Identifier2 = 21
    REAL = 22
    STR = 23
    WS = 24
    ERROR_CHAR = 25
    UNCLOSE_STRING = 26
    ILLEGAL_ESCAPE = 27
    UNTERMINATED_COMMENT = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INT", "FLOAT", "RETURN", "LB", "RB", "SM", "CM", 
            "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", "ID", "LETTER", 
            "FLOATLIT", "INTLIT", "Identifier1", "Identifier2", "REAL", 
            "STR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "COMMENT", "INT", "FLOAT", "RETURN", "LB", "RB", "SM", 
                  "CM", "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", "ID", 
                  "LETTER", "FLOATLIT", "INTLIT", "Identifier1", "LOWER_LETTER", 
                  "UPPER_LETTER", "DIGIT", "Identifier2", "REAL", "INT_PART", 
                  "DEC_PART", "EPX_PART", "STR", "DOUBLE_QUOTE", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


