# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u01ff\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\7\32\u00dc")
        buf.write("\n\32\f\32\16\32\u00df\13\32\3\32\3\32\6\32\u00e3\n\32")
        buf.write("\r\32\16\32\u00e4\3\32\3\32\3\33\3\33\7\33\u00eb\n\33")
        buf.write("\f\33\16\33\u00ee\13\33\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\5\61\u0174\n\61\3\62\3\62\3\62\3\62\5")
        buf.write("\62\u017a\n\62\3\63\3\63\7\63\u017e\n\63\f\63\16\63\u0181")
        buf.write("\13\63\3\64\3\64\3\64\3\64\7\64\u0187\n\64\f\64\16\64")
        buf.write("\u018a\13\64\3\65\3\65\3\65\3\65\7\65\u0190\n\65\f\65")
        buf.write("\16\65\u0193\13\65\3\66\3\66\5\66\u0197\n\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u019e\n\66\3\67\3\67\7\67\u01a2\n")
        buf.write("\67\f\67\16\67\u01a5\13\67\38\38\58\u01a9\n8\38\68\u01ac")
        buf.write("\n8\r8\168\u01ad\39\39\59\u01b2\n9\3:\3:\3:\3:\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\3E\5E\u01db\n")
        buf.write("E\3F\6F\u01de\nF\rF\16F\u01df\3F\3F\3G\3G\3G\3G\5G\u01e8")
        buf.write("\nG\3H\3H\3H\3H\3H\3H\7H\u01f0\nH\fH\16H\u01f3\13H\3I")
        buf.write("\3I\3I\3I\7I\u01f9\nI\fI\16I\u01fc\13I\3J\3J\4\u00dd\u01fa")
        buf.write("\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\64m\2o\2q\65")
        buf.write("s\66u\67w8y9{:};\177<\u0081=\u0083>\u0085?\u0087@\u0089")
        buf.write("\2\u008bA\u008dB\u008fC\u0091D\u0093E\3\2\21\3\2c|\6\2")
        buf.write("\62;C\\aac|\3\2\63;\3\2\62;\4\2QQqq\3\2\639\3\2\629\4")
        buf.write("\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GGgg\4\2--//\5\2\13\f\17")
        buf.write("\17\"\"\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\2\u0216")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2k\3\2\2\2\2q\3")
        buf.write("\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{")
        buf.write("\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u0097\3\2\2\2\7\u009a\3\2\2")
        buf.write("\2\t\u009c\3\2\2\2\13\u009f\3\2\2\2\r\u00a1\3\2\2\2\17")
        buf.write("\u00a4\3\2\2\2\21\u00a6\3\2\2\2\23\u00a9\3\2\2\2\25\u00ab")
        buf.write("\3\2\2\2\27\u00ae\3\2\2\2\31\u00b0\3\2\2\2\33\u00b2\3")
        buf.write("\2\2\2\35\u00b5\3\2\2\2\37\u00b8\3\2\2\2!\u00bb\3\2\2")
        buf.write("\2#\u00bd\3\2\2\2%\u00bf\3\2\2\2\'\u00c2\3\2\2\2)\u00c5")
        buf.write("\3\2\2\2+\u00c9\3\2\2\2-\u00cc\3\2\2\2/\u00cf\3\2\2\2")
        buf.write("\61\u00d3\3\2\2\2\63\u00e2\3\2\2\2\65\u00e8\3\2\2\2\67")
        buf.write("\u00ef\3\2\2\29\u00f4\3\2\2\2;\u00fa\3\2\2\2=\u0103\3")
        buf.write("\2\2\2?\u0106\3\2\2\2A\u010b\3\2\2\2C\u0112\3\2\2\2E\u011a")
        buf.write("\3\2\2\2G\u0120\3\2\2\2I\u0127\3\2\2\2K\u0130\3\2\2\2")
        buf.write("M\u0134\3\2\2\2O\u013d\3\2\2\2Q\u0140\3\2\2\2S\u014a\3")
        buf.write("\2\2\2U\u0151\3\2\2\2W\u0156\3\2\2\2Y\u015a\3\2\2\2[\u0160")
        buf.write("\3\2\2\2]\u0165\3\2\2\2_\u016b\3\2\2\2a\u0173\3\2\2\2")
        buf.write("c\u0179\3\2\2\2e\u017b\3\2\2\2g\u0182\3\2\2\2i\u018b\3")
        buf.write("\2\2\2k\u0196\3\2\2\2m\u019f\3\2\2\2o\u01a6\3\2\2\2q\u01b1")
        buf.write("\3\2\2\2s\u01b3\3\2\2\2u\u01b7\3\2\2\2w\u01b9\3\2\2\2")
        buf.write("y\u01bb\3\2\2\2{\u01bd\3\2\2\2}\u01bf\3\2\2\2\177\u01c1")
        buf.write("\3\2\2\2\u0081\u01c3\3\2\2\2\u0083\u01c5\3\2\2\2\u0085")
        buf.write("\u01c7\3\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01da\3\2\2\2")
        buf.write("\u008b\u01dd\3\2\2\2\u008d\u01e3\3\2\2\2\u008f\u01e9\3")
        buf.write("\2\2\2\u0091\u01f4\3\2\2\2\u0093\u01fd\3\2\2\2\u0095\u0096")
        buf.write("\7?\2\2\u0096\4\3\2\2\2\u0097\u0098\7?\2\2\u0098\u0099")
        buf.write("\7?\2\2\u0099\6\3\2\2\2\u009a\u009b\7-\2\2\u009b\b\3\2")
        buf.write("\2\2\u009c\u009d\7-\2\2\u009d\u009e\7\60\2\2\u009e\n\3")
        buf.write("\2\2\2\u009f\u00a0\7/\2\2\u00a0\f\3\2\2\2\u00a1\u00a2")
        buf.write("\7/\2\2\u00a2\u00a3\7\60\2\2\u00a3\16\3\2\2\2\u00a4\u00a5")
        buf.write("\7,\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7\u00a8")
        buf.write("\7\60\2\2\u00a8\22\3\2\2\2\u00a9\u00aa\7^\2\2\u00aa\24")
        buf.write("\3\2\2\2\u00ab\u00ac\7^\2\2\u00ac\u00ad\7\60\2\2\u00ad")
        buf.write("\26\3\2\2\2\u00ae\u00af\7\'\2\2\u00af\30\3\2\2\2\u00b0")
        buf.write("\u00b1\7#\2\2\u00b1\32\3\2\2\2\u00b2\u00b3\7(\2\2\u00b3")
        buf.write("\u00b4\7(\2\2\u00b4\34\3\2\2\2\u00b5\u00b6\7~\2\2\u00b6")
        buf.write("\u00b7\7~\2\2\u00b7\36\3\2\2\2\u00b8\u00b9\7#\2\2\u00b9")
        buf.write("\u00ba\7?\2\2\u00ba \3\2\2\2\u00bb\u00bc\7>\2\2\u00bc")
        buf.write("\"\3\2\2\2\u00bd\u00be\7@\2\2\u00be$\3\2\2\2\u00bf\u00c0")
        buf.write("\7>\2\2\u00c0\u00c1\7?\2\2\u00c1&\3\2\2\2\u00c2\u00c3")
        buf.write("\7@\2\2\u00c3\u00c4\7?\2\2\u00c4(\3\2\2\2\u00c5\u00c6")
        buf.write("\7?\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00c8\7?\2\2\u00c8")
        buf.write("*\3\2\2\2\u00c9\u00ca\7>\2\2\u00ca\u00cb\7\60\2\2\u00cb")
        buf.write(",\3\2\2\2\u00cc\u00cd\7@\2\2\u00cd\u00ce\7\60\2\2\u00ce")
        buf.write(".\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0\u00d1\7?\2\2\u00d1")
        buf.write("\u00d2\7\60\2\2\u00d2\60\3\2\2\2\u00d3\u00d4\7@\2\2\u00d4")
        buf.write("\u00d5\7?\2\2\u00d5\u00d6\7\60\2\2\u00d6\62\3\2\2\2\u00d7")
        buf.write("\u00d8\7,\2\2\u00d8\u00d9\7,\2\2\u00d9\u00dd\3\2\2\2\u00da")
        buf.write("\u00dc\13\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7,\2\2\u00e1")
        buf.write("\u00e3\7,\2\2\u00e2\u00d7\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3")
        buf.write("\2\2\2\u00e6\u00e7\b\32\2\2\u00e7\64\3\2\2\2\u00e8\u00ec")
        buf.write("\t\2\2\2\u00e9\u00eb\t\3\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ee\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\66\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\7D\2")
        buf.write("\2\u00f0\u00f1\7q\2\2\u00f1\u00f2\7f\2\2\u00f2\u00f3\7")
        buf.write("{\2\2\u00f38\3\2\2\2\u00f4\u00f5\7D\2\2\u00f5\u00f6\7")
        buf.write("t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9")
        buf.write("\7m\2\2\u00f9:\3\2\2\2\u00fa\u00fb\7E\2\2\u00fb\u00fc")
        buf.write("\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff")
        buf.write("\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102")
        buf.write("\7g\2\2\u0102<\3\2\2\2\u0103\u0104\7F\2\2\u0104\u0105")
        buf.write("\7q\2\2\u0105>\3\2\2\2\u0106\u0107\7G\2\2\u0107\u0108")
        buf.write("\7n\2\2\u0108\u0109\7u\2\2\u0109\u010a\7g\2\2\u010a@\3")
        buf.write("\2\2\2\u010b\u010c\7G\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7u\2\2\u010e\u010f\7g\2\2\u010f\u0110\7K\2\2\u0110\u0111")
        buf.write("\7h\2\2\u0111B\3\2\2\2\u0112\u0113\7G\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7f\2\2\u0115\u0116\7D\2\2\u0116\u0117")
        buf.write("\7q\2\2\u0117\u0118\7f\2\2\u0118\u0119\7{\2\2\u0119D\3")
        buf.write("\2\2\2\u011a\u011b\7G\2\2\u011b\u011c\7p\2\2\u011c\u011d")
        buf.write("\7f\2\2\u011d\u011e\7K\2\2\u011e\u011f\7h\2\2\u011fF\3")
        buf.write("\2\2\2\u0120\u0121\7G\2\2\u0121\u0122\7p\2\2\u0122\u0123")
        buf.write("\7f\2\2\u0123\u0124\7H\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126H\3\2\2\2\u0127\u0128\7G\2\2\u0128\u0129")
        buf.write("\7p\2\2\u0129\u012a\7f\2\2\u012a\u012b\7Y\2\2\u012b\u012c")
        buf.write("\7j\2\2\u012c\u012d\7k\2\2\u012d\u012e\7n\2\2\u012e\u012f")
        buf.write("\7g\2\2\u012fJ\3\2\2\2\u0130\u0131\7H\2\2\u0131\u0132")
        buf.write("\7q\2\2\u0132\u0133\7t\2\2\u0133L\3\2\2\2\u0134\u0135")
        buf.write("\7H\2\2\u0135\u0136\7w\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7e\2\2\u0138\u0139\7v\2\2\u0139\u013a\7k\2\2\u013a\u013b")
        buf.write("\7q\2\2\u013b\u013c\7p\2\2\u013cN\3\2\2\2\u013d\u013e")
        buf.write("\7K\2\2\u013e\u013f\7h\2\2\u013fP\3\2\2\2\u0140\u0141")
        buf.write("\7R\2\2\u0141\u0142\7c\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7c\2\2\u0144\u0145\7o\2\2\u0145\u0146\7g\2\2\u0146\u0147")
        buf.write("\7v\2\2\u0147\u0148\7g\2\2\u0148\u0149\7t\2\2\u0149R\3")
        buf.write("\2\2\2\u014a\u014b\7T\2\2\u014b\u014c\7g\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7w\2\2\u014e\u014f\7t\2\2\u014f\u0150")
        buf.write("\7p\2\2\u0150T\3\2\2\2\u0151\u0152\7V\2\2\u0152\u0153")
        buf.write("\7j\2\2\u0153\u0154\7g\2\2\u0154\u0155\7p\2\2\u0155V\3")
        buf.write("\2\2\2\u0156\u0157\7X\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7t\2\2\u0159X\3\2\2\2\u015a\u015b\7Y\2\2\u015b\u015c")
        buf.write("\7j\2\2\u015c\u015d\7k\2\2\u015d\u015e\7n\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015fZ\3\2\2\2\u0160\u0161\7V\2\2\u0161\u0162")
        buf.write("\7t\2\2\u0162\u0163\7w\2\2\u0163\u0164\7g\2\2\u0164\\")
        buf.write("\3\2\2\2\u0165\u0166\7H\2\2\u0166\u0167\7c\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\u0169\7u\2\2\u0169\u016a\7g\2\2\u016a^\3")
        buf.write("\2\2\2\u016b\u016c\7G\2\2\u016c\u016d\7p\2\2\u016d\u016e")
        buf.write("\7f\2\2\u016e\u016f\7F\2\2\u016f\u0170\7q\2\2\u0170`\3")
        buf.write("\2\2\2\u0171\u0174\5c\62\2\u0172\u0174\5k\66\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174b\3\2\2\2\u0175\u017a")
        buf.write("\7\62\2\2\u0176\u017a\5e\63\2\u0177\u017a\5g\64\2\u0178")
        buf.write("\u017a\5i\65\2\u0179\u0175\3\2\2\2\u0179\u0176\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017ad\3\2\2")
        buf.write("\2\u017b\u017f\t\4\2\2\u017c\u017e\t\5\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180f\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("\u0183\7\62\2\2\u0183\u0184\t\6\2\2\u0184\u0188\t\7\2")
        buf.write("\2\u0185\u0187\t\b\2\2\u0186\u0185\3\2\2\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("h\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c\7\62\2\2\u018c")
        buf.write("\u018d\t\t\2\2\u018d\u0191\t\n\2\2\u018e\u0190\t\13\2")
        buf.write("\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192j\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0194\u0197\7\62\2\2\u0195\u0197\5e\63\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u019d\3\2\2\2")
        buf.write("\u0198\u019e\5m\67\2\u0199\u019e\5o8\2\u019a\u019b\5m")
        buf.write("\67\2\u019b\u019c\5o8\2\u019c\u019e\3\2\2\2\u019d\u0198")
        buf.write("\3\2\2\2\u019d\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019e")
        buf.write("l\3\2\2\2\u019f\u01a3\5\u0083B\2\u01a0\u01a2\t\5\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4n\3\2\2\2\u01a5\u01a3\3\2\2")
        buf.write("\2\u01a6\u01a8\t\f\2\2\u01a7\u01a9\t\r\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01ac\t\5\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01aep\3\2\2")
        buf.write("\2\u01af\u01b2\5[.\2\u01b0\u01b2\5]/\2\u01b1\u01af\3\2")
        buf.write("\2\2\u01b1\u01b0\3\2\2\2\u01b2r\3\2\2\2\u01b3\u01b4\5")
        buf.write("\u008fH\2\u01b4\u01b5\7$\2\2\u01b5\u01b6\b:\3\2\u01b6")
        buf.write("t\3\2\2\2\u01b7\u01b8\7}\2\2\u01b8v\3\2\2\2\u01b9\u01ba")
        buf.write("\7\177\2\2\u01bax\3\2\2\2\u01bb\u01bc\7*\2\2\u01bcz\3")
        buf.write("\2\2\2\u01bd\u01be\7+\2\2\u01be|\3\2\2\2\u01bf\u01c0\7")
        buf.write("]\2\2\u01c0~\3\2\2\2\u01c1\u01c2\7_\2\2\u01c2\u0080\3")
        buf.write("\2\2\2\u01c3\u01c4\7=\2\2\u01c4\u0082\3\2\2\2\u01c5\u01c6")
        buf.write("\7\60\2\2\u01c6\u0084\3\2\2\2\u01c7\u01c8\7.\2\2\u01c8")
        buf.write("\u0086\3\2\2\2\u01c9\u01ca\7<\2\2\u01ca\u0088\3\2\2\2")
        buf.write("\u01cb\u01cc\7^\2\2\u01cc\u01db\7d\2\2\u01cd\u01ce\7^")
        buf.write("\2\2\u01ce\u01db\7h\2\2\u01cf\u01d0\7^\2\2\u01d0\u01db")
        buf.write("\7t\2\2\u01d1\u01d2\7^\2\2\u01d2\u01db\7p\2\2\u01d3\u01d4")
        buf.write("\7^\2\2\u01d4\u01db\7v\2\2\u01d5\u01d6\7^\2\2\u01d6\u01db")
        buf.write("\7)\2\2\u01d7\u01db\7^\2\2\u01d8\u01d9\7^\2\2\u01d9\u01db")
        buf.write("\7^\2\2\u01da\u01cb\3\2\2\2\u01da\u01cd\3\2\2\2\u01da")
        buf.write("\u01cf\3\2\2\2\u01da\u01d1\3\2\2\2\u01da\u01d3\3\2\2\2")
        buf.write("\u01da\u01d5\3\2\2\2\u01da\u01d7\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01db\u008a\3\2\2\2\u01dc\u01de\t\16\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\b")
        buf.write("F\2\2\u01e2\u008c\3\2\2\2\u01e3\u01e7\5\u008fH\2\u01e4")
        buf.write("\u01e5\7^\2\2\u01e5\u01e8\n\17\2\2\u01e6\u01e8\7)\2\2")
        buf.write("\u01e7\u01e4\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u008e\3")
        buf.write("\2\2\2\u01e9\u01f1\7$\2\2\u01ea\u01eb\7^\2\2\u01eb\u01f0")
        buf.write("\t\17\2\2\u01ec\u01ed\7)\2\2\u01ed\u01f0\7$\2\2\u01ee")
        buf.write("\u01f0\n\20\2\2\u01ef\u01ea\3\2\2\2\u01ef\u01ec\3\2\2")
        buf.write("\2\u01ef\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u0090\3\2\2\2\u01f3")
        buf.write("\u01f1\3\2\2\2\u01f4\u01f5\7,\2\2\u01f5\u01f6\7,\2\2\u01f6")
        buf.write("\u01fa\3\2\2\2\u01f7\u01f9\13\2\2\2\u01f8\u01f7\3\2\2")
        buf.write("\2\u01f9\u01fc\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fa\u01f8")
        buf.write("\3\2\2\2\u01fb\u0092\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd")
        buf.write("\u01fe\13\2\2\2\u01fe\u0094\3\2\2\2\27\2\u00dd\u00e4\u00ec")
        buf.write("\u0173\u0179\u017f\u0188\u0191\u0196\u019d\u01a3\u01a8")
        buf.write("\u01ad\u01b1\u01da\u01df\u01e7\u01ef\u01f1\u01fa\4\b\2")
        buf.write("\2\3:\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    COMMENT = 25
    IDENT = 26
    BODY = 27
    BREAK = 28
    CONTINUE = 29
    DO = 30
    ELSE = 31
    ELSEIF = 32
    ENDBODY = 33
    ENDIF = 34
    ENDFOR = 35
    ENDWHILE = 36
    FOR = 37
    FUNCTION = 38
    IF = 39
    PARAMETER = 40
    RETURN = 41
    THEN = 42
    VAR = 43
    WHILE = 44
    TRUE = 45
    FALSE = 46
    ENDDO = 47
    CONST = 48
    INT_LIT = 49
    FLOAT_LIT = 50
    BOOL_LIT = 51
    STRING_LIT = 52
    LCURLY = 53
    RCURLY = 54
    LR = 55
    RR = 56
    LB = 57
    RB = 58
    SEMI = 59
    DOT = 60
    COMMA = 61
    COLON = 62
    WS = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    UNTERMINATED_COMMENT = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'=='", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", 
            "'\\'", "'\\.'", "'%'", "'!'", "'&&'", "'||'", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'{'", "'}'", "'('", "')'", 
            "'['", "']'", "';'", "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "CONST", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
            "STRING_LIT", "LCURLY", "RCURLY", "LR", "RR", "LB", "RB", "SEMI", 
            "DOT", "COMMA", "COLON", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "COMMENT", "IDENT", 
                  "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "CONST", "INT_LIT", "DEC", "OCT", "HEX", 
                  "FLOAT_LIT", "DEC_PART", "EXP_PART", "BOOL_LIT", "STRING_LIT", 
                  "LCURLY", "RCURLY", "LR", "RR", "LB", "RB", "SEMI", "DOT", 
                  "COMMA", "COLON", "ESCAPE_STRING", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

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
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[56] = self.STRING_LIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


