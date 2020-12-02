# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\20\7\20r\n\20\f\20\16\20u\13\20\3\21\3\21\5\21y\n\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0081\n\22\3\23\3")
        buf.write("\23\3\24\3\24\7\24\u0087\n\24\f\24\16\24\u008a\13\24\3")
        buf.write("\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30\7\30\u0095")
        buf.write("\n\30\f\30\16\30\u0098\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u00a0\n\31\3\32\3\32\7\32\u00a4\n\32\f\32\16")
        buf.write("\32\u00a7\13\32\3\32\6\32\u00aa\n\32\r\32\16\32\u00ab")
        buf.write("\5\32\u00ae\n\32\3\33\3\33\6\33\u00b2\n\33\r\33\16\33")
        buf.write("\u00b3\3\34\3\34\5\34\u00b8\n\34\3\34\6\34\u00bb\n\34")
        buf.write("\r\34\16\34\u00bc\3\35\3\35\3\35\7\35\u00c2\n\35\f\35")
        buf.write("\16\35\u00c5\13\35\3\35\3\35\3\36\3\36\3\36\3\37\6\37")
        buf.write("\u00cd\n\37\r\37\16\37\u00ce\3\37\3\37\3 \3 \3!\3!\3\"")
        buf.write("\3\"\3#\3#\2\2$\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\2+\2-\2/\26\61\27\63\2\65\2\67\29\30;\2=\31?\32A\33")
        buf.write("C\34E\35\3\2\t\3\2c|\4\2\62;c|\3\2C\\\3\2\62;\3\2\63;")
        buf.write("\3\2))\5\2\13\f\17\17\"\"\2\u00e5\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\29\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\3G\3\2\2\2\5K\3")
        buf.write("\2\2\2\7Q\3\2\2\2\tX\3\2\2\2\13Z\3\2\2\2\r\\\3\2\2\2\17")
        buf.write("^\3\2\2\2\21`\3\2\2\2\23b\3\2\2\2\25d\3\2\2\2\27f\3\2")
        buf.write("\2\2\31h\3\2\2\2\33j\3\2\2\2\35l\3\2\2\2\37n\3\2\2\2!")
        buf.write("x\3\2\2\2#z\3\2\2\2%\u0082\3\2\2\2\'\u0084\3\2\2\2)\u008b")
        buf.write("\3\2\2\2+\u008d\3\2\2\2-\u008f\3\2\2\2/\u0091\3\2\2\2")
        buf.write("\61\u0099\3\2\2\2\63\u00ad\3\2\2\2\65\u00af\3\2\2\2\67")
        buf.write("\u00b5\3\2\2\29\u00be\3\2\2\2;\u00c8\3\2\2\2=\u00cc\3")
        buf.write("\2\2\2?\u00d2\3\2\2\2A\u00d4\3\2\2\2C\u00d6\3\2\2\2E\u00d8")
        buf.write("\3\2\2\2GH\7k\2\2HI\7p\2\2IJ\7v\2\2J\4\3\2\2\2KL\7h\2")
        buf.write("\2LM\7n\2\2MN\7q\2\2NO\7c\2\2OP\7v\2\2P\6\3\2\2\2QR\7")
        buf.write("t\2\2RS\7g\2\2ST\7v\2\2TU\7w\2\2UV\7t\2\2VW\7p\2\2W\b")
        buf.write("\3\2\2\2XY\7}\2\2Y\n\3\2\2\2Z[\7\177\2\2[\f\3\2\2\2\\")
        buf.write("]\7=\2\2]\16\3\2\2\2^_\7.\2\2_\20\3\2\2\2`a\7?\2\2a\22")
        buf.write("\3\2\2\2bc\7*\2\2c\24\3\2\2\2de\7+\2\2e\26\3\2\2\2fg\7")
        buf.write("-\2\2g\30\3\2\2\2hi\7/\2\2i\32\3\2\2\2jk\7,\2\2k\34\3")
        buf.write("\2\2\2lm\7\61\2\2m\36\3\2\2\2ns\5!\21\2or\5!\21\2pr\5")
        buf.write("-\27\2qo\3\2\2\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2")
        buf.write("\2t \3\2\2\2us\3\2\2\2vy\5)\25\2wy\5+\26\2xv\3\2\2\2x")
        buf.write("w\3\2\2\2y\"\3\2\2\2z\u0080\5\63\32\2{\u0081\5\65\33\2")
        buf.write("|\u0081\5\67\34\2}~\5\65\33\2~\177\5\67\34\2\177\u0081")
        buf.write("\3\2\2\2\u0080{\3\2\2\2\u0080|\3\2\2\2\u0080}\3\2\2\2")
        buf.write("\u0081$\3\2\2\2\u0082\u0083\5\63\32\2\u0083&\3\2\2\2\u0084")
        buf.write("\u0088\t\2\2\2\u0085\u0087\t\3\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3")
        buf.write("\2\2\2\u0089(\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c")
        buf.write("\t\2\2\2\u008c*\3\2\2\2\u008d\u008e\t\4\2\2\u008e,\3\2")
        buf.write("\2\2\u008f\u0090\t\5\2\2\u0090.\3\2\2\2\u0091\u0096\5")
        buf.write(")\25\2\u0092\u0095\5)\25\2\u0093\u0095\5-\27\2\u0094\u0092")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\u0098\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\60\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u009f\5\63\32\2\u009a\u00a0\5\65")
        buf.write("\33\2\u009b\u00a0\5\67\34\2\u009c\u009d\5\65\33\2\u009d")
        buf.write("\u009e\5\67\34\2\u009e\u00a0\3\2\2\2\u009f\u009a\3\2\2")
        buf.write("\2\u009f\u009b\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\62\3")
        buf.write("\2\2\2\u00a1\u00a5\t\6\2\2\u00a2\u00a4\5-\27\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00ae\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a8\u00aa\7\62\2\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u00a1\3\2\2\2\u00ad\u00a9\3\2\2\2")
        buf.write("\u00ae\64\3\2\2\2\u00af\u00b1\7\60\2\2\u00b0\u00b2\5-")
        buf.write("\27\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\66\3\2\2\2\u00b5\u00b7")
        buf.write("\7g\2\2\u00b6\u00b8\7/\2\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00bb\5-\27\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd8\3\2\2\2\u00be\u00c3\7)\2\2")
        buf.write("\u00bf\u00c2\5;\36\2\u00c0\u00c2\n\7\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c7\7)\2\2\u00c7:\3\2\2\2\u00c8")
        buf.write("\u00c9\7)\2\2\u00c9\u00ca\7)\2\2\u00ca<\3\2\2\2\u00cb")
        buf.write("\u00cd\t\b\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\u00d1\b\37\2\2\u00d1>\3\2\2\2\u00d2\u00d3")
        buf.write("\13\2\2\2\u00d3@\3\2\2\2\u00d4\u00d5\13\2\2\2\u00d5B\3")
        buf.write("\2\2\2\u00d6\u00d7\13\2\2\2\u00d7D\3\2\2\2\u00d8\u00d9")
        buf.write("\13\2\2\2\u00d9F\3\2\2\2\24\2qsx\u0080\u0088\u0094\u0096")
        buf.write("\u009f\u00a5\u00ab\u00ad\u00b3\u00b7\u00bc\u00c1\u00c3")
        buf.write("\u00ce\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    RETURN = 3
    LB = 4
    RB = 5
    SM = 6
    CM = 7
    EQ = 8
    LP = 9
    RP = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    ID = 15
    LETTER = 16
    FLOATLIT = 17
    INTLIT = 18
    Identifier1 = 19
    Identifier2 = 20
    REAL = 21
    STR = 22
    WS = 23
    ERROR_CHAR = 24
    UNCLOSE_STRING = 25
    ILLEGAL_ESCAPE = 26
    UNTERMINATED_COMMENT = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", 
            "RP", "ADD", "SUB", "MUL", "DIV", "ID", "LETTER", "FLOATLIT", 
            "INTLIT", "Identifier1", "Identifier2", "REAL", "STR", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "FLOAT", "RETURN", "LB", "RB", "SM", "CM", "EQ", 
                  "LP", "RP", "ADD", "SUB", "MUL", "DIV", "ID", "LETTER", 
                  "FLOATLIT", "INTLIT", "Identifier1", "LOWER_LETTER", "UPPER_LETTER", 
                  "DIGIT", "Identifier2", "REAL", "INT_PART", "DEC_PART", 
                  "EPX_PART", "STR", "DOUBLE_QUOTE", "WS", "ERROR_CHAR", 
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


