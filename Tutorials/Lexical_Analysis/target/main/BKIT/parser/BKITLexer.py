# Generated from main/BKIT/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("t\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\7\2$\n\2\f\2\16\2\'")
        buf.write("\13\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5\60\n\5\f\5\16\5")
        buf.write("\63\13\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6;\n\6\3\7\5\7>\n\7")
        buf.write("\3\7\3\7\7\7B\n\7\f\7\16\7E\13\7\3\7\5\7H\n\7\3\b\3\b")
        buf.write("\6\bL\n\b\r\b\16\bM\3\t\3\t\5\tR\n\t\3\t\6\tU\n\t\r\t")
        buf.write("\16\tV\3\n\3\n\3\n\7\n\\\n\n\f\n\16\n_\13\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\6\fg\n\f\r\f\16\fh\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\2\2\21\3\3\5\2\7\2\t\4\13")
        buf.write("\5\r\2\17\2\21\2\23\6\25\2\27\7\31\b\33\t\35\n\37\13\3")
        buf.write("\2\b\3\2c|\4\2\62;c|\3\2\62;\3\2\63;\3\2))\5\2\13\f\17")
        buf.write("\17\"\"\2{\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\3!\3\2\2\2\5(\3\2\2\2\7*\3\2\2\2\t,")
        buf.write("\3\2\2\2\13\64\3\2\2\2\rG\3\2\2\2\17I\3\2\2\2\21O\3\2")
        buf.write("\2\2\23X\3\2\2\2\25b\3\2\2\2\27f\3\2\2\2\31l\3\2\2\2\33")
        buf.write("n\3\2\2\2\35p\3\2\2\2\37r\3\2\2\2!%\t\2\2\2\"$\t\3\2\2")
        buf.write("#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\4\3\2\2\2")
        buf.write("\'%\3\2\2\2()\t\2\2\2)\6\3\2\2\2*+\t\4\2\2+\b\3\2\2\2")
        buf.write(",\61\5\5\3\2-\60\5\5\3\2.\60\5\7\4\2/-\3\2\2\2/.\3\2\2")
        buf.write("\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\n\3\2\2")
        buf.write("\2\63\61\3\2\2\2\64:\5\r\7\2\65;\5\17\b\2\66;\5\21\t\2")
        buf.write("\678\5\17\b\289\5\21\t\29;\3\2\2\2:\65\3\2\2\2:\66\3\2")
        buf.write("\2\2:\67\3\2\2\2;\f\3\2\2\2<>\7/\2\2=<\3\2\2\2=>\3\2\2")
        buf.write("\2>?\3\2\2\2?C\t\5\2\2@B\5\7\4\2A@\3\2\2\2BE\3\2\2\2C")
        buf.write("A\3\2\2\2CD\3\2\2\2DH\3\2\2\2EC\3\2\2\2FH\7\62\2\2G=\3")
        buf.write("\2\2\2GF\3\2\2\2H\16\3\2\2\2IK\7\60\2\2JL\5\7\4\2KJ\3")
        buf.write("\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\20\3\2\2\2OQ\7g")
        buf.write("\2\2PR\7/\2\2QP\3\2\2\2QR\3\2\2\2RT\3\2\2\2SU\5\7\4\2")
        buf.write("TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2W\22\3\2\2\2X")
        buf.write("]\7)\2\2Y\\\5\25\13\2Z\\\n\6\2\2[Y\3\2\2\2[Z\3\2\2\2\\")
        buf.write("_\3\2\2\2][\3\2\2\2]^\3\2\2\2^`\3\2\2\2_]\3\2\2\2`a\7")
        buf.write(")\2\2a\24\3\2\2\2bc\7)\2\2cd\7)\2\2d\26\3\2\2\2eg\t\7")
        buf.write("\2\2fe\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2")
        buf.write("jk\b\f\2\2k\30\3\2\2\2lm\13\2\2\2m\32\3\2\2\2no\13\2\2")
        buf.write("\2o\34\3\2\2\2pq\13\2\2\2q\36\3\2\2\2rs\13\2\2\2s \3\2")
        buf.write("\2\2\20\2%/\61:=CGMQV[]h\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Identifier1 = 1
    Identifier2 = 2
    REAL = 3
    STR = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8
    UNTERMINATED_COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "Identifier1", "Identifier2", "REAL", "STR", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Identifier1", "LOWER_LETTER", "DIGIT", "Identifier2", 
                  "REAL", "INT_PART", "DEC_PART", "EPX_PART", "STR", "DOUBLE_QUOTE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

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


