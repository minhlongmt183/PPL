# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01b5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\2\3\3\7\3h\n\3")
        buf.write("\f\3\16\3k\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5u\n")
        buf.write("\5\f\5\16\5x\13\5\3\6\3\6\3\6\3\6\7\6~\n\6\f\6\16\6\u0081")
        buf.write("\13\6\3\6\3\6\5\6\u0085\n\6\3\7\3\7\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u008d\n\t\3\n\3\n\3\13\3\13\3\f\7\f\u0094\n\f\f\f\16")
        buf.write("\f\u0097\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009f\n\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\7\17\u00ac")
        buf.write("\n\17\f\17\16\17\u00af\13\17\3\20\3\20\3\20\3\20\7\20")
        buf.write("\u00b5\n\20\f\20\16\20\u00b8\13\20\3\21\7\21\u00bb\n\21")
        buf.write("\f\21\16\21\u00be\13\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\7\21\u00c9\n\21\f\21\16\21\u00cc\13\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\7\24\u00dd\n\24\f\24\16\24\u00e0")
        buf.write("\13\24\3\24\5\24\u00e3\n\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\5\34\u0116\n\34\3\34\3\34\3\34\3\35\3\35\3\35\7\35\u011e")
        buf.write("\n\35\f\35\16\35\u0121\13\35\3\36\3\36\5\36\u0125\n\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\7\37\u012c\n\37\f\37\16\37\u012f")
        buf.write("\13\37\3 \3 \3 \5 \u0134\n \3!\3!\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u013c\n\"\3\"\3\"\6\"\u0140\n\"\r\"\16\"\u0141\3#\3#")
        buf.write("\3#\3#\3#\5#\u0149\n#\3$\3$\3$\3$\3$\3$\7$\u0151\n$\f")
        buf.write("$\16$\u0154\13$\3%\3%\3%\3%\3%\3%\7%\u015c\n%\f%\16%\u015f")
        buf.write("\13%\3&\3&\3&\3&\3&\3&\7&\u0167\n&\f&\16&\u016a\13&\3")
        buf.write("\'\3\'\3\'\5\'\u016f\n\'\3(\3(\3(\5(\u0174\n(\3)\3)\3")
        buf.write(")\3)\5)\u017a\n)\3*\3*\3*\3*\3*\5*\u0181\n*\3+\3+\3+\3")
        buf.write("+\3+\3+\5+\u0189\n+\3,\3,\3,\5,\u018e\n,\3-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\5-\u0199\n-\3.\3.\3.\5.\u019e\n.\3.\3.\3")
        buf.write("/\3/\5/\u01a4\n/\3/\3/\3\60\3\60\3\60\7\60\u01ab\n\60")
        buf.write("\f\60\16\60\u01ae\13\60\3\61\3\61\3\61\5\61\u01b3\n\61")
        buf.write("\3\61\2\5FHJ\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\b\3\2\60")
        buf.write("\63\3\2\4\16\3\2\17\20\3\2\21\24\3\2\25\31\3\2\23\24\2")
        buf.write("\u01b3\2b\3\2\2\2\4i\3\2\2\2\6l\3\2\2\2\bq\3\2\2\2\ny")
        buf.write("\3\2\2\2\f\u0086\3\2\2\2\16\u0088\3\2\2\2\20\u008c\3\2")
        buf.write("\2\2\22\u008e\3\2\2\2\24\u0090\3\2\2\2\26\u0095\3\2\2")
        buf.write("\2\30\u0098\3\2\2\2\32\u00a6\3\2\2\2\34\u00a8\3\2\2\2")
        buf.write("\36\u00b0\3\2\2\2 \u00bc\3\2\2\2\"\u00cd\3\2\2\2$\u00d2")
        buf.write("\3\2\2\2&\u00d7\3\2\2\2(\u00e7\3\2\2\2*\u00ec\3\2\2\2")
        buf.write(",\u00ef\3\2\2\2.\u00fe\3\2\2\2\60\u0105\3\2\2\2\62\u010c")
        buf.write("\3\2\2\2\64\u010f\3\2\2\2\66\u0112\3\2\2\28\u011a\3\2")
        buf.write("\2\2:\u0122\3\2\2\2<\u0128\3\2\2\2>\u0133\3\2\2\2@\u0135")
        buf.write("\3\2\2\2B\u0137\3\2\2\2D\u0148\3\2\2\2F\u014a\3\2\2\2")
        buf.write("H\u0155\3\2\2\2J\u0160\3\2\2\2L\u016e\3\2\2\2N\u0173\3")
        buf.write("\2\2\2P\u0179\3\2\2\2R\u0180\3\2\2\2T\u0188\3\2\2\2V\u018d")
        buf.write("\3\2\2\2X\u0198\3\2\2\2Z\u019a\3\2\2\2\\\u01a1\3\2\2\2")
        buf.write("^\u01a7\3\2\2\2`\u01b2\3\2\2\2bc\5\4\3\2cd\5\26\f\2de")
        buf.write("\7\2\2\3e\3\3\2\2\2fh\5\6\4\2gf\3\2\2\2hk\3\2\2\2ig\3")
        buf.write("\2\2\2ij\3\2\2\2j\5\3\2\2\2ki\3\2\2\2lm\7-\2\2mn\7=\2")
        buf.write("\2no\5\b\5\2op\7:\2\2p\7\3\2\2\2qv\5\n\6\2rs\7<\2\2su")
        buf.write("\5\n\6\2tr\3\2\2\2ux\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\t\3")
        buf.write("\2\2\2xv\3\2\2\2y\177\7\34\2\2z{\78\2\2{|\7\61\2\2|~\7")
        buf.write("9\2\2}z\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\u0084\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083")
        buf.write("\7\3\2\2\u0083\u0085\5\f\7\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\13\3\2\2\2\u0086\u0087\5\16\b\2\u0087")
        buf.write("\r\3\2\2\2\u0088\u0089\5\20\t\2\u0089\17\3\2\2\2\u008a")
        buf.write("\u008d\5\22\n\2\u008b\u008d\5\24\13\2\u008c\u008a\3\2")
        buf.write("\2\2\u008c\u008b\3\2\2\2\u008d\21\3\2\2\2\u008e\u008f")
        buf.write("\t\2\2\2\u008f\23\3\2\2\2\u0090\u0091\5\\/\2\u0091\25")
        buf.write("\3\2\2\2\u0092\u0094\5\30\r\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\27\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7(\2")
        buf.write("\2\u0099\u009a\7=\2\2\u009a\u009e\5\32\16\2\u009b\u009c")
        buf.write("\7*\2\2\u009c\u009d\7=\2\2\u009d\u009f\5\34\17\2\u009e")
        buf.write("\u009b\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u00a1\7\35\2\2\u00a1\u00a2\7=\2\2\u00a2\u00a3\5")
        buf.write(" \21\2\u00a3\u00a4\7#\2\2\u00a4\u00a5\7;\2\2\u00a5\31")
        buf.write("\3\2\2\2\u00a6\u00a7\7\34\2\2\u00a7\33\3\2\2\2\u00a8\u00ad")
        buf.write("\5\36\20\2\u00a9\u00aa\7<\2\2\u00aa\u00ac\5\36\20\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\35\3\2\2\2\u00af\u00ad\3\2")
        buf.write("\2\2\u00b0\u00b6\7\34\2\2\u00b1\u00b2\78\2\2\u00b2\u00b3")
        buf.write("\7\61\2\2\u00b3\u00b5\79\2\2\u00b4\u00b1\3\2\2\2\u00b5")
        buf.write("\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\37\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bb\5\"")
        buf.write("\22\2\u00ba\u00b9\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00ca\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00bf\u00c9\5$\23\2\u00c0\u00c9\5&\24\2")
        buf.write("\u00c1\u00c9\5,\27\2\u00c2\u00c9\5.\30\2\u00c3\u00c9\5")
        buf.write("\60\31\2\u00c4\u00c9\5\62\32\2\u00c5\u00c9\5\64\33\2\u00c6")
        buf.write("\u00c9\5\66\34\2\u00c7\u00c9\5:\36\2\u00c8\u00bf\3\2\2")
        buf.write("\2\u00c8\u00c0\3\2\2\2\u00c8\u00c1\3\2\2\2\u00c8\u00c2")
        buf.write("\3\2\2\2\u00c8\u00c3\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8")
        buf.write("\u00c5\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2")
        buf.write("\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00cb!\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce")
        buf.write("\7-\2\2\u00ce\u00cf\7=\2\2\u00cf\u00d0\5\b\5\2\u00d0\u00d1")
        buf.write("\7:\2\2\u00d1#\3\2\2\2\u00d2\u00d3\5> \2\u00d3\u00d4\7")
        buf.write("\3\2\2\u00d4\u00d5\5D#\2\u00d5\u00d6\7:\2\2\u00d6%\3\2")
        buf.write("\2\2\u00d7\u00d8\7)\2\2\u00d8\u00d9\5D#\2\u00d9\u00da")
        buf.write("\7,\2\2\u00da\u00de\5 \21\2\u00db\u00dd\5(\25\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3")
        buf.write("\2\2\2\u00e1\u00e3\5*\26\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\7$\2\2\u00e5")
        buf.write("\u00e6\7;\2\2\u00e6\'\3\2\2\2\u00e7\u00e8\7\"\2\2\u00e8")
        buf.write("\u00e9\5D#\2\u00e9\u00ea\7,\2\2\u00ea\u00eb\5 \21\2\u00eb")
        buf.write(")\3\2\2\2\u00ec\u00ed\7!\2\2\u00ed\u00ee\5 \21\2\u00ee")
        buf.write("+\3\2\2\2\u00ef\u00f0\7\'\2\2\u00f0\u00f1\7\66\2\2\u00f1")
        buf.write("\u00f2\5@!\2\u00f2\u00f3\7\3\2\2\u00f3\u00f4\5D#\2\u00f4")
        buf.write("\u00f5\7<\2\2\u00f5\u00f6\5D#\2\u00f6\u00f7\7<\2\2\u00f7")
        buf.write("\u00f8\5D#\2\u00f8\u00f9\7\67\2\2\u00f9\u00fa\7 \2\2\u00fa")
        buf.write("\u00fb\5 \21\2\u00fb\u00fc\7%\2\2\u00fc\u00fd\7;\2\2\u00fd")
        buf.write("-\3\2\2\2\u00fe\u00ff\7.\2\2\u00ff\u0100\5D#\2\u0100\u0101")
        buf.write("\7 \2\2\u0101\u0102\5 \21\2\u0102\u0103\7&\2\2\u0103\u0104")
        buf.write("\7;\2\2\u0104/\3\2\2\2\u0105\u0106\7 \2\2\u0106\u0107")
        buf.write("\5 \21\2\u0107\u0108\7.\2\2\u0108\u0109\5D#\2\u0109\u010a")
        buf.write("\7/\2\2\u010a\u010b\7;\2\2\u010b\61\3\2\2\2\u010c\u010d")
        buf.write("\7\36\2\2\u010d\u010e\7:\2\2\u010e\63\3\2\2\2\u010f\u0110")
        buf.write("\7\37\2\2\u0110\u0111\7:\2\2\u0111\65\3\2\2\2\u0112\u0113")
        buf.write("\5\32\16\2\u0113\u0115\7\66\2\2\u0114\u0116\58\35\2\u0115")
        buf.write("\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u0118\7\67\2\2\u0118\u0119\7:\2\2\u0119\67\3\2")
        buf.write("\2\2\u011a\u011f\5D#\2\u011b\u011c\7<\2\2\u011c\u011e")
        buf.write("\5D#\2\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u01209\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0122\u0124\7+\2\2\u0123\u0125\5D#\2\u0124\u0123")
        buf.write("\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\7:\2\2\u0127;\3\2\2\2\u0128\u012d\5> \2\u0129\u012a")
        buf.write("\7<\2\2\u012a\u012c\5> \2\u012b\u0129\3\2\2\2\u012c\u012f")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("=\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0134\5@!\2\u0131")
        buf.write("\u0134\5B\"\2\u0132\u0134\5D#\2\u0133\u0130\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134?\3\2\2\2\u0135")
        buf.write("\u0136\7\34\2\2\u0136A\3\2\2\2\u0137\u013f\7\34\2\2\u0138")
        buf.write("\u013b\78\2\2\u0139\u013c\5\16\b\2\u013a\u013c\5D#\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013e\79\2\2\u013e\u0140\3\2\2\2\u013f\u0138\3")
        buf.write("\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142")
        buf.write("\3\2\2\2\u0142C\3\2\2\2\u0143\u0144\5F$\2\u0144\u0145")
        buf.write("\t\3\2\2\u0145\u0146\5F$\2\u0146\u0149\3\2\2\2\u0147\u0149")
        buf.write("\5F$\2\u0148\u0143\3\2\2\2\u0148\u0147\3\2\2\2\u0149E")
        buf.write("\3\2\2\2\u014a\u014b\b$\1\2\u014b\u014c\5H%\2\u014c\u0152")
        buf.write("\3\2\2\2\u014d\u014e\f\4\2\2\u014e\u014f\t\4\2\2\u014f")
        buf.write("\u0151\5H%\2\u0150\u014d\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153G\3\2\2\2\u0154")
        buf.write("\u0152\3\2\2\2\u0155\u0156\b%\1\2\u0156\u0157\5J&\2\u0157")
        buf.write("\u015d\3\2\2\2\u0158\u0159\f\4\2\2\u0159\u015a\t\5\2\2")
        buf.write("\u015a\u015c\5J&\2\u015b\u0158\3\2\2\2\u015c\u015f\3\2")
        buf.write("\2\2\u015d\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015eI\3")
        buf.write("\2\2\2\u015f\u015d\3\2\2\2\u0160\u0161\b&\1\2\u0161\u0162")
        buf.write("\5L\'\2\u0162\u0168\3\2\2\2\u0163\u0164\f\4\2\2\u0164")
        buf.write("\u0165\t\6\2\2\u0165\u0167\5L\'\2\u0166\u0163\3\2\2\2")
        buf.write("\u0167\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3")
        buf.write("\2\2\2\u0169K\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u016c")
        buf.write("\7\32\2\2\u016c\u016f\5L\'\2\u016d\u016f\5N(\2\u016e\u016b")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016fM\3\2\2\2\u0170\u0171")
        buf.write("\t\7\2\2\u0171\u0174\5N(\2\u0172\u0174\5P)\2\u0173\u0170")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174O\3\2\2\2\u0175\u0176")
        buf.write("\5T+\2\u0176\u0177\5X-\2\u0177\u017a\3\2\2\2\u0178\u017a")
        buf.write("\5R*\2\u0179\u0175\3\2\2\2\u0179\u0178\3\2\2\2\u017aQ")
        buf.write("\3\2\2\2\u017b\u0181\5V,\2\u017c\u017d\7\66\2\2\u017d")
        buf.write("\u017e\5D#\2\u017e\u017f\7\67\2\2\u017f\u0181\3\2\2\2")
        buf.write("\u0180\u017b\3\2\2\2\u0180\u017c\3\2\2\2\u0181S\3\2\2")
        buf.write("\2\u0182\u0189\7\34\2\2\u0183\u0189\5Z.\2\u0184\u0185")
        buf.write("\7\66\2\2\u0185\u0186\5D#\2\u0186\u0187\7\67\2\2\u0187")
        buf.write("\u0189\3\2\2\2\u0188\u0182\3\2\2\2\u0188\u0183\3\2\2\2")
        buf.write("\u0188\u0184\3\2\2\2\u0189U\3\2\2\2\u018a\u018e\5\32\16")
        buf.write("\2\u018b\u018e\5\16\b\2\u018c\u018e\5Z.\2\u018d\u018a")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("W\3\2\2\2\u018f\u0190\78\2\2\u0190\u0191\5D#\2\u0191\u0192")
        buf.write("\79\2\2\u0192\u0199\3\2\2\2\u0193\u0194\78\2\2\u0194\u0195")
        buf.write("\5D#\2\u0195\u0196\79\2\2\u0196\u0197\5X-\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u018f\3\2\2\2\u0198\u0193\3\2\2\2\u0199")
        buf.write("Y\3\2\2\2\u019a\u019b\7\34\2\2\u019b\u019d\7\66\2\2\u019c")
        buf.write("\u019e\58\35\2\u019d\u019c\3\2\2\2\u019d\u019e\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u01a0\7\67\2\2\u01a0[\3\2\2")
        buf.write("\2\u01a1\u01a3\7\64\2\2\u01a2\u01a4\5^\60\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a6\7\65\2\2\u01a6]\3\2\2\2\u01a7\u01ac\5`\61\2\u01a8")
        buf.write("\u01a9\7<\2\2\u01a9\u01ab\5`\61\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad_\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b3")
        buf.write("\5\20\t\2\u01b0\u01b3\7\34\2\2\u01b1\u01b3\7>\2\2\u01b2")
        buf.write("\u01af\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2")
        buf.write("\u01b3a\3\2\2\2&iv\177\u0084\u008c\u0095\u009e\u00ad\u00b6")
        buf.write("\u00bc\u00c8\u00ca\u00de\u00e2\u0115\u011f\u0124\u012d")
        buf.write("\u0133\u013b\u0141\u0148\u0152\u015d\u0168\u016e\u0173")
        buf.write("\u0179\u0180\u0188\u018d\u0198\u019d\u01a3\u01ac\u01b2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", 
                     "'&&'", "'||'", "'+'", "'+.'", "'-'", "'-.'", "'*'", 
                     "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "<INVALID>", 
                     "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'EndDo'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "';'", "'.'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "IDENT", "BODY", "BREAK", 
                      "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", 
                      "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "FLOAT_LIT", 
                      "INT_LIT", "BOOL_LIT", "STRING_LIT", "LCURLY", "RCURLY", 
                      "LR", "RR", "LB", "RB", "SEMI", "DOT", "COMMA", "COLON", 
                      "WS", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_glo_var_decl_part = 1
    RULE_var_decl = 2
    RULE_variable_list_decl = 3
    RULE_variable_decl = 4
    RULE_init_value = 5
    RULE_literal = 6
    RULE_bktype = 7
    RULE_primitive_type = 8
    RULE_compound_type = 9
    RULE_func_decl_part = 10
    RULE_func_decl = 11
    RULE_func_name = 12
    RULE_param_list = 13
    RULE_func_param_decl = 14
    RULE_statement_list = 15
    RULE_var_decl_statement = 16
    RULE_assign_statement = 17
    RULE_if_statement = 18
    RULE_else_if_part = 19
    RULE_else_part = 20
    RULE_for_statement = 21
    RULE_while_statement = 22
    RULE_do_while_statement = 23
    RULE_break_statement = 24
    RULE_continue_statement = 25
    RULE_call_statement = 26
    RULE_param_func_call = 27
    RULE_return_statement = 28
    RULE_variable_list = 29
    RULE_variable = 30
    RULE_scal_var = 31
    RULE_comp_var = 32
    RULE_expression = 33
    RULE_exp1 = 34
    RULE_exp2 = 35
    RULE_exp3 = 36
    RULE_exp4 = 37
    RULE_exp5 = 38
    RULE_exp6 = 39
    RULE_exp7 = 40
    RULE_name_index_op = 41
    RULE_operand = 42
    RULE_index_operator = 43
    RULE_func_call_expr = 44
    RULE_array = 45
    RULE_arr_elem_list = 46
    RULE_arr_elem = 47

    ruleNames =  [ "program", "glo_var_decl_part", "var_decl", "variable_list_decl", 
                   "variable_decl", "init_value", "literal", "bktype", "primitive_type", 
                   "compound_type", "func_decl_part", "func_decl", "func_name", 
                   "param_list", "func_param_decl", "statement_list", "var_decl_statement", 
                   "assign_statement", "if_statement", "else_if_part", "else_part", 
                   "for_statement", "while_statement", "do_while_statement", 
                   "break_statement", "continue_statement", "call_statement", 
                   "param_func_call", "return_statement", "variable_list", 
                   "variable", "scal_var", "comp_var", "expression", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "name_index_op", 
                   "operand", "index_operator", "func_call_expr", "array", 
                   "arr_elem_list", "arr_elem" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    COMMENT=25
    IDENT=26
    BODY=27
    BREAK=28
    CONTINUE=29
    DO=30
    ELSE=31
    ELSEIF=32
    ENDBODY=33
    ENDIF=34
    ENDFOR=35
    ENDWHILE=36
    FOR=37
    FUNCTION=38
    IF=39
    PARAMETER=40
    RETURN=41
    THEN=42
    VAR=43
    WHILE=44
    ENDDO=45
    FLOAT_LIT=46
    INT_LIT=47
    BOOL_LIT=48
    STRING_LIT=49
    LCURLY=50
    RCURLY=51
    LR=52
    RR=53
    LB=54
    RB=55
    SEMI=56
    DOT=57
    COMMA=58
    COLON=59
    WS=60
    UNCLOSE_STRING=61
    UNTERMINATED_COMMENT=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def glo_var_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Glo_var_decl_partContext,0)


        def func_decl_part(self):
            return self.getTypedRuleContext(BKITParser.Func_decl_partContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.glo_var_decl_part()
            self.state = 97
            self.func_decl_part()
            self.state = 98
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Glo_var_decl_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_glo_var_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlo_var_decl_part" ):
                return visitor.visitGlo_var_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def glo_var_decl_part(self):

        localctx = BKITParser.Glo_var_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_glo_var_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 100
                self.var_decl()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list_decl(self):
            return self.getTypedRuleContext(BKITParser.Variable_list_declContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BKITParser.VAR)
            self.state = 107
            self.match(BKITParser.COLON)
            self.state = 108
            self.variable_list_decl()
            self.state = 109
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_list_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_list_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list_decl" ):
                return visitor.visitVariable_list_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_list_decl(self):

        localctx = BKITParser.Variable_list_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_list_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.variable_decl()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 112
                self.match(BKITParser.COMMA)
                self.state = 113
                self.variable_decl()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LB)
            else:
                return self.getToken(BKITParser.LB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RB)
            else:
                return self.getToken(BKITParser.RB, i)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKITParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKITParser.IDENT)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LB:
                self.state = 120
                self.match(BKITParser.LB)
                self.state = 121
                self.match(BKITParser.INT_LIT)
                self.state = 122
                self.match(BKITParser.RB)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.T__0:
                self.state = 128
                self.match(BKITParser.T__0)
                self.state = 129
                self.init_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bktype(self):
            return self.getTypedRuleContext(BKITParser.BktypeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.bktype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BktypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(BKITParser.Primitive_typeContext,0)


        def compound_type(self):
            return self.getTypedRuleContext(BKITParser.Compound_typeContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_bktype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBktype" ):
                return visitor.visitBktype(self)
            else:
                return visitor.visitChildren(self)




    def bktype(self):

        localctx = BKITParser.BktypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bktype)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FLOAT_LIT, BKITParser.INT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.primitive_type()
                pass
            elif token in [BKITParser.LCURLY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.compound_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def BOOL_LIT(self):
            return self.getToken(BKITParser.BOOL_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = BKITParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_compound_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_type" ):
                return visitor.visitCompound_type(self)
            else:
                return visitor.visitChildren(self)




    def compound_type(self):

        localctx = BKITParser.Compound_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_compound_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decl_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl_part" ):
                return visitor.visitFunc_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def func_decl_part(self):

        localctx = BKITParser.Func_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 144
                self.func_decl()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def func_name(self):
            return self.getTypedRuleContext(BKITParser.Func_nameContext,0)


        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(BKITParser.FUNCTION)
            self.state = 151
            self.match(BKITParser.COLON)
            self.state = 152
            self.func_name()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 153
                self.match(BKITParser.PARAMETER)
                self.state = 154
                self.match(BKITParser.COLON)
                self.state = 155
                self.param_list()


            self.state = 158
            self.match(BKITParser.BODY)
            self.state = 159
            self.match(BKITParser.COLON)
            self.state = 160
            self.statement_list()
            self.state = 161
            self.match(BKITParser.ENDBODY)
            self.state = 162
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_func_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_name" ):
                return visitor.visitFunc_name(self)
            else:
                return visitor.visitChildren(self)




    def func_name(self):

        localctx = BKITParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKITParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_param_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_param_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_param_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.func_param_decl()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 167
                self.match(BKITParser.COMMA)
                self.state = 168
                self.func_param_decl()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_param_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LB)
            else:
                return self.getToken(BKITParser.LB, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RB)
            else:
                return self.getToken(BKITParser.RB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_param_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param_decl" ):
                return visitor.visitFunc_param_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_param_decl(self):

        localctx = BKITParser.Func_param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(BKITParser.IDENT)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LB:
                self.state = 175
                self.match(BKITParser.LB)
                self.state = 176
                self.match(BKITParser.INT_LIT)
                self.state = 177
                self.match(BKITParser.RB)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decl_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decl_statementContext,i)


        def assign_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Assign_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Assign_statementContext,i)


        def if_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.If_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.If_statementContext,i)


        def for_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.For_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.For_statementContext,i)


        def while_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.While_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.While_statementContext,i)


        def do_while_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Do_while_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Do_while_statementContext,i)


        def break_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Break_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Break_statementContext,i)


        def continue_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Continue_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Continue_statementContext,i)


        def call_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Call_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Call_statementContext,i)


        def return_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Return_statementContext)
            else:
                return self.getTypedRuleContext(BKITParser.Return_statementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = BKITParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 183
                self.var_decl_statement()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 198
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        self.state = 189
                        self.assign_statement()
                        pass

                    elif la_ == 2:
                        self.state = 190
                        self.if_statement()
                        pass

                    elif la_ == 3:
                        self.state = 191
                        self.for_statement()
                        pass

                    elif la_ == 4:
                        self.state = 192
                        self.while_statement()
                        pass

                    elif la_ == 5:
                        self.state = 193
                        self.do_while_statement()
                        pass

                    elif la_ == 6:
                        self.state = 194
                        self.break_statement()
                        pass

                    elif la_ == 7:
                        self.state = 195
                        self.continue_statement()
                        pass

                    elif la_ == 8:
                        self.state = 196
                        self.call_statement()
                        pass

                    elif la_ == 9:
                        self.state = 197
                        self.return_statement()
                        pass

             
                self.state = 202
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list_decl(self):
            return self.getTypedRuleContext(BKITParser.Variable_list_declContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl_statement" ):
                return visitor.visitVar_decl_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_decl_statement(self):

        localctx = BKITParser.Var_decl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_decl_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BKITParser.VAR)
            self.state = 204
            self.match(BKITParser.COLON)
            self.state = 205
            self.variable_list_decl()
            self.state = 206
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = BKITParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.variable()
            self.state = 209
            self.match(BKITParser.T__0)
            self.state = 210
            self.expression()
            self.state = 211
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def else_if_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Else_if_partContext)
            else:
                return self.getTypedRuleContext(BKITParser.Else_if_partContext,i)


        def else_part(self):
            return self.getTypedRuleContext(BKITParser.Else_partContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = BKITParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(BKITParser.IF)
            self.state = 214
            self.expression()
            self.state = 215
            self.match(BKITParser.THEN)
            self.state = 216
            self.statement_list()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 217
                self.else_if_part()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 223
                self.else_part()


            self.state = 226
            self.match(BKITParser.ENDIF)
            self.state = 227
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_part" ):
                return visitor.visitElse_if_part(self)
            else:
                return visitor.visitChildren(self)




    def else_if_part(self):

        localctx = BKITParser.Else_if_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_else_if_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BKITParser.ELSEIF)
            self.state = 230
            self.expression()
            self.state = 231
            self.match(BKITParser.THEN)
            self.state = 232
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = BKITParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_else_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.ELSE)
            self.state = 235
            self.statement_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def scal_var(self):
            return self.getTypedRuleContext(BKITParser.Scal_varContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = BKITParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(BKITParser.FOR)
            self.state = 238
            self.match(BKITParser.LR)
            self.state = 239
            self.scal_var()
            self.state = 240
            self.match(BKITParser.T__0)
            self.state = 241
            self.expression()
            self.state = 242
            self.match(BKITParser.COMMA)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(BKITParser.COMMA)
            self.state = 245
            self.expression()
            self.state = 246
            self.match(BKITParser.RR)
            self.state = 247
            self.match(BKITParser.DO)
            self.state = 248
            self.statement_list()
            self.state = 249
            self.match(BKITParser.ENDFOR)
            self.state = 250
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = BKITParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(BKITParser.WHILE)
            self.state = 253
            self.expression()
            self.state = 254
            self.match(BKITParser.DO)
            self.state = 255
            self.statement_list()
            self.state = 256
            self.match(BKITParser.ENDWHILE)
            self.state = 257
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def statement_list(self):
            return self.getTypedRuleContext(BKITParser.Statement_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_statement" ):
                return visitor.visitDo_while_statement(self)
            else:
                return visitor.visitChildren(self)




    def do_while_statement(self):

        localctx = BKITParser.Do_while_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_do_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(BKITParser.DO)
            self.state = 260
            self.statement_list()
            self.state = 261
            self.match(BKITParser.WHILE)
            self.state = 262
            self.expression()
            self.state = 263
            self.match(BKITParser.ENDDO)
            self.state = 264
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = BKITParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(BKITParser.BREAK)
            self.state = 267
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = BKITParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(BKITParser.CONTINUE)
            self.state = 270
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_name(self):
            return self.getTypedRuleContext(BKITParser.Func_nameContext,0)


        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def param_func_call(self):
            return self.getTypedRuleContext(BKITParser.Param_func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = BKITParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.func_name()
            self.state = 273
            self.match(BKITParser.LR)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__16) | (1 << BKITParser.T__17) | (1 << BKITParser.T__23) | (1 << BKITParser.IDENT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LCURLY) | (1 << BKITParser.LR))) != 0):
                self.state = 274
                self.param_func_call()


            self.state = 277
            self.match(BKITParser.RR)
            self.state = 278
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_func_call" ):
                return visitor.visitParam_func_call(self)
            else:
                return visitor.visitChildren(self)




    def param_func_call(self):

        localctx = BKITParser.Param_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_param_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.expression()
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 281
                self.match(BKITParser.COMMA)
                self.state = 282
                self.expression()
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = BKITParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BKITParser.RETURN)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__16) | (1 << BKITParser.T__17) | (1 << BKITParser.T__23) | (1 << BKITParser.IDENT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LCURLY) | (1 << BKITParser.LR))) != 0):
                self.state = 289
                self.expression()


            self.state = 292
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VariableContext)
            else:
                return self.getTypedRuleContext(BKITParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.variable()
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 295
                self.match(BKITParser.COMMA)
                self.state = 296
                self.variable()
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scal_var(self):
            return self.getTypedRuleContext(BKITParser.Scal_varContext,0)


        def comp_var(self):
            return self.getTypedRuleContext(BKITParser.Comp_varContext,0)


        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_variable)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.scal_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.comp_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scal_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scal_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScal_var" ):
                return visitor.visitScal_var(self)
            else:
                return visitor.visitChildren(self)




    def scal_var(self):

        localctx = BKITParser.Scal_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_scal_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(BKITParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comp_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LB)
            else:
                return self.getToken(BKITParser.LB, i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RB)
            else:
                return self.getToken(BKITParser.RB, i)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_comp_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_var" ):
                return visitor.visitComp_var(self)
            else:
                return visitor.visitChildren(self)




    def comp_var(self):

        localctx = BKITParser.Comp_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_comp_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(BKITParser.IDENT)
            self.state = 317 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 310
                self.match(BKITParser.LB)
                self.state = 313
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 311
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 312
                    self.expression()
                    pass


                self.state = 315
                self.match(BKITParser.RB)
                self.state = 319 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def getRuleIndex(self):
            return BKITParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.exp1(0)
                self.state = 322
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__1) | (1 << BKITParser.T__2) | (1 << BKITParser.T__3) | (1 << BKITParser.T__4) | (1 << BKITParser.T__5) | (1 << BKITParser.T__6) | (1 << BKITParser.T__7) | (1 << BKITParser.T__8) | (1 << BKITParser.T__9) | (1 << BKITParser.T__10) | (1 << BKITParser.T__11))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 332
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.T__12 or _la==BKITParser.T__13):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 333
                    self.exp2(0) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 347
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 342
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 343
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__14) | (1 << BKITParser.T__15) | (1 << BKITParser.T__16) | (1 << BKITParser.T__17))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 344
                    self.exp3(0) 
                self.state = 349
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 358
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 353
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 354
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__18) | (1 << BKITParser.T__19) | (1 << BKITParser.T__20) | (1 << BKITParser.T__21) | (1 << BKITParser.T__22))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 355
                    self.exp4() 
                self.state = 360
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp4)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.T__23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(BKITParser.T__23)
                self.state = 362
                self.exp4()
                pass
            elif token in [BKITParser.T__16, BKITParser.T__17, BKITParser.IDENT, BKITParser.FLOAT_LIT, BKITParser.INT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LCURLY, BKITParser.LR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.T__16, BKITParser.T__17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                _la = self._input.LA(1)
                if not(_la==BKITParser.T__16 or _la==BKITParser.T__17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 367
                self.exp5()
                pass
            elif token in [BKITParser.IDENT, BKITParser.FLOAT_LIT, BKITParser.INT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LCURLY, BKITParser.LR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_index_op(self):
            return self.getTypedRuleContext(BKITParser.Name_index_opContext,0)


        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_exp6)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.name_index_op()
                self.state = 372
                self.index_operator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.exp7()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(BKITParser.OperandContext,0)


        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp7)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IDENT, BKITParser.FLOAT_LIT, BKITParser.INT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LCURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.operand()
                pass
            elif token in [BKITParser.LR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.match(BKITParser.LR)
                self.state = 379
                self.expression()
                self.state = 380
                self.match(BKITParser.RR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_index_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(BKITParser.Func_call_exprContext,0)


        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_name_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_index_op" ):
                return visitor.visitName_index_op(self)
            else:
                return visitor.visitChildren(self)




    def name_index_op(self):

        localctx = BKITParser.Name_index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_name_index_op)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(BKITParser.IDENT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.func_call_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.match(BKITParser.LR)
                self.state = 387
                self.expression()
                self.state = 388
                self.match(BKITParser.RR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_name(self):
            return self.getTypedRuleContext(BKITParser.Func_nameContext,0)


        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(BKITParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKITParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operand)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.func_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 394
                self.func_call_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def index_operator(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operator" ):
                return visitor.visitIndex_operator(self)
            else:
                return visitor.visitChildren(self)




    def index_operator(self):

        localctx = BKITParser.Index_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_index_operator)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(BKITParser.LB)
                self.state = 398
                self.expression()
                self.state = 399
                self.match(BKITParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.match(BKITParser.LB)
                self.state = 402
                self.expression()
                self.state = 403
                self.match(BKITParser.RB)
                self.state = 404
                self.index_operator()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def LR(self):
            return self.getToken(BKITParser.LR, 0)

        def RR(self):
            return self.getToken(BKITParser.RR, 0)

        def param_func_call(self):
            return self.getTypedRuleContext(BKITParser.Param_func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




    def func_call_expr(self):

        localctx = BKITParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_func_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(BKITParser.IDENT)
            self.state = 409
            self.match(BKITParser.LR)
            self.state = 411
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.T__16) | (1 << BKITParser.T__17) | (1 << BKITParser.T__23) | (1 << BKITParser.IDENT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LCURLY) | (1 << BKITParser.LR))) != 0):
                self.state = 410
                self.param_func_call()


            self.state = 413
            self.match(BKITParser.RR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCURLY(self):
            return self.getToken(BKITParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(BKITParser.RCURLY, 0)

        def arr_elem_list(self):
            return self.getTypedRuleContext(BKITParser.Arr_elem_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(BKITParser.LCURLY)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.IDENT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.INT_LIT) | (1 << BKITParser.BOOL_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.LCURLY) | (1 << BKITParser.WS))) != 0):
                self.state = 416
                self.arr_elem_list()


            self.state = 419
            self.match(BKITParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elem_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Arr_elemContext)
            else:
                return self.getTypedRuleContext(BKITParser.Arr_elemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_arr_elem_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem_list" ):
                return visitor.visitArr_elem_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem_list(self):

        localctx = BKITParser.Arr_elem_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_arr_elem_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.arr_elem()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 422
                self.match(BKITParser.COMMA)
                self.state = 423
                self.arr_elem()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bktype(self):
            return self.getTypedRuleContext(BKITParser.BktypeContext,0)


        def IDENT(self):
            return self.getToken(BKITParser.IDENT, 0)

        def WS(self):
            return self.getToken(BKITParser.WS, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_arr_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elem" ):
                return visitor.visitArr_elem(self)
            else:
                return visitor.visitChildren(self)




    def arr_elem(self):

        localctx = BKITParser.Arr_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arr_elem)
        try:
            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.FLOAT_LIT, BKITParser.INT_LIT, BKITParser.BOOL_LIT, BKITParser.STRING_LIT, BKITParser.LCURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.bktype()
                pass
            elif token in [BKITParser.IDENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.match(BKITParser.IDENT)
                pass
            elif token in [BKITParser.WS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 431
                self.match(BKITParser.WS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[34] = self.exp1_sempred
        self._predicates[35] = self.exp2_sempred
        self._predicates[36] = self.exp3_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




