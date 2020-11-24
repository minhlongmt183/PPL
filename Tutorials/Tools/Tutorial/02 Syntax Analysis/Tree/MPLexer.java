// Generated from MP.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MPLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LINE_CMT=1, BLOCK_CMT_1=2, BLOCK_CMT_2=3, ANDTHEN=4, ORELSE=5, BREAK=6, 
		CONTINUE=7, FOR=8, WHILE=9, TO=10, DOWNTO=11, WITH=12, DO=13, IF=14, THEN=15, 
		ELSE=16, VAR=17, OF=18, BEGIN=19, END=20, RETURN=21, FUNCTION=22, PROCEDURE=23, 
		ARRAY=24, REAL=25, BOOLEAN=26, INTEGER=27, STRING=28, NOT=29, AND=30, 
		OR=31, DIV=32, MOD=33, ADD=34, SUB=35, MUL=36, DIV_F=37, EQUAL=38, NOTEQUAL=39, 
		LESSTHAN=40, GREATERTHAN=41, LESSEQUAL=42, GREATEREQUAL=43, ASSIGN=44, 
		LSB=45, RSB=46, COLON=47, LB=48, RB=49, SEMI=50, DDOT=51, COMMA=52, INTEGER_LITERAL=53, 
		REAL_LITERAL=54, BOOLEAN_LITERAL=55, TRUE=56, FALSE=57, UNCLOSE_STRING=58, 
		ILLEGAL_ESCAPE=59, STRING_LITERAL=60, IDENTIFIER=61, WS=62, ERROR_CHAR=63;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
		"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "LINE_CMT", 
		"BLOCK_CMT_1", "BLOCK_CMT_2", "ANDTHEN", "ORELSE", "BREAK", "CONTINUE", 
		"FOR", "WHILE", "TO", "DOWNTO", "WITH", "DO", "IF", "THEN", "ELSE", "VAR", 
		"OF", "BEGIN", "END", "RETURN", "FUNCTION", "PROCEDURE", "ARRAY", "REAL", 
		"BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADD", 
		"SUB", "MUL", "DIV_F", "EQUAL", "NOTEQUAL", "LESSTHAN", "GREATERTHAN", 
		"LESSEQUAL", "GREATEREQUAL", "ASSIGN", "LSB", "RSB", "COLON", "LB", "RB", 
		"SEMI", "DDOT", "COMMA", "DIGIT", "INTEGER_LITERAL", "EXPONENT", "REAL_LITERAL", 
		"BOOLEAN_LITERAL", "TRUE", "FALSE", "BSP", "FF", "CR", "NEWLINE", "TAB", 
		"SQUOTE", "DQUOTE", "BSL", "LEGAL_ESCAPE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
		"STRING_LITERAL", "IDENTIFIER", "WS", "ERROR_CHAR"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, "'+'", "'-'", 
		"'*'", "'/'", "'='", "'<>'", "'<'", "'>'", "'<='", "'>='", "':='", "'['", 
		"']'", "':'", "'('", "')'", "';'", "'..'", "','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "LINE_CMT", "BLOCK_CMT_1", "BLOCK_CMT_2", "ANDTHEN", "ORELSE", "BREAK", 
		"CONTINUE", "FOR", "WHILE", "TO", "DOWNTO", "WITH", "DO", "IF", "THEN", 
		"ELSE", "VAR", "OF", "BEGIN", "END", "RETURN", "FUNCTION", "PROCEDURE", 
		"ARRAY", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
		"MOD", "ADD", "SUB", "MUL", "DIV_F", "EQUAL", "NOTEQUAL", "LESSTHAN", 
		"GREATERTHAN", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "LSB", "RSB", "COLON", 
		"LB", "RB", "SEMI", "DDOT", "COMMA", "INTEGER_LITERAL", "REAL_LITERAL", 
		"BOOLEAN_LITERAL", "TRUE", "FALSE", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
		"STRING_LITERAL", "IDENTIFIER", "WS", "ERROR_CHAR"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MPLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A\u0272\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4_\t_\4"+
		"`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6"+
		"\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3"+
		"\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3"+
		"\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3"+
		"\34\3\34\3\34\7\34\u0104\n\34\f\34\16\34\u0107\13\34\3\34\3\34\3\35\3"+
		"\35\7\35\u010d\n\35\f\35\16\35\u0110\13\35\3\35\3\35\3\35\3\35\3\36\3"+
		"\36\3\36\3\36\7\36\u011a\n\36\f\36\16\36\u011d\13\36\3\36\3\36\3\36\3"+
		"\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3"+
		" \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3"+
		"#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3"+
		"\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3"+
		"-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61"+
		"\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62"+
		"\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64"+
		"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66"+
		"\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\3"+
		"9\39\3:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3"+
		"B\3B\3B\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3I\3I\3J\3J\3K\3"+
		"K\3L\3L\3M\3M\3N\3N\3N\3O\3O\3P\3P\3Q\6Q\u01fb\nQ\rQ\16Q\u01fc\3R\3R\5"+
		"R\u0201\nR\3R\6R\u0204\nR\rR\16R\u0205\3S\6S\u0209\nS\rS\16S\u020a\3S"+
		"\3S\7S\u020f\nS\fS\16S\u0212\13S\5S\u0214\nS\3S\5S\u0217\nS\3S\3S\6S\u021b"+
		"\nS\rS\16S\u021c\3S\5S\u0220\nS\5S\u0222\nS\3T\3T\5T\u0226\nT\3U\3U\3"+
		"U\3U\3U\3V\3V\3V\3V\3V\3V\3W\3W\3W\3X\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3"+
		"[\3\\\3\\\3\\\3]\3]\3]\3^\3^\3^\3_\3_\3_\3_\3_\3_\3_\3_\5_\u0253\n_\3"+
		"`\3`\3`\7`\u0258\n`\f`\16`\u025b\13`\3a\3a\3a\3b\3b\3b\3c\3c\7c\u0265"+
		"\nc\fc\16c\u0268\13c\3d\6d\u026b\nd\rd\16d\u026c\3d\3d\3e\3e\4\u010e\u011b"+
		"\2f\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37"+
		"\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG"+
		"\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g\33i\34"+
		"k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087+\u0089,\u008b"+
		"-\u008d.\u008f/\u0091\60\u0093\61\u0095\62\u0097\63\u0099\64\u009b\65"+
		"\u009d\66\u009f\2\u00a1\67\u00a3\2\u00a58\u00a79\u00a9:\u00ab;\u00ad\2"+
		"\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf"+
		"<\u00c1=\u00c3>\u00c5?\u00c7@\u00c9A\3\2#\4\2CCcc\4\2DDdd\4\2EEee\4\2"+
		"FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4"+
		"\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWw"+
		"w\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\3\2\f\f\3\2\62;\7\2\n\f\16"+
		"\17$$))^^\6\2\n\13\16\16))^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17"+
		"\"\"\2\u0265\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2"+
		"\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M"+
		"\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2"+
		"\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2"+
		"\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s"+
		"\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177"+
		"\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2"+
		"\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091"+
		"\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2"+
		"\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u00a1\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7"+
		"\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2"+
		"\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\3\u00cb"+
		"\3\2\2\2\5\u00cd\3\2\2\2\7\u00cf\3\2\2\2\t\u00d1\3\2\2\2\13\u00d3\3\2"+
		"\2\2\r\u00d5\3\2\2\2\17\u00d7\3\2\2\2\21\u00d9\3\2\2\2\23\u00db\3\2\2"+
		"\2\25\u00dd\3\2\2\2\27\u00df\3\2\2\2\31\u00e1\3\2\2\2\33\u00e3\3\2\2\2"+
		"\35\u00e5\3\2\2\2\37\u00e7\3\2\2\2!\u00e9\3\2\2\2#\u00eb\3\2\2\2%\u00ed"+
		"\3\2\2\2\'\u00ef\3\2\2\2)\u00f1\3\2\2\2+\u00f3\3\2\2\2-\u00f5\3\2\2\2"+
		"/\u00f7\3\2\2\2\61\u00f9\3\2\2\2\63\u00fb\3\2\2\2\65\u00fd\3\2\2\2\67"+
		"\u00ff\3\2\2\29\u010a\3\2\2\2;\u0115\3\2\2\2=\u0123\3\2\2\2?\u012c\3\2"+
		"\2\2A\u0134\3\2\2\2C\u013a\3\2\2\2E\u0143\3\2\2\2G\u0147\3\2\2\2I\u014d"+
		"\3\2\2\2K\u0150\3\2\2\2M\u0157\3\2\2\2O\u015c\3\2\2\2Q\u015f\3\2\2\2S"+
		"\u0162\3\2\2\2U\u0167\3\2\2\2W\u016c\3\2\2\2Y\u0170\3\2\2\2[\u0173\3\2"+
		"\2\2]\u0179\3\2\2\2_\u017d\3\2\2\2a\u0184\3\2\2\2c\u018d\3\2\2\2e\u0197"+
		"\3\2\2\2g\u019d\3\2\2\2i\u01a2\3\2\2\2k\u01aa\3\2\2\2m\u01b2\3\2\2\2o"+
		"\u01b9\3\2\2\2q\u01bd\3\2\2\2s\u01c1\3\2\2\2u\u01c4\3\2\2\2w\u01c8\3\2"+
		"\2\2y\u01cc\3\2\2\2{\u01ce\3\2\2\2}\u01d0\3\2\2\2\177\u01d2\3\2\2\2\u0081"+
		"\u01d4\3\2\2\2\u0083\u01d6\3\2\2\2\u0085\u01d9\3\2\2\2\u0087\u01db\3\2"+
		"\2\2\u0089\u01dd\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e3\3\2\2\2\u008f"+
		"\u01e6\3\2\2\2\u0091\u01e8\3\2\2\2\u0093\u01ea\3\2\2\2\u0095\u01ec\3\2"+
		"\2\2\u0097\u01ee\3\2\2\2\u0099\u01f0\3\2\2\2\u009b\u01f2\3\2\2\2\u009d"+
		"\u01f5\3\2\2\2\u009f\u01f7\3\2\2\2\u00a1\u01fa\3\2\2\2\u00a3\u01fe\3\2"+
		"\2\2\u00a5\u0221\3\2\2\2\u00a7\u0225\3\2\2\2\u00a9\u0227\3\2\2\2\u00ab"+
		"\u022c\3\2\2\2\u00ad\u0232\3\2\2\2\u00af\u0235\3\2\2\2\u00b1\u0238\3\2"+
		"\2\2\u00b3\u023b\3\2\2\2\u00b5\u023e\3\2\2\2\u00b7\u0241\3\2\2\2\u00b9"+
		"\u0244\3\2\2\2\u00bb\u0247\3\2\2\2\u00bd\u0252\3\2\2\2\u00bf\u0254\3\2"+
		"\2\2\u00c1\u025c\3\2\2\2\u00c3\u025f\3\2\2\2\u00c5\u0262\3\2\2\2\u00c7"+
		"\u026a\3\2\2\2\u00c9\u0270\3\2\2\2\u00cb\u00cc\t\2\2\2\u00cc\4\3\2\2\2"+
		"\u00cd\u00ce\t\3\2\2\u00ce\6\3\2\2\2\u00cf\u00d0\t\4\2\2\u00d0\b\3\2\2"+
		"\2\u00d1\u00d2\t\5\2\2\u00d2\n\3\2\2\2\u00d3\u00d4\t\6\2\2\u00d4\f\3\2"+
		"\2\2\u00d5\u00d6\t\7\2\2\u00d6\16\3\2\2\2\u00d7\u00d8\t\b\2\2\u00d8\20"+
		"\3\2\2\2\u00d9\u00da\t\t\2\2\u00da\22\3\2\2\2\u00db\u00dc\t\n\2\2\u00dc"+
		"\24\3\2\2\2\u00dd\u00de\t\13\2\2\u00de\26\3\2\2\2\u00df\u00e0\t\f\2\2"+
		"\u00e0\30\3\2\2\2\u00e1\u00e2\t\r\2\2\u00e2\32\3\2\2\2\u00e3\u00e4\t\16"+
		"\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\t\17\2\2\u00e6\36\3\2\2\2\u00e7\u00e8"+
		"\t\20\2\2\u00e8 \3\2\2\2\u00e9\u00ea\t\21\2\2\u00ea\"\3\2\2\2\u00eb\u00ec"+
		"\t\22\2\2\u00ec$\3\2\2\2\u00ed\u00ee\t\23\2\2\u00ee&\3\2\2\2\u00ef\u00f0"+
		"\t\24\2\2\u00f0(\3\2\2\2\u00f1\u00f2\t\25\2\2\u00f2*\3\2\2\2\u00f3\u00f4"+
		"\t\26\2\2\u00f4,\3\2\2\2\u00f5\u00f6\t\27\2\2\u00f6.\3\2\2\2\u00f7\u00f8"+
		"\t\30\2\2\u00f8\60\3\2\2\2\u00f9\u00fa\t\31\2\2\u00fa\62\3\2\2\2\u00fb"+
		"\u00fc\t\32\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\t\33\2\2\u00fe\66\3\2\2\2"+
		"\u00ff\u0100\7\61\2\2\u0100\u0101\7\61\2\2\u0101\u0105\3\2\2\2\u0102\u0104"+
		"\n\34\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2"+
		"\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109"+
		"\b\34\2\2\u01098\3\2\2\2\u010a\u010e\7}\2\2\u010b\u010d\13\2\2\2\u010c"+
		"\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010f\3\2\2\2\u010e\u010c\3\2"+
		"\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111\u0112\7\177\2\2\u0112"+
		"\u0113\3\2\2\2\u0113\u0114\b\35\2\2\u0114:\3\2\2\2\u0115\u0116\7*\2\2"+
		"\u0116\u0117\7,\2\2\u0117\u011b\3\2\2\2\u0118\u011a\13\2\2\2\u0119\u0118"+
		"\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c"+
		"\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7,\2\2\u011f\u0120\7+\2"+
		"\2\u0120\u0121\3\2\2\2\u0121\u0122\b\36\2\2\u0122<\3\2\2\2\u0123\u0124"+
		"\5\3\2\2\u0124\u0125\5\35\17\2\u0125\u0126\5\t\5\2\u0126\u0127\7\"\2\2"+
		"\u0127\u0128\5)\25\2\u0128\u0129\5\21\t\2\u0129\u012a\5\13\6\2\u012a\u012b"+
		"\5\35\17\2\u012b>\3\2\2\2\u012c\u012d\5\37\20\2\u012d\u012e\5%\23\2\u012e"+
		"\u012f\7\"\2\2\u012f\u0130\5\13\6\2\u0130\u0131\5\31\r\2\u0131\u0132\5"+
		"\'\24\2\u0132\u0133\5\13\6\2\u0133@\3\2\2\2\u0134\u0135\5\5\3\2\u0135"+
		"\u0136\5%\23\2\u0136\u0137\5\13\6\2\u0137\u0138\5\3\2\2\u0138\u0139\5"+
		"\27\f\2\u0139B\3\2\2\2\u013a\u013b\5\7\4\2\u013b\u013c\5\37\20\2\u013c"+
		"\u013d\5\35\17\2\u013d\u013e\5)\25\2\u013e\u013f\5\23\n\2\u013f\u0140"+
		"\5\35\17\2\u0140\u0141\5+\26\2\u0141\u0142\5\13\6\2\u0142D\3\2\2\2\u0143"+
		"\u0144\5\r\7\2\u0144\u0145\5\37\20\2\u0145\u0146\5%\23\2\u0146F\3\2\2"+
		"\2\u0147\u0148\5/\30\2\u0148\u0149\5\21\t\2\u0149\u014a\5\23\n\2\u014a"+
		"\u014b\5\31\r\2\u014b\u014c\5\13\6\2\u014cH\3\2\2\2\u014d\u014e\5)\25"+
		"\2\u014e\u014f\5\37\20\2\u014fJ\3\2\2\2\u0150\u0151\5\t\5\2\u0151\u0152"+
		"\5\37\20\2\u0152\u0153\5/\30\2\u0153\u0154\5\35\17\2\u0154\u0155\5)\25"+
		"\2\u0155\u0156\5\37\20\2\u0156L\3\2\2\2\u0157\u0158\5/\30\2\u0158\u0159"+
		"\5\23\n\2\u0159\u015a\5)\25\2\u015a\u015b\5\21\t\2\u015bN\3\2\2\2\u015c"+
		"\u015d\5\t\5\2\u015d\u015e\5\37\20\2\u015eP\3\2\2\2\u015f\u0160\5\23\n"+
		"\2\u0160\u0161\5\r\7\2\u0161R\3\2\2\2\u0162\u0163\5)\25\2\u0163\u0164"+
		"\5\21\t\2\u0164\u0165\5\13\6\2\u0165\u0166\5\35\17\2\u0166T\3\2\2\2\u0167"+
		"\u0168\5\13\6\2\u0168\u0169\5\31\r\2\u0169\u016a\5\'\24\2\u016a\u016b"+
		"\5\13\6\2\u016bV\3\2\2\2\u016c\u016d\5-\27\2\u016d\u016e\5\3\2\2\u016e"+
		"\u016f\5%\23\2\u016fX\3\2\2\2\u0170\u0171\5\37\20\2\u0171\u0172\5\r\7"+
		"\2\u0172Z\3\2\2\2\u0173\u0174\5\5\3\2\u0174\u0175\5\13\6\2\u0175\u0176"+
		"\5\17\b\2\u0176\u0177\5\23\n\2\u0177\u0178\5\35\17\2\u0178\\\3\2\2\2\u0179"+
		"\u017a\5\13\6\2\u017a\u017b\5\35\17\2\u017b\u017c\5\t\5\2\u017c^\3\2\2"+
		"\2\u017d\u017e\5%\23\2\u017e\u017f\5\13\6\2\u017f\u0180\5)\25\2\u0180"+
		"\u0181\5+\26\2\u0181\u0182\5%\23\2\u0182\u0183\5\35\17\2\u0183`\3\2\2"+
		"\2\u0184\u0185\5\r\7\2\u0185\u0186\5+\26\2\u0186\u0187\5\35\17\2\u0187"+
		"\u0188\5\7\4\2\u0188\u0189\5)\25\2\u0189\u018a\5\23\n\2\u018a\u018b\5"+
		"\37\20\2\u018b\u018c\5\35\17\2\u018cb\3\2\2\2\u018d\u018e\5!\21\2\u018e"+
		"\u018f\5%\23\2\u018f\u0190\5\37\20\2\u0190\u0191\5\7\4\2\u0191\u0192\5"+
		"\13\6\2\u0192\u0193\5\t\5\2\u0193\u0194\5+\26\2\u0194\u0195\5%\23\2\u0195"+
		"\u0196\5\13\6\2\u0196d\3\2\2\2\u0197\u0198\5\3\2\2\u0198\u0199\5%\23\2"+
		"\u0199\u019a\5%\23\2\u019a\u019b\5\3\2\2\u019b\u019c\5\63\32\2\u019cf"+
		"\3\2\2\2\u019d\u019e\5%\23\2\u019e\u019f\5\13\6\2\u019f\u01a0\5\3\2\2"+
		"\u01a0\u01a1\5\31\r\2\u01a1h\3\2\2\2\u01a2\u01a3\5\5\3\2\u01a3\u01a4\5"+
		"\37\20\2\u01a4\u01a5\5\37\20\2\u01a5\u01a6\5\31\r\2\u01a6\u01a7\5\13\6"+
		"\2\u01a7\u01a8\5\3\2\2\u01a8\u01a9\5\35\17\2\u01a9j\3\2\2\2\u01aa\u01ab"+
		"\5\23\n\2\u01ab\u01ac\5\35\17\2\u01ac\u01ad\5)\25\2\u01ad\u01ae\5\13\6"+
		"\2\u01ae\u01af\5\17\b\2\u01af\u01b0\5\13\6\2\u01b0\u01b1\5%\23\2\u01b1"+
		"l\3\2\2\2\u01b2\u01b3\5\'\24\2\u01b3\u01b4\5)\25\2\u01b4\u01b5\5%\23\2"+
		"\u01b5\u01b6\5\23\n\2\u01b6\u01b7\5\35\17\2\u01b7\u01b8\5\17\b\2\u01b8"+
		"n\3\2\2\2\u01b9\u01ba\5\35\17\2\u01ba\u01bb\5\37\20\2\u01bb\u01bc\5)\25"+
		"\2\u01bcp\3\2\2\2\u01bd\u01be\5\3\2\2\u01be\u01bf\5\35\17\2\u01bf\u01c0"+
		"\5\t\5\2\u01c0r\3\2\2\2\u01c1\u01c2\5\37\20\2\u01c2\u01c3\5%\23\2\u01c3"+
		"t\3\2\2\2\u01c4\u01c5\5\t\5\2\u01c5\u01c6\5\23\n\2\u01c6\u01c7\5-\27\2"+
		"\u01c7v\3\2\2\2\u01c8\u01c9\5\33\16\2\u01c9\u01ca\5\37\20\2\u01ca\u01cb"+
		"\5\t\5\2\u01cbx\3\2\2\2\u01cc\u01cd\7-\2\2\u01cdz\3\2\2\2\u01ce\u01cf"+
		"\7/\2\2\u01cf|\3\2\2\2\u01d0\u01d1\7,\2\2\u01d1~\3\2\2\2\u01d2\u01d3\7"+
		"\61\2\2\u01d3\u0080\3\2\2\2\u01d4\u01d5\7?\2\2\u01d5\u0082\3\2\2\2\u01d6"+
		"\u01d7\7>\2\2\u01d7\u01d8\7@\2\2\u01d8\u0084\3\2\2\2\u01d9\u01da\7>\2"+
		"\2\u01da\u0086\3\2\2\2\u01db\u01dc\7@\2\2\u01dc\u0088\3\2\2\2\u01dd\u01de"+
		"\7>\2\2\u01de\u01df\7?\2\2\u01df\u008a\3\2\2\2\u01e0\u01e1\7@\2\2\u01e1"+
		"\u01e2\7?\2\2\u01e2\u008c\3\2\2\2\u01e3\u01e4\7<\2\2\u01e4\u01e5\7?\2"+
		"\2\u01e5\u008e\3\2\2\2\u01e6\u01e7\7]\2\2\u01e7\u0090\3\2\2\2\u01e8\u01e9"+
		"\7_\2\2\u01e9\u0092\3\2\2\2\u01ea\u01eb\7<\2\2\u01eb\u0094\3\2\2\2\u01ec"+
		"\u01ed\7*\2\2\u01ed\u0096\3\2\2\2\u01ee\u01ef\7+\2\2\u01ef\u0098\3\2\2"+
		"\2\u01f0\u01f1\7=\2\2\u01f1\u009a\3\2\2\2\u01f2\u01f3\7\60\2\2\u01f3\u01f4"+
		"\7\60\2\2\u01f4\u009c\3\2\2\2\u01f5\u01f6\7.\2\2\u01f6\u009e\3\2\2\2\u01f7"+
		"\u01f8\t\35\2\2\u01f8\u00a0\3\2\2\2\u01f9\u01fb\5\u009fP\2\u01fa\u01f9"+
		"\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd"+
		"\u00a2\3\2\2\2\u01fe\u0200\t\6\2\2\u01ff\u0201\7/\2\2\u0200\u01ff\3\2"+
		"\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2\u0202\u0204\5\u009fP\2\u0203"+
		"\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2"+
		"\2\2\u0206\u00a4\3\2\2\2\u0207\u0209\5\u009fP\2\u0208\u0207\3\2\2\2\u0209"+
		"\u020a\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u0213\3\2"+
		"\2\2\u020c\u0210\7\60\2\2\u020d\u020f\5\u009fP\2\u020e\u020d\3\2\2\2\u020f"+
		"\u0212\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0214\3\2"+
		"\2\2\u0212\u0210\3\2\2\2\u0213\u020c\3\2\2\2\u0213\u0214\3\2\2\2\u0214"+
		"\u0216\3\2\2\2\u0215\u0217\5\u00a3R\2\u0216\u0215\3\2\2\2\u0216\u0217"+
		"\3\2\2\2\u0217\u0222\3\2\2\2\u0218\u021a\7\60\2\2\u0219\u021b\5\u009f"+
		"P\2\u021a\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021a\3\2\2\2\u021c"+
		"\u021d\3\2\2\2\u021d\u021f\3\2\2\2\u021e\u0220\5\u00a3R\2\u021f\u021e"+
		"\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u0208\3\2\2\2\u0221"+
		"\u0218\3\2\2\2\u0222\u00a6\3\2\2\2\u0223\u0226\5\u00a9U\2\u0224\u0226"+
		"\5\u00abV\2\u0225\u0223\3\2\2\2\u0225\u0224\3\2\2\2\u0226\u00a8\3\2\2"+
		"\2\u0227\u0228\5)\25\2\u0228\u0229\5%\23\2\u0229\u022a\5+\26\2\u022a\u022b"+
		"\5\13\6\2\u022b\u00aa\3\2\2\2\u022c\u022d\5\r\7\2\u022d\u022e\5\3\2\2"+
		"\u022e\u022f\5\31\r\2\u022f\u0230\5\'\24\2\u0230\u0231\5\13\6\2\u0231"+
		"\u00ac\3\2\2\2\u0232\u0233\7^\2\2\u0233\u0234\7d\2\2\u0234\u00ae\3\2\2"+
		"\2\u0235\u0236\7^\2\2\u0236\u0237\7h\2\2\u0237\u00b0\3\2\2\2\u0238\u0239"+
		"\7^\2\2\u0239\u023a\7t\2\2\u023a\u00b2\3\2\2\2\u023b\u023c\7^\2\2\u023c"+
		"\u023d\7p\2\2\u023d\u00b4\3\2\2\2\u023e\u023f\7^\2\2\u023f\u0240\7v\2"+
		"\2\u0240\u00b6\3\2\2\2\u0241\u0242\7^\2\2\u0242\u0243\7)\2\2\u0243\u00b8"+
		"\3\2\2\2\u0244\u0245\7^\2\2\u0245\u0246\7$\2\2\u0246\u00ba\3\2\2\2\u0247"+
		"\u0248\7^\2\2\u0248\u0249\7^\2\2\u0249\u00bc\3\2\2\2\u024a\u0253\5\u00ad"+
		"W\2\u024b\u0253\5\u00afX\2\u024c\u0253\5\u00b1Y\2\u024d\u0253\5\u00b3"+
		"Z\2\u024e\u0253\5\u00b5[\2\u024f\u0253\5\u00b7\\\2\u0250\u0253\5\u00b9"+
		"]\2\u0251\u0253\5\u00bb^\2\u0252\u024a\3\2\2\2\u0252\u024b\3\2\2\2\u0252"+
		"\u024c\3\2\2\2\u0252\u024d\3\2\2\2\u0252\u024e\3\2\2\2\u0252\u024f\3\2"+
		"\2\2\u0252\u0250\3\2\2\2\u0252\u0251\3\2\2\2\u0253\u00be\3\2\2\2\u0254"+
		"\u0259\7$\2\2\u0255\u0258\n\36\2\2\u0256\u0258\5\u00bd_\2\u0257\u0255"+
		"\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u025b\3\2\2\2\u0259\u0257\3\2\2\2\u0259"+
		"\u025a\3\2\2\2\u025a\u00c0\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\5\u00bf"+
		"`\2\u025d\u025e\t\37\2\2\u025e\u00c2\3\2\2\2\u025f\u0260\5\u00bf`\2\u0260"+
		"\u0261\7$\2\2\u0261\u00c4\3\2\2\2\u0262\u0266\t \2\2\u0263\u0265\t!\2"+
		"\2\u0264\u0263\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0267"+
		"\3\2\2\2\u0267\u00c6\3\2\2\2\u0268\u0266\3\2\2\2\u0269\u026b\t\"\2\2\u026a"+
		"\u0269\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2"+
		"\2\2\u026d\u026e\3\2\2\2\u026e\u026f\bd\2\2\u026f\u00c8\3\2\2\2\u0270"+
		"\u0271\13\2\2\2\u0271\u00ca\3\2\2\2\26\2\u0105\u010e\u011b\u01fc\u0200"+
		"\u0205\u020a\u0210\u0213\u0216\u021c\u021f\u0221\u0225\u0252\u0257\u0259"+
		"\u0266\u026c\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}