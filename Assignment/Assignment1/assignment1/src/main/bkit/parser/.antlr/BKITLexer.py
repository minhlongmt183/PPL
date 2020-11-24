# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Assignments/Assignment1/assignment1/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01e6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u00d6\n\32\f\32\16\32\u00d9")
        buf.write("\13\32\3\32\3\32\6\32\u00dd\n\32\r\32\16\32\u00de\3\32")
        buf.write("\3\32\3\33\3\33\7\33\u00e5\n\33\f\33\16\33\u00e8\13\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3/\3/\5/\u0167\n/\3\60\6\60\u016a\n\60\r\60\16\60\u016b")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u0172\n\61\3\62\3\62\7\62\u0176")
        buf.write("\n\62\f\62\16\62\u0179\13\62\3\63\3\63\3\63\3\63\7\63")
        buf.write("\u017f\n\63\f\63\16\63\u0182\13\63\3\64\3\64\3\64\3\64")
        buf.write("\7\64\u0188\n\64\f\64\16\64\u018b\13\64\3\65\3\65\7\65")
        buf.write("\u018f\n\65\f\65\16\65\u0192\13\65\3\66\3\66\5\66\u0196")
        buf.write("\n\66\3\66\6\66\u0199\n\66\r\66\16\66\u019a\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01a6\n\67\3")
        buf.write("8\38\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\6C\u01c1\nC\rC\16C\u01c2\3C\3C\3D")
        buf.write("\3D\3D\3D\3D\3D\7D\u01cd\nD\fD\16D\u01d0\13D\3D\5D\u01d3")
        buf.write("\nD\3E\3E\3E\3E\7E\u01d9\nE\fE\16E\u01dc\13E\3F\3F\3F")
        buf.write("\3F\3F\5F\u01e3\nF\3G\3G\4\u00d7\u01da\2H\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\2a\61c\2e\2g\2i\2k\2m\62o\63q\64s\65u\66w\67y8")
        buf.write("{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\u008d")
        buf.write("B\3\2\23\3\2c|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2QQqq")
        buf.write("\3\2\639\3\2\629\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2GGgg\4")
        buf.write("\2--//\5\2\13\f\17\17\"\"\t\2))^^ddhhppttvv\7\2\n\f\16")
        buf.write("\17$$))^^\3\3\f\f\3\2$$\2\u01f6\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2a\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w")
        buf.write("\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0091\3\2\2\2\7\u0094\3\2\2\2\t\u0097")
        buf.write("\3\2\2\2\13\u0099\3\2\2\2\r\u009b\3\2\2\2\17\u009e\3\2")
        buf.write("\2\2\21\u00a1\3\2\2\2\23\u00a5\3\2\2\2\25\u00a8\3\2\2")
        buf.write("\2\27\u00ab\3\2\2\2\31\u00af\3\2\2\2\33\u00b3\3\2\2\2")
        buf.write("\35\u00b6\3\2\2\2\37\u00b9\3\2\2\2!\u00bb\3\2\2\2#\u00be")
        buf.write("\3\2\2\2%\u00c0\3\2\2\2\'\u00c3\3\2\2\2)\u00c5\3\2\2\2")
        buf.write("+\u00c8\3\2\2\2-\u00ca\3\2\2\2/\u00cd\3\2\2\2\61\u00cf")
        buf.write("\3\2\2\2\63\u00dc\3\2\2\2\65\u00e2\3\2\2\2\67\u00e9\3")
        buf.write("\2\2\29\u00ee\3\2\2\2;\u00f4\3\2\2\2=\u00fd\3\2\2\2?\u0100")
        buf.write("\3\2\2\2A\u0105\3\2\2\2C\u010c\3\2\2\2E\u0114\3\2\2\2")
        buf.write("G\u011a\3\2\2\2I\u0121\3\2\2\2K\u012a\3\2\2\2M\u012e\3")
        buf.write("\2\2\2O\u0137\3\2\2\2Q\u013a\3\2\2\2S\u0144\3\2\2\2U\u014b")
        buf.write("\3\2\2\2W\u0150\3\2\2\2Y\u0154\3\2\2\2[\u015a\3\2\2\2")
        buf.write("]\u0160\3\2\2\2_\u0169\3\2\2\2a\u0171\3\2\2\2c\u0173\3")
        buf.write("\2\2\2e\u017a\3\2\2\2g\u0183\3\2\2\2i\u018c\3\2\2\2k\u0193")
        buf.write("\3\2\2\2m\u01a5\3\2\2\2o\u01a7\3\2\2\2q\u01ab\3\2\2\2")
        buf.write("s\u01ad\3\2\2\2u\u01af\3\2\2\2w\u01b1\3\2\2\2y\u01b3\3")
        buf.write("\2\2\2{\u01b5\3\2\2\2}\u01b7\3\2\2\2\177\u01b9\3\2\2\2")
        buf.write("\u0081\u01bb\3\2\2\2\u0083\u01bd\3\2\2\2\u0085\u01c0\3")
        buf.write("\2\2\2\u0087\u01c6\3\2\2\2\u0089\u01d4\3\2\2\2\u008b\u01dd")
        buf.write("\3\2\2\2\u008d\u01e4\3\2\2\2\u008f\u0090\7?\2\2\u0090")
        buf.write("\4\3\2\2\2\u0091\u0092\7?\2\2\u0092\u0093\7?\2\2\u0093")
        buf.write("\6\3\2\2\2\u0094\u0095\7#\2\2\u0095\u0096\7?\2\2\u0096")
        buf.write("\b\3\2\2\2\u0097\u0098\7>\2\2\u0098\n\3\2\2\2\u0099\u009a")
        buf.write("\7@\2\2\u009a\f\3\2\2\2\u009b\u009c\7>\2\2\u009c\u009d")
        buf.write("\7?\2\2\u009d\16\3\2\2\2\u009e\u009f\7@\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\20\3\2\2\2\u00a1\u00a2\7?\2\2\u00a2\u00a3")
        buf.write("\7\61\2\2\u00a3\u00a4\7?\2\2\u00a4\22\3\2\2\2\u00a5\u00a6")
        buf.write("\7>\2\2\u00a6\u00a7\7\60\2\2\u00a7\24\3\2\2\2\u00a8\u00a9")
        buf.write("\7@\2\2\u00a9\u00aa\7\60\2\2\u00aa\26\3\2\2\2\u00ab\u00ac")
        buf.write("\7>\2\2\u00ac\u00ad\7?\2\2\u00ad\u00ae\7\60\2\2\u00ae")
        buf.write("\30\3\2\2\2\u00af\u00b0\7@\2\2\u00b0\u00b1\7?\2\2\u00b1")
        buf.write("\u00b2\7\60\2\2\u00b2\32\3\2\2\2\u00b3\u00b4\7(\2\2\u00b4")
        buf.write("\u00b5\7(\2\2\u00b5\34\3\2\2\2\u00b6\u00b7\7~\2\2\u00b7")
        buf.write("\u00b8\7~\2\2\u00b8\36\3\2\2\2\u00b9\u00ba\7-\2\2\u00ba")
        buf.write(" \3\2\2\2\u00bb\u00bc\7-\2\2\u00bc\u00bd\7\60\2\2\u00bd")
        buf.write("\"\3\2\2\2\u00be\u00bf\7/\2\2\u00bf$\3\2\2\2\u00c0\u00c1")
        buf.write("\7/\2\2\u00c1\u00c2\7\60\2\2\u00c2&\3\2\2\2\u00c3\u00c4")
        buf.write("\7,\2\2\u00c4(\3\2\2\2\u00c5\u00c6\7,\2\2\u00c6\u00c7")
        buf.write("\7\60\2\2\u00c7*\3\2\2\2\u00c8\u00c9\7^\2\2\u00c9,\3\2")
        buf.write("\2\2\u00ca\u00cb\7^\2\2\u00cb\u00cc\7\60\2\2\u00cc.\3")
        buf.write("\2\2\2\u00cd\u00ce\7\'\2\2\u00ce\60\3\2\2\2\u00cf\u00d0")
        buf.write("\7#\2\2\u00d0\62\3\2\2\2\u00d1\u00d2\7,\2\2\u00d2\u00d3")
        buf.write("\7,\2\2\u00d3\u00d7\3\2\2\2\u00d4\u00d6\13\2\2\2\u00d5")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d7\3")
        buf.write("\2\2\2\u00da\u00db\7,\2\2\u00db\u00dd\7,\2\2\u00dc\u00d1")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\b\32\2")
        buf.write("\2\u00e1\64\3\2\2\2\u00e2\u00e6\t\2\2\2\u00e3\u00e5\t")
        buf.write("\3\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\66\3\2\2\2\u00e8\u00e6")
        buf.write("\3\2\2\2\u00e9\u00ea\7D\2\2\u00ea\u00eb\7q\2\2\u00eb\u00ec")
        buf.write("\7f\2\2\u00ec\u00ed\7{\2\2\u00ed8\3\2\2\2\u00ee\u00ef")
        buf.write("\7D\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7c\2\2\u00f2\u00f3\7m\2\2\u00f3:\3\2\2\2\u00f4\u00f5")
        buf.write("\7E\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7g\2\2\u00fc<\3\2\2\2\u00fd\u00fe")
        buf.write("\7F\2\2\u00fe\u00ff\7q\2\2\u00ff>\3\2\2\2\u0100\u0101")
        buf.write("\7G\2\2\u0101\u0102\7n\2\2\u0102\u0103\7u\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104@\3\2\2\2\u0105\u0106\7G\2\2\u0106\u0107")
        buf.write("\7n\2\2\u0107\u0108\7u\2\2\u0108\u0109\7g\2\2\u0109\u010a")
        buf.write("\7K\2\2\u010a\u010b\7h\2\2\u010bB\3\2\2\2\u010c\u010d")
        buf.write("\7G\2\2\u010d\u010e\7p\2\2\u010e\u010f\7f\2\2\u010f\u0110")
        buf.write("\7D\2\2\u0110\u0111\7q\2\2\u0111\u0112\7f\2\2\u0112\u0113")
        buf.write("\7{\2\2\u0113D\3\2\2\2\u0114\u0115\7G\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7f\2\2\u0117\u0118\7K\2\2\u0118\u0119")
        buf.write("\7h\2\2\u0119F\3\2\2\2\u011a\u011b\7G\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7f\2\2\u011d\u011e\7H\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7t\2\2\u0120H\3\2\2\2\u0121\u0122")
        buf.write("\7G\2\2\u0122\u0123\7p\2\2\u0123\u0124\7f\2\2\u0124\u0125")
        buf.write("\7Y\2\2\u0125\u0126\7j\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7n\2\2\u0128\u0129\7g\2\2\u0129J\3\2\2\2\u012a\u012b")
        buf.write("\7H\2\2\u012b\u012c\7q\2\2\u012c\u012d\7t\2\2\u012dL\3")
        buf.write("\2\2\2\u012e\u012f\7H\2\2\u012f\u0130\7w\2\2\u0130\u0131")
        buf.write("\7p\2\2\u0131\u0132\7e\2\2\u0132\u0133\7v\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7q\2\2\u0135\u0136\7p\2\2\u0136N\3")
        buf.write("\2\2\2\u0137\u0138\7K\2\2\u0138\u0139\7h\2\2\u0139P\3")
        buf.write("\2\2\2\u013a\u013b\7R\2\2\u013b\u013c\7c\2\2\u013c\u013d")
        buf.write("\7t\2\2\u013d\u013e\7c\2\2\u013e\u013f\7o\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7v\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7t\2\2\u0143R\3\2\2\2\u0144\u0145\7T\2\2\u0145\u0146")
        buf.write("\7g\2\2\u0146\u0147\7v\2\2\u0147\u0148\7w\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7p\2\2\u014aT\3\2\2\2\u014b\u014c")
        buf.write("\7V\2\2\u014c\u014d\7j\2\2\u014d\u014e\7g\2\2\u014e\u014f")
        buf.write("\7p\2\2\u014fV\3\2\2\2\u0150\u0151\7X\2\2\u0151\u0152")
        buf.write("\7c\2\2\u0152\u0153\7t\2\2\u0153X\3\2\2\2\u0154\u0155")
        buf.write("\7Y\2\2\u0155\u0156\7j\2\2\u0156\u0157\7k\2\2\u0157\u0158")
        buf.write("\7n\2\2\u0158\u0159\7g\2\2\u0159Z\3\2\2\2\u015a\u015b")
        buf.write("\7G\2\2\u015b\u015c\7p\2\2\u015c\u015d\7f\2\2\u015d\u015e")
        buf.write("\7F\2\2\u015e\u015f\7q\2\2\u015f\\\3\2\2\2\u0160\u0166")
        buf.write("\5_\60\2\u0161\u0167\5i\65\2\u0162\u0167\5k\66\2\u0163")
        buf.write("\u0164\5i\65\2\u0164\u0165\5k\66\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u0161\3\2\2\2\u0166\u0162\3\2\2\2\u0166\u0163\3")
        buf.write("\2\2\2\u0167^\3\2\2\2\u0168\u016a\t\4\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c`\3\2\2\2\u016d\u0172\7\62\2\2\u016e")
        buf.write("\u0172\5c\62\2\u016f\u0172\5e\63\2\u0170\u0172\5g\64\2")
        buf.write("\u0171\u016d\3\2\2\2\u0171\u016e\3\2\2\2\u0171\u016f\3")
        buf.write("\2\2\2\u0171\u0170\3\2\2\2\u0172b\3\2\2\2\u0173\u0177")
        buf.write("\t\5\2\2\u0174\u0176\t\4\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178d\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\7\62\2")
        buf.write("\2\u017b\u017c\t\6\2\2\u017c\u0180\t\7\2\2\u017d\u017f")
        buf.write("\t\b\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181f\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0183\u0184\7\62\2\2\u0184\u0185\t\t\2")
        buf.write("\2\u0185\u0189\t\n\2\2\u0186\u0188\t\13\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018ah\3\2\2\2\u018b\u0189\3\2\2\2\u018c")
        buf.write("\u0190\5\177@\2\u018d\u018f\t\4\2\2\u018e\u018d\3\2\2")
        buf.write("\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191")
        buf.write("\3\2\2\2\u0191j\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0195")
        buf.write("\t\f\2\2\u0194\u0196\t\r\2\2\u0195\u0194\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0199\t\4\2\2")
        buf.write("\u0198\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3")
        buf.write("\2\2\2\u019a\u019b\3\2\2\2\u019bl\3\2\2\2\u019c\u019d")
        buf.write("\7V\2\2\u019d\u019e\7t\2\2\u019e\u019f\7w\2\2\u019f\u01a6")
        buf.write("\7g\2\2\u01a0\u01a1\7H\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3")
        buf.write("\7n\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a6\7g\2\2\u01a5\u019c")
        buf.write("\3\2\2\2\u01a5\u01a0\3\2\2\2\u01a6n\3\2\2\2\u01a7\u01a8")
        buf.write("\5\u0087D\2\u01a8\u01a9\7$\2\2\u01a9\u01aa\b8\3\2\u01aa")
        buf.write("p\3\2\2\2\u01ab\u01ac\7}\2\2\u01acr\3\2\2\2\u01ad\u01ae")
        buf.write("\7\177\2\2\u01aet\3\2\2\2\u01af\u01b0\7*\2\2\u01b0v\3")
        buf.write("\2\2\2\u01b1\u01b2\7+\2\2\u01b2x\3\2\2\2\u01b3\u01b4\7")
        buf.write("]\2\2\u01b4z\3\2\2\2\u01b5\u01b6\7_\2\2\u01b6|\3\2\2\2")
        buf.write("\u01b7\u01b8\7=\2\2\u01b8~\3\2\2\2\u01b9\u01ba\7\60\2")
        buf.write("\2\u01ba\u0080\3\2\2\2\u01bb\u01bc\7.\2\2\u01bc\u0082")
        buf.write("\3\2\2\2\u01bd\u01be\7<\2\2\u01be\u0084\3\2\2\2\u01bf")
        buf.write("\u01c1\t\16\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2")
        buf.write("\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c4")
        buf.write("\3\2\2\2\u01c4\u01c5\bC\2\2\u01c5\u0086\3\2\2\2\u01c6")
        buf.write("\u01ce\7$\2\2\u01c7\u01c8\7^\2\2\u01c8\u01cd\t\17\2\2")
        buf.write("\u01c9\u01ca\7)\2\2\u01ca\u01cd\7$\2\2\u01cb\u01cd\n\20")
        buf.write("\2\2\u01cc\u01c7\3\2\2\2\u01cc\u01c9\3\2\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cf\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d3\t\21\2\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3")
        buf.write("\3\2\2\2\u01d3\u0088\3\2\2\2\u01d4\u01d5\7,\2\2\u01d5")
        buf.write("\u01d6\7,\2\2\u01d6\u01da\3\2\2\2\u01d7\u01d9\13\2\2\2")
        buf.write("\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01db\3")
        buf.write("\2\2\2\u01da\u01d8\3\2\2\2\u01db\u008a\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dd\u01e2\5\u0087D\2\u01de\u01df\7^\2\2\u01df")
        buf.write("\u01e3\n\17\2\2\u01e0\u01e1\7)\2\2\u01e1\u01e3\n\22\2")
        buf.write("\2\u01e2\u01de\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u008c")
        buf.write("\3\2\2\2\u01e4\u01e5\13\2\2\2\u01e5\u008e\3\2\2\2\26\2")
        buf.write("\u00d7\u00de\u00e6\u0166\u016b\u0171\u0177\u0180\u0189")
        buf.write("\u0190\u0195\u019a\u01a5\u01c2\u01cc\u01ce\u01d2\u01da")
        buf.write("\u01e2\4\b\2\2\38\2")
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
    ENDDO = 45
    FLOAT_LIT = 46
    INT_LIT = 47
    BOOL_LIT = 48
    STRING_LIT = 49
    LCURLY = 50
    RCURLY = 51
    LR = 52
    RR = 53
    LB = 54
    RB = 55
    SEMI = 56
    DOT = 57
    COMMA = 58
    COLON = 59
    WS = 60
    UNCLOSE_STRING = 61
    UNTERMINATED_COMMENT = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'&&'", "'||'", "'+'", "'+.'", 
            "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", 
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", 
            "'.'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "IDENT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
            "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
            "FLOAT_LIT", "INT_LIT", "BOOL_LIT", "STRING_LIT", "LCURLY", 
            "RCURLY", "LR", "RR", "LB", "RB", "SEMI", "DOT", "COMMA", "COLON", 
            "WS", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "COMMENT", "IDENT", 
                  "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "ENDDO", 
                  "FLOAT_LIT", "INT_PART", "INT_LIT", "DEC", "OCT", "HEX", 
                  "DEC_PART", "EXP_PART", "BOOL_LIT", "STRING_LIT", "LCURLY", 
                  "RCURLY", "LR", "RR", "LB", "RB", "SEMI", "DOT", "COMMA", 
                  "COLON", "WS", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            raise IllegalEscape(self.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRING_LIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


