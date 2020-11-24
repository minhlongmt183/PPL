# Generated from main/lexical_analysis/parser/lexical_analysis.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\u0089\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\3\2\6\2+\n\2\r\2\16\2,\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\3\7\3")
        buf.write("\7\3\7\7\7A\n\7\f\7\16\7D\13\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\nP\n\n\3\13\5\13S\n\13\3\13\3\13\7")
        buf.write("\13W\n\13\f\13\16\13Z\13\13\3\13\5\13]\n\13\3\f\3\f\6")
        buf.write("\fa\n\f\r\f\16\fb\3\r\3\r\5\rg\n\r\3\r\6\rj\n\r\r\r\16")
        buf.write("\rk\3\16\3\16\3\16\7\16q\n\16\f\16\16\16t\13\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\20\6\20|\n\20\r\20\16\20}\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\2\2\25\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\2\21\2\23\t\25\2\27\2\31\2\33")
        buf.write("\n\35\2\37\13!\f#\r%\16\'\17\3\2\b\3\2c|\4\2\62;c|\3\2")
        buf.write("\62;\3\2\63;\3\2))\5\2\13\f\17\17\"\"\2\u0091\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\23\3\2\2\2\2\33\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3*\3\2\2\2")
        buf.write("\5.\3\2\2\2\7\60\3\2\2\2\t\62\3\2\2\2\13\66\3\2\2\2\r")
        buf.write("=\3\2\2\2\17E\3\2\2\2\21G\3\2\2\2\23I\3\2\2\2\25\\\3\2")
        buf.write("\2\2\27^\3\2\2\2\31d\3\2\2\2\33m\3\2\2\2\35w\3\2\2\2\37")
        buf.write("{\3\2\2\2!\u0081\3\2\2\2#\u0083\3\2\2\2%\u0085\3\2\2\2")
        buf.write("\'\u0087\3\2\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2")
        buf.write("\2,-\3\2\2\2-\4\3\2\2\2./\7=\2\2/\6\3\2\2\2\60\61\7<\2")
        buf.write("\2\61\b\3\2\2\2\62\63\7X\2\2\63\64\7c\2\2\64\65\7t\2\2")
        buf.write("\65\n\3\2\2\2\66:\t\2\2\2\679\t\3\2\28\67\3\2\2\29<\3")
        buf.write("\2\2\2:8\3\2\2\2:;\3\2\2\2;\f\3\2\2\2<:\3\2\2\2=B\5\17")
        buf.write("\b\2>A\5\17\b\2?A\5\21\t\2@>\3\2\2\2@?\3\2\2\2AD\3\2\2")
        buf.write("\2B@\3\2\2\2BC\3\2\2\2C\16\3\2\2\2DB\3\2\2\2EF\t\2\2\2")
        buf.write("F\20\3\2\2\2GH\t\4\2\2H\22\3\2\2\2IO\5\25\13\2JP\5\27")
        buf.write("\f\2KP\5\31\r\2LM\5\27\f\2MN\5\31\r\2NP\3\2\2\2OJ\3\2")
        buf.write("\2\2OK\3\2\2\2OL\3\2\2\2P\24\3\2\2\2QS\7/\2\2RQ\3\2\2")
        buf.write("\2RS\3\2\2\2ST\3\2\2\2TX\t\5\2\2UW\5\21\t\2VU\3\2\2\2")
        buf.write("WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y]\3\2\2\2ZX\3\2\2\2[]\7")
        buf.write("\62\2\2\\R\3\2\2\2\\[\3\2\2\2]\26\3\2\2\2^`\7\60\2\2_")
        buf.write("a\5\21\t\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\30")
        buf.write("\3\2\2\2df\7g\2\2eg\7/\2\2fe\3\2\2\2fg\3\2\2\2gi\3\2\2")
        buf.write("\2hj\5\21\t\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2")
        buf.write("l\32\3\2\2\2mr\7)\2\2nq\5\35\17\2oq\n\6\2\2pn\3\2\2\2")
        buf.write("po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3")
        buf.write("\2\2\2uv\7)\2\2v\34\3\2\2\2wx\7)\2\2xy\7)\2\2y\36\3\2")
        buf.write("\2\2z|\t\7\2\2{z\3\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2")
        buf.write("~\177\3\2\2\2\177\u0080\b\20\2\2\u0080 \3\2\2\2\u0081")
        buf.write("\u0082\13\2\2\2\u0082\"\3\2\2\2\u0083\u0084\13\2\2\2\u0084")
        buf.write("$\3\2\2\2\u0085\u0086\13\2\2\2\u0086&\3\2\2\2\u0087\u0088")
        buf.write("\13\2\2\2\u0088(\3\2\2\2\21\2,:@BORX\\bfkpr}\3\b\2\2")
        return buf.getvalue()


class lexical_analysisLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    INT = 5
    Identifier = 6
    REAL = 7
    STR = 8
    WS = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12
    UNTERMINATED_COMMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "INT", "Identifier", "REAL", "STR", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "SEMI", "COLON", "VAR", "INT", "Identifier", "LOWER_LETTER", 
                  "DIGIT", "REAL", "INT_PART", "DEC_PART", "EPX_PART", "STR", 
                  "DOUBLE_QUOTE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "lexical_analysis.g4"

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


