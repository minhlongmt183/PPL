# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\5\4\31\n\4\3\5\3")
        buf.write("\5\3\6\6\6\36\n\6\r\6\16\6\37\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\5\b)\n\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2")
        buf.write("\4\5\2(\2\20\3\2\2\2\4\23\3\2\2\2\6\30\3\2\2\2\b\32\3")
        buf.write("\2\2\2\n\35\3\2\2\2\f!\3\2\2\2\16(\3\2\2\2\20\21\5\6\4")
        buf.write("\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\5\b\5\2\24\25\5\n")
        buf.write("\6\2\25\5\3\2\2\2\26\31\5\b\5\2\27\31\5\4\3\2\30\26\3")
        buf.write("\2\2\2\30\27\3\2\2\2\31\7\3\2\2\2\32\33\t\2\2\2\33\t\3")
        buf.write("\2\2\2\34\36\5\f\7\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35")
        buf.write("\3\2\2\2\37 \3\2\2\2 \13\3\2\2\2!\"\7\6\2\2\"#\5\16\b")
        buf.write("\2#$\7\t\2\2$%\5\16\b\2%&\7\7\2\2&\r\3\2\2\2\')\7\b\2")
        buf.write("\2(\'\3\2\2\2()\3\2\2\2)*\3\2\2\2*+\7\3\2\2+\17\3\2\2")
        buf.write("\2\5\30\37(")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'integer'", "'real'", "'['", 
                     "']'", "'-'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "INTTYPE", "FLOATTYPE", "LSB", 
                      "RSB", "SIGN", "DOTDOT", "COMMA", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_arraytype = 1
    RULE_mptype = 2
    RULE_primtype = 3
    RULE_dimens = 4
    RULE_dimen = 5
    RULE_num = 6

    ruleNames =  [ "program", "arraytype", "mptype", "primtype", "dimens", 
                   "dimen", "num" ]

    EOF = Token.EOF
    INTLIT=1
    INTTYPE=2
    FLOATTYPE=3
    LSB=4
    RSB=5
    SIGN=6
    DOTDOT=7
    COMMA=8
    WS=9
    ERROR_CHAR=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MPParser.MptypeContext,0)


        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mptype()
            self.state = 15
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArraytypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def dimens(self):
            return self.getTypedRuleContext(MPParser.DimensContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MPParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.primtype()
            self.state = 18
            self.dimens()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primtype(self):
            return self.getTypedRuleContext(MPParser.PrimtypeContext,0)


        def arraytype(self):
            return self.getTypedRuleContext(MPParser.ArraytypeContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mptype)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.primtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.arraytype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MPParser.FLOATTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_primtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimtype" ):
                return visitor.visitPrimtype(self)
            else:
                return visitor.visitChildren(self)




    def primtype(self):

        localctx = MPParser.PrimtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            _la = self._input.LA(1)
            if not(_la==MPParser.INTTYPE or _la==MPParser.FLOATTYPE):
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

    class DimensContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimen(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.DimenContext)
            else:
                return self.getTypedRuleContext(MPParser.DimenContext,i)


        def getRuleIndex(self):
            return MPParser.RULE_dimens

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimens" ):
                return visitor.visitDimens(self)
            else:
                return visitor.visitChildren(self)




    def dimens(self):

        localctx = MPParser.DimensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.dimen()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MPParser.LSB):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DimenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MPParser.LSB, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.NumContext)
            else:
                return self.getTypedRuleContext(MPParser.NumContext,i)


        def DOTDOT(self):
            return self.getToken(MPParser.DOTDOT, 0)

        def RSB(self):
            return self.getToken(MPParser.RSB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_dimen

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimen" ):
                return visitor.visitDimen(self)
            else:
                return visitor.visitChildren(self)




    def dimen(self):

        localctx = MPParser.DimenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimen)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(MPParser.LSB)
            self.state = 32
            self.num()
            self.state = 33
            self.match(MPParser.DOTDOT)
            self.state = 34
            self.num()
            self.state = 35
            self.match(MPParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def SIGN(self):
            return self.getToken(MPParser.SIGN, 0)

        def getRuleIndex(self):
            return MPParser.RULE_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = MPParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_num)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.SIGN:
                self.state = 37
                self.match(MPParser.SIGN)


            self.state = 40
            self.match(MPParser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





