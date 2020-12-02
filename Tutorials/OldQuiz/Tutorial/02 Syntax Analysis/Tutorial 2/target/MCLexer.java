// Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1

    package mc.parser;

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, COMMENT=2, INT=3, VOID=4, FLOAT=5, BOOLEAN=6, BREAK=7, CONTINUE=8, 
		ELSE=9, FOR=10, IF=11, RETURN=12, DO=13, WHILE=14, STRING=15, ADDOP=16, 
		MULOP=17, LOGNOT=18, LOGOR=19, NOTEQ=20, LST=21, LTE=22, ASG=23, SUBOP=24, 
		DIVOP=25, MOD=26, LOGAND=27, EQ=28, GRT=29, GTE=30, LB=31, RB=32, LP=33, 
		RP=34, LS=35, RS=36, SEMI=37, CM=38, INTLIT=39, BOOLEANLIT=40, FLOATLIT=41, 
		ILLEGAL_ESCAPE=42, UNCLOSE_STRING=43, STRINGLIT=44, ID=45, ERROR_CHAR=46;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"WS", "COMMENT", "INT", "VOID", "FLOAT", "BOOLEAN", "BREAK", "CONTINUE", 
		"ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", "FALSE", "STRING", 
		"ADDOP", "MULOP", "LOGNOT", "LOGOR", "NOTEQ", "LST", "LTE", "ASG", "SUBOP", 
		"DIVOP", "MOD", "LOGAND", "EQ", "GRT", "GTE", "LB", "RB", "LP", "RP", 
		"LS", "RS", "SEMI", "CM", "INTLIT", "BOOLEANLIT", "FLOATLIT", "FLPOINT", 
		"EXP", "BSP", "FF", "CR", "NEWLINE", "TAB", "SQUOTE", "DQUOTE", "BSL", 
		"LEGAL_ESCAPE", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "STRINGLIT", "ID", 
		"ERROR_CHAR"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, "'int'", "'void'", "'float'", "'boolean'", "'break'", 
		"'continue'", "'else'", "'for'", "'if'", "'return'", "'do'", "'while'", 
		"'string'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", 
		"'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'('", "')'", "'{'", 
		"'}'", "'['", "']'", "';'", "','"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "WS", "COMMENT", "INT", "VOID", "FLOAT", "BOOLEAN", "BREAK", "CONTINUE", 
		"ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "STRING", "ADDOP", "MULOP", 
		"LOGNOT", "LOGOR", "NOTEQ", "LST", "LTE", "ASG", "SUBOP", "DIVOP", "MOD", 
		"LOGAND", "EQ", "GRT", "GTE", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", 
		"CM", "INTLIT", "BOOLEANLIT", "FLOATLIT", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
		"STRINGLIT", "ID", "ERROR_CHAR"
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


	@Override
	public Token emit() {
	    switch (getType()) {
	    case UNCLOSE_STRING:       
	        Token result = super.emit();
	        // you'll need to define this method
	        throw new UncloseString(result.getText());
	        
	    case ILLEGAL_ESCAPE:
	        result = super.emit();
	        throw new IllegalEscape(result.getText());

	    case ERROR_CHAR:
	        result = super.emit();
	        throw new ErrorToken(result.getText()); 

	    default:
	        return super.emit();
	    }
	}


	public MCLexer(CharStream input) {
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

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 54:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 55:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 56:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

			    setText(getText().substring(1, getText().length()));

			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:

			    setText(getText().substring(1, getText().length()));

			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:

			    setText(getText().substring(1, getText().length()-1));

			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60\u0191\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\3\2"+
		"\6\2{\n\2\r\2\16\2|\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u0085\n\3\f\3\16\3\u0088"+
		"\13\3\3\3\3\3\3\3\3\3\7\3\u008e\n\3\f\3\16\3\u0091\13\3\3\3\3\3\5\3\u0095"+
		"\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26"+
		"\3\26\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34"+
		"\3\34\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3"+
		"#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\6*\u0122\n*\r*\16*\u0123"+
		"\3+\3+\5+\u0128\n+\3,\7,\u012b\n,\f,\16,\u012e\13,\3,\3,\3,\3,\3,\3,\7"+
		",\u0136\n,\f,\16,\u0139\13,\5,\u013b\n,\3,\5,\u013e\n,\3,\3,\3,\5,\u0143"+
		"\n,\3-\3-\3.\3.\5.\u0149\n.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3"+
		"\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3"+
		"\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u016d\n\67\38\3"+
		"8\38\78\u0172\n8\f8\168\u0175\138\38\38\38\38\39\39\39\79\u017e\n9\f9"+
		"\169\u0181\139\39\39\3:\3:\3:\3:\3;\3;\7;\u018b\n;\f;\16;\u018e\13;\3"+
		"<\3<\4\u008f\u0173\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27"+
		"\r\31\16\33\17\35\20\37\2!\2#\21%\22\'\23)\24+\25-\26/\27\61\30\63\31"+
		"\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y\2[\2]\2_\2a\2"+
		"c\2e\2g\2i\2k\2m\2o,q-s.u/w\60\3\2\n\5\2\n\f\16\17\"\"\4\2\f\f\17\17\3"+
		"\2\62;\4\2GGgg\6\2\f\f\17\17$$^^\n\2$$))^^ddhhppttvv\5\2C\\aac|\6\2\62"+
		";C\\aac|\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2#\3\2\2\2\2%\3"+
		"\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3"+
		"\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2"+
		"=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3"+
		"\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2"+
		"\2\2W\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\3"+
		"z\3\2\2\2\5\u0094\3\2\2\2\7\u0098\3\2\2\2\t\u009c\3\2\2\2\13\u00a1\3\2"+
		"\2\2\r\u00a7\3\2\2\2\17\u00af\3\2\2\2\21\u00b5\3\2\2\2\23\u00be\3\2\2"+
		"\2\25\u00c3\3\2\2\2\27\u00c7\3\2\2\2\31\u00ca\3\2\2\2\33\u00d1\3\2\2\2"+
		"\35\u00d4\3\2\2\2\37\u00da\3\2\2\2!\u00df\3\2\2\2#\u00e5\3\2\2\2%\u00ec"+
		"\3\2\2\2\'\u00ee\3\2\2\2)\u00f0\3\2\2\2+\u00f2\3\2\2\2-\u00f5\3\2\2\2"+
		"/\u00f8\3\2\2\2\61\u00fa\3\2\2\2\63\u00fd\3\2\2\2\65\u00ff\3\2\2\2\67"+
		"\u0101\3\2\2\29\u0103\3\2\2\2;\u0105\3\2\2\2=\u0108\3\2\2\2?\u010b\3\2"+
		"\2\2A\u010d\3\2\2\2C\u0110\3\2\2\2E\u0112\3\2\2\2G\u0114\3\2\2\2I\u0116"+
		"\3\2\2\2K\u0118\3\2\2\2M\u011a\3\2\2\2O\u011c\3\2\2\2Q\u011e\3\2\2\2S"+
		"\u0121\3\2\2\2U\u0127\3\2\2\2W\u0142\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2"+
		"\2\2]\u014c\3\2\2\2_\u014f\3\2\2\2a\u0152\3\2\2\2c\u0155\3\2\2\2e\u0158"+
		"\3\2\2\2g\u015b\3\2\2\2i\u015e\3\2\2\2k\u0161\3\2\2\2m\u016c\3\2\2\2o"+
		"\u016e\3\2\2\2q\u017a\3\2\2\2s\u0184\3\2\2\2u\u0188\3\2\2\2w\u018f\3\2"+
		"\2\2y{\t\2\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177"+
		"\b\2\2\2\177\4\3\2\2\2\u0080\u0081\7\61\2\2\u0081\u0082\7\61\2\2\u0082"+
		"\u0086\3\2\2\2\u0083\u0085\n\3\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2"+
		"\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0095\3\2\2\2\u0088"+
		"\u0086\3\2\2\2\u0089\u008a\7\61\2\2\u008a\u008b\7,\2\2\u008b\u008f\3\2"+
		"\2\2\u008c\u008e\13\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f"+
		"\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3\2"+
		"\2\2\u0092\u0093\7,\2\2\u0093\u0095\7\61\2\2\u0094\u0080\3\2\2\2\u0094"+
		"\u0089\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\b\3\2\2\u0097\6\3\2\2\2"+
		"\u0098\u0099\7k\2\2\u0099\u009a\7p\2\2\u009a\u009b\7v\2\2\u009b\b\3\2"+
		"\2\2\u009c\u009d\7x\2\2\u009d\u009e\7q\2\2\u009e\u009f\7k\2\2\u009f\u00a0"+
		"\7f\2\2\u00a0\n\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4"+
		"\7q\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7v\2\2\u00a6\f\3\2\2\2\u00a7\u00a8"+
		"\7d\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7n\2\2\u00ab"+
		"\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7p\2\2\u00ae\16\3\2\2\2\u00af"+
		"\u00b0\7d\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3\7c\2\2"+
		"\u00b3\u00b4\7m\2\2\u00b4\20\3\2\2\2\u00b5\u00b6\7e\2\2\u00b6\u00b7\7"+
		"q\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb"+
		"\7p\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7g\2\2\u00bd\22\3\2\2\2\u00be\u00bf"+
		"\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2"+
		"\24\3\2\2\2\u00c3\u00c4\7h\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7t\2\2\u00c6"+
		"\26\3\2\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9\30\3\2\2\2\u00ca"+
		"\u00cb\7t\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7w\2\2"+
		"\u00ce\u00cf\7t\2\2\u00cf\u00d0\7p\2\2\u00d0\32\3\2\2\2\u00d1\u00d2\7"+
		"f\2\2\u00d2\u00d3\7q\2\2\u00d3\34\3\2\2\2\u00d4\u00d5\7y\2\2\u00d5\u00d6"+
		"\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7g\2\2\u00d9"+
		"\36\3\2\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7w\2\2\u00dd"+
		"\u00de\7g\2\2\u00de \3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7c\2\2\u00e1"+
		"\u00e2\7n\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4\7g\2\2\u00e4\"\3\2\2\2\u00e5"+
		"\u00e6\7u\2\2\u00e6\u00e7\7v\2\2\u00e7\u00e8\7t\2\2\u00e8\u00e9\7k\2\2"+
		"\u00e9\u00ea\7p\2\2\u00ea\u00eb\7i\2\2\u00eb$\3\2\2\2\u00ec\u00ed\7-\2"+
		"\2\u00ed&\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef(\3\2\2\2\u00f0\u00f1\7#\2\2"+
		"\u00f1*\3\2\2\2\u00f2\u00f3\7~\2\2\u00f3\u00f4\7~\2\2\u00f4,\3\2\2\2\u00f5"+
		"\u00f6\7#\2\2\u00f6\u00f7\7?\2\2\u00f7.\3\2\2\2\u00f8\u00f9\7>\2\2\u00f9"+
		"\60\3\2\2\2\u00fa\u00fb\7>\2\2\u00fb\u00fc\7?\2\2\u00fc\62\3\2\2\2\u00fd"+
		"\u00fe\7?\2\2\u00fe\64\3\2\2\2\u00ff\u0100\7/\2\2\u0100\66\3\2\2\2\u0101"+
		"\u0102\7\61\2\2\u01028\3\2\2\2\u0103\u0104\7\'\2\2\u0104:\3\2\2\2\u0105"+
		"\u0106\7(\2\2\u0106\u0107\7(\2\2\u0107<\3\2\2\2\u0108\u0109\7?\2\2\u0109"+
		"\u010a\7?\2\2\u010a>\3\2\2\2\u010b\u010c\7@\2\2\u010c@\3\2\2\2\u010d\u010e"+
		"\7@\2\2\u010e\u010f\7?\2\2\u010fB\3\2\2\2\u0110\u0111\7*\2\2\u0111D\3"+
		"\2\2\2\u0112\u0113\7+\2\2\u0113F\3\2\2\2\u0114\u0115\7}\2\2\u0115H\3\2"+
		"\2\2\u0116\u0117\7\177\2\2\u0117J\3\2\2\2\u0118\u0119\7]\2\2\u0119L\3"+
		"\2\2\2\u011a\u011b\7_\2\2\u011bN\3\2\2\2\u011c\u011d\7=\2\2\u011dP\3\2"+
		"\2\2\u011e\u011f\7.\2\2\u011fR\3\2\2\2\u0120\u0122\t\4\2\2\u0121\u0120"+
		"\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124"+
		"T\3\2\2\2\u0125\u0128\5\37\20\2\u0126\u0128\5!\21\2\u0127\u0125\3\2\2"+
		"\2\u0127\u0126\3\2\2\2\u0128V\3\2\2\2\u0129\u012b\t\4\2\2\u012a\u0129"+
		"\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d"+
		"\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\5Y-\2\u0130\u0131\5S*\2"+
		"\u0131\u013b\3\2\2\2\u0132\u0133\5S*\2\u0133\u0137\5Y-\2\u0134\u0136\t"+
		"\4\2\2\u0135\u0134\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137"+
		"\u0138\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u012c\3\2"+
		"\2\2\u013a\u0132\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u013e\5[.\2\u013d\u013c"+
		"\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u0143\3\2\2\2\u013f\u0140\5S*\2\u0140"+
		"\u0141\5[.\2\u0141\u0143\3\2\2\2\u0142\u013a\3\2\2\2\u0142\u013f\3\2\2"+
		"\2\u0143X\3\2\2\2\u0144\u0145\7\60\2\2\u0145Z\3\2\2\2\u0146\u0148\t\5"+
		"\2\2\u0147\u0149\7/\2\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149"+
		"\u014a\3\2\2\2\u014a\u014b\5S*\2\u014b\\\3\2\2\2\u014c\u014d\7^\2\2\u014d"+
		"\u014e\7d\2\2\u014e^\3\2\2\2\u014f\u0150\7^\2\2\u0150\u0151\7h\2\2\u0151"+
		"`\3\2\2\2\u0152\u0153\7^\2\2\u0153\u0154\7t\2\2\u0154b\3\2\2\2\u0155\u0156"+
		"\7^\2\2\u0156\u0157\7p\2\2\u0157d\3\2\2\2\u0158\u0159\7^\2\2\u0159\u015a"+
		"\7v\2\2\u015af\3\2\2\2\u015b\u015c\7^\2\2\u015c\u015d\7)\2\2\u015dh\3"+
		"\2\2\2\u015e\u015f\7^\2\2\u015f\u0160\7$\2\2\u0160j\3\2\2\2\u0161\u0162"+
		"\7^\2\2\u0162\u0163\7^\2\2\u0163l\3\2\2\2\u0164\u016d\5]/\2\u0165\u016d"+
		"\5_\60\2\u0166\u016d\5a\61\2\u0167\u016d\5c\62\2\u0168\u016d\5e\63\2\u0169"+
		"\u016d\5g\64\2\u016a\u016d\5i\65\2\u016b\u016d\5k\66\2\u016c\u0164\3\2"+
		"\2\2\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c"+
		"\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2"+
		"\2\2\u016dn\3\2\2\2\u016e\u0173\7$\2\2\u016f\u0172\n\6\2\2\u0170\u0172"+
		"\5m\67\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173"+
		"\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0176\3\2\2\2\u0175\u0173\3\2"+
		"\2\2\u0176\u0177\7^\2\2\u0177\u0178\n\7\2\2\u0178\u0179\b8\3\2\u0179p"+
		"\3\2\2\2\u017a\u017f\7$\2\2\u017b\u017e\n\6\2\2\u017c\u017e\5m\67\2\u017d"+
		"\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2"+
		"\2\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182"+
		"\u0183\b9\4\2\u0183r\3\2\2\2\u0184\u0185\5q9\2\u0185\u0186\7$\2\2\u0186"+
		"\u0187\b:\5\2\u0187t\3\2\2\2\u0188\u018c\t\b\2\2\u0189\u018b\t\t\2\2\u018a"+
		"\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2"+
		"\2\2\u018dv\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\13\2\2\2\u0190x\3"+
		"\2\2\2\25\2|\u0086\u008f\u0094\u0123\u0127\u012c\u0137\u013a\u013d\u0142"+
		"\u0148\u016c\u0171\u0173\u017d\u017f\u018c\6\b\2\2\38\2\39\3\3:\4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}