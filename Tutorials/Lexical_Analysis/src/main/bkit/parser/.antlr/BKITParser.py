# Generated from /media/edisc/DATA/MinhLong/MT-183/_2020/PPL/Tutorials/Lexical_Analysis/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u00bd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3\66\n\3\3\4\3\4\5\4:\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\7\5")
        buf.write("\7K\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\5\tT\n\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\7\n^\n\n\f\n\16\na\13\n\3\13\3")
        buf.write("\13\3\13\7\13f\n\13\f\13\16\13i\13\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\7\fp\n\f\f\f\16\fs\13\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r~\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\5\17\u0087\n\17\3\17\3\17\3\20\3\20\3\20\7\20\u008e")
        buf.write("\n\20\f\20\16\20\u0091\13\20\3\21\3\21\3\21\5\21\u0096")
        buf.write("\n\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\5\23\u00a0")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00a7\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00ae\n\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00b5\n\26\3\27\3\27\3\27\3\27\5\27\u00bb\n")
        buf.write("\27\3\27\2\2\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,\2\4\3\2\3\4\3\2\17\20\2\u00bc\2.\3\2\2\2\4\65")
        buf.write("\3\2\2\2\69\3\2\2\2\b;\3\2\2\2\n?\3\2\2\2\fJ\3\2\2\2\16")
        buf.write("L\3\2\2\2\20Q\3\2\2\2\22W\3\2\2\2\24b\3\2\2\2\26l\3\2")
        buf.write("\2\2\30}\3\2\2\2\32\177\3\2\2\2\34\u0083\3\2\2\2\36\u008a")
        buf.write("\3\2\2\2 \u0095\3\2\2\2\"\u0097\3\2\2\2$\u009f\3\2\2\2")
        buf.write("&\u00a6\3\2\2\2(\u00ad\3\2\2\2*\u00b4\3\2\2\2,\u00ba\3")
        buf.write("\2\2\2./\5\4\3\2/\60\7\2\2\3\60\3\3\2\2\2\61\62\5\6\4")
        buf.write("\2\62\63\5\4\3\2\63\66\3\2\2\2\64\66\5\6\4\2\65\61\3\2")
        buf.write("\2\2\65\64\3\2\2\2\66\5\3\2\2\2\67:\5\b\5\28:\5\16\b\2")
        buf.write("9\67\3\2\2\298\3\2\2\2:\7\3\2\2\2;<\5\n\6\2<=\5\f\7\2")
        buf.write("=>\7\b\2\2>\t\3\2\2\2?@\t\2\2\2@\13\3\2\2\2AF\7\21\2\2")
        buf.write("BC\7\t\2\2CE\7\21\2\2DB\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG")
        buf.write("\3\2\2\2GK\3\2\2\2HF\3\2\2\2IK\3\2\2\2JA\3\2\2\2JI\3\2")
        buf.write("\2\2K\r\3\2\2\2LM\5\n\6\2MN\7\21\2\2NO\5\20\t\2OP\5\24")
        buf.write("\13\2P\17\3\2\2\2QS\7\13\2\2RT\5\22\n\2SR\3\2\2\2ST\3")
        buf.write("\2\2\2TU\3\2\2\2UV\7\f\2\2V\21\3\2\2\2WX\5\n\6\2X_\5\f")
        buf.write("\7\2YZ\7\b\2\2Z[\5\n\6\2[\\\5\f\7\2\\^\3\2\2\2]Y\3\2\2")
        buf.write("\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\23\3\2\2\2a_\3\2\2\2")
        buf.write("bg\7\6\2\2cf\5\26\f\2df\5\30\r\2ec\3\2\2\2ed\3\2\2\2f")
        buf.write("i\3\2\2\2ge\3\2\2\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2jk\7")
        buf.write("\7\2\2k\25\3\2\2\2lq\5\b\5\2mn\7\b\2\2np\5\b\5\2om\3\2")
        buf.write("\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\27\3\2\2\2sq\3\2\2")
        buf.write("\2tu\5\32\16\2uv\7\b\2\2v~\3\2\2\2wx\5\34\17\2xy\7\b\2")
        buf.write("\2y~\3\2\2\2z{\5\"\22\2{|\7\b\2\2|~\3\2\2\2}t\3\2\2\2")
        buf.write("}w\3\2\2\2}z\3\2\2\2~\31\3\2\2\2\177\u0080\7\21\2\2\u0080")
        buf.write("\u0081\7\n\2\2\u0081\u0082\5$\23\2\u0082\33\3\2\2\2\u0083")
        buf.write("\u0084\7\21\2\2\u0084\u0086\7\13\2\2\u0085\u0087\5\36")
        buf.write("\20\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0089\7\f\2\2\u0089\35\3\2\2\2\u008a\u008f")
        buf.write("\5 \21\2\u008b\u008c\7\t\2\2\u008c\u008e\5 \21\2\u008d")
        buf.write("\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\37\3\2\2\2\u0091\u008f\3\2")
        buf.write("\2\2\u0092\u0096\7\24\2\2\u0093\u0096\7\23\2\2\u0094\u0096")
        buf.write("\5\22\n\2\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095")
        buf.write("\u0094\3\2\2\2\u0096!\3\2\2\2\u0097\u0098\7\5\2\2\u0098")
        buf.write("\u0099\5$\23\2\u0099#\3\2\2\2\u009a\u009b\5&\24\2\u009b")
        buf.write("\u009c\7\r\2\2\u009c\u009d\5$\23\2\u009d\u00a0\3\2\2\2")
        buf.write("\u009e\u00a0\5&\24\2\u009f\u009a\3\2\2\2\u009f\u009e\3")
        buf.write("\2\2\2\u00a0%\3\2\2\2\u00a1\u00a2\5(\25\2\u00a2\u00a3")
        buf.write("\7\16\2\2\u00a3\u00a4\5(\25\2\u00a4\u00a7\3\2\2\2\u00a5")
        buf.write("\u00a7\5(\25\2\u00a6\u00a1\3\2\2\2\u00a6\u00a5\3\2\2\2")
        buf.write("\u00a7\'\3\2\2\2\u00a8\u00a9\5*\26\2\u00a9\u00aa\t\3\2")
        buf.write("\2\u00aa\u00ab\5(\25\2\u00ab\u00ae\3\2\2\2\u00ac\u00ae")
        buf.write("\5*\26\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write(")\3\2\2\2\u00af\u00b0\7\13\2\2\u00b0\u00b1\5$\23\2\u00b1")
        buf.write("\u00b2\7\f\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b5\5,\27\2")
        buf.write("\u00b4\u00af\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5+\3\2\2")
        buf.write("\2\u00b6\u00bb\7\21\2\2\u00b7\u00bb\7\24\2\2\u00b8\u00bb")
        buf.write("\7\23\2\2\u00b9\u00bb\5\34\17\2\u00ba\u00b6\3\2\2\2\u00ba")
        buf.write("\u00b7\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2")
        buf.write("\u00bb-\3\2\2\2\24\659FJS_egq}\u0086\u008f\u0095\u009f")
        buf.write("\u00a6\u00ad\u00b4\u00ba")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'return'", "'{'", 
                     "'}'", "';'", "','", "'='", "'('", "')'", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "RETURN", "LB", "RB", 
                      "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", "MUL", 
                      "DIV", "ID", "LETTER", "FLOATLIT", "INTLIT", "Identifier1", 
                      "Identifier2", "REAL", "STR", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_manydecl = 1
    RULE_decl = 2
    RULE_var_decl = 3
    RULE_data_type = 4
    RULE_id_list = 5
    RULE_func_decl = 6
    RULE_param_decl = 7
    RULE_param_list = 8
    RULE_body = 9
    RULE_var_decl_list = 10
    RULE_statement = 11
    RULE_assign_stmt = 12
    RULE_call_stmt = 13
    RULE_call_param = 14
    RULE_one_param = 15
    RULE_ret_stmt = 16
    RULE_exp = 17
    RULE_exp1 = 18
    RULE_exp2 = 19
    RULE_exp3 = 20
    RULE_operands = 21

    ruleNames =  [ "program", "manydecl", "decl", "var_decl", "data_type", 
                   "id_list", "func_decl", "param_decl", "param_list", "body", 
                   "var_decl_list", "statement", "assign_stmt", "call_stmt", 
                   "call_param", "one_param", "ret_stmt", "exp", "exp1", 
                   "exp2", "exp3", "operands" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    RETURN=3
    LB=4
    RB=5
    SM=6
    CM=7
    EQ=8
    LP=9
    RP=10
    ADD=11
    SUB=12
    MUL=13
    DIV=14
    ID=15
    LETTER=16
    FLOATLIT=17
    INTLIT=18
    Identifier1=19
    Identifier2=20
    REAL=21
    STR=22
    WS=23
    ERROR_CHAR=24
    UNCLOSE_STRING=25
    ILLEGAL_ESCAPE=26
    UNTERMINATED_COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def manydecl(self):
            return self.getTypedRuleContext(BKITParser.ManydeclContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.manydecl()
            self.state = 45
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKITParser.DeclContext,0)


        def manydecl(self):
            return self.getTypedRuleContext(BKITParser.ManydeclContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_manydecl




    def manydecl(self):

        localctx = BKITParser.ManydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydecl)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.decl()
                self.state = 48
                self.manydecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(BKITParser.Var_declContext,0)


        def func_decl(self):
            return self.getTypedRuleContext(BKITParser.Func_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_decl




    def decl(self):

        localctx = BKITParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.func_decl()
                pass


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

        def data_type(self):
            return self.getTypedRuleContext(BKITParser.Data_typeContext,0)


        def id_list(self):
            return self.getTypedRuleContext(BKITParser.Id_listContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.data_type()
            self.state = 58
            self.id_list()
            self.state = 59
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_data_type




    def data_type(self):

        localctx = BKITParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
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


    class Id_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_id_list




    def id_list(self):

        localctx = BKITParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_list)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(BKITParser.ID)
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 64
                        self.match(BKITParser.CM)
                        self.state = 65
                        self.match(BKITParser.ID) 
                    self.state = 70
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass
            elif token in [BKITParser.SM, BKITParser.CM, BKITParser.RP]:
                self.enterOuterAlt(localctx, 2)

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


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_type(self):
            return self.getTypedRuleContext(BKITParser.Data_typeContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def param_decl(self):
            return self.getTypedRuleContext(BKITParser.Param_declContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.data_type()
            self.state = 75
            self.match(BKITParser.ID)
            self.state = 76
            self.param_decl()
            self.state = 77
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_param_decl




    def param_decl(self):

        localctx = BKITParser.Param_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(BKITParser.LP)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 80
                self.param_list()


            self.state = 83
            self.match(BKITParser.RP)
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

        def data_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Data_typeContext)
            else:
                return self.getTypedRuleContext(BKITParser.Data_typeContext,i)


        def id_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Id_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Id_listContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SM)
            else:
                return self.getToken(BKITParser.SM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.data_type()
            self.state = 86
            self.id_list()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SM:
                self.state = 87
                self.match(BKITParser.SM)

                self.state = 88
                self.data_type()
                self.state = 89
                self.id_list()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def var_decl_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decl_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decl_listContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StatementContext)
            else:
                return self.getTypedRuleContext(BKITParser.StatementContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(BKITParser.LB)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.RETURN) | (1 << BKITParser.ID))) != 0):
                self.state = 99
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT, BKITParser.FLOAT]:
                    self.state = 97
                    self.var_decl_list()
                    pass
                elif token in [BKITParser.RETURN, BKITParser.ID]:
                    self.state = 98
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decl_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SM)
            else:
                return self.getToken(BKITParser.SM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_decl_list




    def var_decl_list(self):

        localctx = BKITParser.Var_decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.var_decl()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SM:
                self.state = 107
                self.match(BKITParser.SM)
                self.state = 108
                self.var_decl()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def ret_stmt(self):
            return self.getTypedRuleContext(BKITParser.Ret_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_statement




    def statement(self):

        localctx = BKITParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.assign_stmt()
                self.state = 115
                self.match(BKITParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.call_stmt()
                self.state = 118
                self.match(BKITParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.ret_stmt()
                self.state = 121
                self.match(BKITParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKITParser.ID)
            self.state = 126
            self.match(BKITParser.EQ)
            self.state = 127
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def call_param(self):
            return self.getTypedRuleContext(BKITParser.Call_paramContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.ID)
            self.state = 130
            self.match(BKITParser.LP)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.INTLIT))) != 0):
                self.state = 131
                self.call_param()


            self.state = 134
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.One_paramContext)
            else:
                return self.getTypedRuleContext(BKITParser.One_paramContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_call_param




    def call_param(self):

        localctx = BKITParser.Call_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.one_param()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 137
                self.match(BKITParser.CM)
                self.state = 138
                self.one_param()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_one_param




    def one_param(self):

        localctx = BKITParser.One_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_one_param)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(BKITParser.INTLIT)
                pass
            elif token in [BKITParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.match(BKITParser.FLOATLIT)
                pass
            elif token in [BKITParser.INT, BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.param_list()
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


    class Ret_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ret_stmt




    def ret_stmt(self):

        localctx = BKITParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ret_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKITParser.RETURN)
            self.state = 150
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.exp1()
                self.state = 153
                self.match(BKITParser.ADD)
                self.state = 154
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.exp1()
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

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp2Context,i)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1




    def exp1(self):

        localctx = BKITParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp1)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.exp2()
                self.state = 160
                self.match(BKITParser.SUB)
                self.state = 161
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.exp2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2




    def exp2(self):

        localctx = BKITParser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp2)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.exp3()
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==BKITParser.MUL or _la==BKITParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.exp2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.exp3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3




    def exp3(self):

        localctx = BKITParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp3)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(BKITParser.LP)
                self.state = 174
                self.exp()
                self.state = 175
                self.match(BKITParser.RP)
                pass
            elif token in [BKITParser.ID, BKITParser.FLOATLIT, BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.operands()
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


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operands




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_operands)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.call_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





