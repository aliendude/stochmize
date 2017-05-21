# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .StochmizeListener import StochmizeListener
else:
    from StochmizeListener import StochmizeListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"!\u00a3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\6\2+\n\2\r\2\16\2,\3\2\3\2\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\3\4\3\4\6\4B\n\4\r\4\16\4C\3\5\3\5\3\5\5\5I\n\5")
        buf.write(u"\3\6\3\6\3\6\3\7\3\7\3\7\5\7Q\n\7\3\b\3\b\3\b\5\bV\n")
        buf.write(u"\b\3\b\3\b\3\b\5\b[\n\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\6\r\177\n\r\r\r\16\r\u0080\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\6\16\u0089\n\16\r\16\16\16\u008a\3\17")
        buf.write(u"\3\17\3\20\3\20\3\20\3\20\7\20\u0093\n\20\f\20\16\20")
        buf.write(u"\u0096\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write(u"\u009f\n\21\3\22\3\22\3\22\2\2\23\2\4\6\b\n\f\16\20\22")
        buf.write(u"\24\26\30\32\34\36 \"\2\5\3\2\30\31\3\2\37 \3\2\32\36")
        buf.write(u"\u009d\2*\3\2\2\2\4\60\3\2\2\2\6A\3\2\2\2\bH\3\2\2\2")
        buf.write(u"\nJ\3\2\2\2\fM\3\2\2\2\16R\3\2\2\2\20_\3\2\2\2\22d\3")
        buf.write(u"\2\2\2\24i\3\2\2\2\26q\3\2\2\2\30~\3\2\2\2\32\u0088\3")
        buf.write(u"\2\2\2\34\u008c\3\2\2\2\36\u008e\3\2\2\2 \u009e\3\2\2")
        buf.write(u"\2\"\u00a0\3\2\2\2$%\7\22\2\2%&\7\37\2\2&\'\7\3\2\2\'")
        buf.write(u"(\5\4\3\2()\7\4\2\2)+\3\2\2\2*$\3\2\2\2+,\3\2\2\2,*\3")
        buf.write(u"\2\2\2,-\3\2\2\2-.\3\2\2\2./\7\2\2\3/\3\3\2\2\2\60\61")
        buf.write(u"\7\23\2\2\61\62\7\3\2\2\62\63\5\6\4\2\63\64\7\4\2\2\64")
        buf.write(u"\65\7\24\2\2\65\66\7\3\2\2\66\67\5\30\r\2\678\7\4\2\2")
        buf.write(u"89\7\25\2\29:\7\3\2\2:;\5\32\16\2;<\7\4\2\2<\5\3\2\2")
        buf.write(u"\2=>\7\37\2\2>?\5\b\5\2?@\7\5\2\2@B\3\2\2\2A=\3\2\2\2")
        buf.write(u"BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\7\3\2\2\2EI\5\n\6\2F")
        buf.write(u"I\5\16\b\2GI\5\f\7\2HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\t")
        buf.write(u"\3\2\2\2JK\7\6\2\2KL\7 \2\2L\13\3\2\2\2MP\7\7\2\2NQ\5")
        buf.write(u"\20\t\2OQ\5\22\n\2PN\3\2\2\2PO\3\2\2\2Q\r\3\2\2\2RS\7")
        buf.write(u"\b\2\2SU\7\t\2\2TV\7\33\2\2UT\3\2\2\2UV\3\2\2\2VW\3\2")
        buf.write(u"\2\2WX\7 \2\2XZ\7\n\2\2Y[\7\33\2\2ZY\3\2\2\2Z[\3\2\2")
        buf.write(u"\2[\\\3\2\2\2\\]\7 \2\2]^\7\13\2\2^\17\3\2\2\2_`\7\26")
        buf.write(u"\2\2`a\7\t\2\2ab\5\24\13\2bc\7\13\2\2c\21\3\2\2\2de\7")
        buf.write(u"\27\2\2ef\7\t\2\2fg\5\26\f\2gh\7\13\2\2h\23\3\2\2\2i")
        buf.write(u"j\7\f\2\2jk\7\6\2\2kl\7 \2\2lm\7\n\2\2mn\7\r\2\2no\7")
        buf.write(u"\6\2\2op\7 \2\2p\25\3\2\2\2qr\7\16\2\2rs\7\6\2\2st\7")
        buf.write(u" \2\2tu\7\n\2\2uv\7\17\2\2vw\7\6\2\2wx\7 \2\2x\27\3\2")
        buf.write(u"\2\2yz\5\36\20\2z{\7!\2\2{|\7 \2\2|}\7\5\2\2}\177\3\2")
        buf.write(u"\2\2~y\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write(u"\u0081\3\2\2\2\u0081\31\3\2\2\2\u0082\u0083\5\34\17\2")
        buf.write(u"\u0083\u0084\7\37\2\2\u0084\u0085\7\6\2\2\u0085\u0086")
        buf.write(u"\5\36\20\2\u0086\u0087\7\5\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write(u"\u0082\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u0088\3\2\2")
        buf.write(u"\2\u008a\u008b\3\2\2\2\u008b\33\3\2\2\2\u008c\u008d\t")
        buf.write(u"\2\2\2\u008d\35\3\2\2\2\u008e\u0094\5 \21\2\u008f\u0090")
        buf.write(u"\5\"\22\2\u0090\u0091\5 \21\2\u0091\u0093\3\2\2\2\u0092")
        buf.write(u"\u008f\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0092\3\2\2")
        buf.write(u"\2\u0094\u0095\3\2\2\2\u0095\37\3\2\2\2\u0096\u0094\3")
        buf.write(u"\2\2\2\u0097\u009f\t\3\2\2\u0098\u0099\7\t\2\2\u0099")
        buf.write(u"\u009a\5\36\20\2\u009a\u009b\7\13\2\2\u009b\u009f\3\2")
        buf.write(u"\2\2\u009c\u009d\7\33\2\2\u009d\u009f\5 \21\2\u009e\u0097")
        buf.write(u"\3\2\2\2\u009e\u0098\3\2\2\2\u009e\u009c\3\2\2\2\u009f")
        buf.write(u"!\3\2\2\2\u00a0\u00a1\t\4\2\2\u00a1#\3\2\2\2\f,CHPUZ")
        buf.write(u"\u0080\u008a\u0094\u009e")
        return buf.getvalue()


class StochmizeParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"';'", u"'='", u"'~'", 
                     u"':'", u"'('", u"','", u"')'", u"'m'", u"'v'", u"'a'", 
                     u"'b'", u"<INVALID>", u"<INVALID>", u"'model'", u"'vars'", 
                     u"'subjto'", u"'objectives'", u"'Normal'", u"'Unif'", 
                     u"'max'", u"'min'", u"'+'", u"'-'", u"'**'", u"'*'", 
                     u"'/'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"WHITESPACE", u"NEWLINE", 
                      u"MODEL", u"VARS_DEF", u"SUBJTO", u"OBJECTIVES", u"NORMAL", 
                      u"UNIF", u"MAX", u"MIN", u"PLUS", u"MINUS", u"POW", 
                      u"PROD", u"DIV", u"ID", u"NUMBER", u"SUBJTO_DEF" ]

    RULE_program = 0
    RULE_model = 1
    RULE_vars_def = 2
    RULE_fixed_range_random = 3
    RULE_fixed = 4
    RULE_random = 5
    RULE_rang = 6
    RULE_normal = 7
    RULE_unif = 8
    RULE_normal_params = 9
    RULE_unif_params = 10
    RULE_subjto = 11
    RULE_objectives = 12
    RULE_min_max = 13
    RULE_expr = 14
    RULE_expr_content = 15
    RULE_operators = 16

    ruleNames =  [ u"program", u"model", u"vars_def", u"fixed_range_random", 
                   u"fixed", u"random", u"rang", u"normal", u"unif", u"normal_params", 
                   u"unif_params", u"subjto", u"objectives", u"min_max", 
                   u"expr", u"expr_content", u"operators" ]

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
    WHITESPACE=14
    NEWLINE=15
    MODEL=16
    VARS_DEF=17
    SUBJTO=18
    OBJECTIVES=19
    NORMAL=20
    UNIF=21
    MAX=22
    MIN=23
    PLUS=24
    MINUS=25
    POW=26
    PROD=27
    DIV=28
    ID=29
    NUMBER=30
    SUBJTO_DEF=31

    def __init__(self, input):
        super(StochmizeParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.ProgramContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(StochmizeParser.EOF, 0)

        def MODEL(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.MODEL)
            else:
                return self.getToken(StochmizeParser.MODEL, i)

        def ID(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.ID)
            else:
                return self.getToken(StochmizeParser.ID, i)

        def model(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.ModelContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.ModelContext,i)


        def getRuleIndex(self):
            return StochmizeParser.RULE_program

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterProgram(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitProgram(self)




    def program(self):

        localctx = StochmizeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.match(StochmizeParser.MODEL)
                self.state = 35
                self.match(StochmizeParser.ID)
                self.state = 36
                self.match(StochmizeParser.T__0)
                self.state = 37
                self.model()
                self.state = 38
                self.match(StochmizeParser.T__1)
                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StochmizeParser.MODEL):
                    break

            self.state = 44
            self.match(StochmizeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.ModelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VARS_DEF(self):
            return self.getToken(StochmizeParser.VARS_DEF, 0)

        def vars_def(self):
            return self.getTypedRuleContext(StochmizeParser.Vars_defContext,0)


        def SUBJTO(self):
            return self.getToken(StochmizeParser.SUBJTO, 0)

        def subjto(self):
            return self.getTypedRuleContext(StochmizeParser.SubjtoContext,0)


        def OBJECTIVES(self):
            return self.getToken(StochmizeParser.OBJECTIVES, 0)

        def objectives(self):
            return self.getTypedRuleContext(StochmizeParser.ObjectivesContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_model

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterModel(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitModel(self)




    def model(self):

        localctx = StochmizeParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(StochmizeParser.VARS_DEF)
            self.state = 47
            self.match(StochmizeParser.T__0)
            self.state = 48
            self.vars_def()
            self.state = 49
            self.match(StochmizeParser.T__1)
            self.state = 50
            self.match(StochmizeParser.SUBJTO)
            self.state = 51
            self.match(StochmizeParser.T__0)
            self.state = 52
            self.subjto()
            self.state = 53
            self.match(StochmizeParser.T__1)
            self.state = 54
            self.match(StochmizeParser.OBJECTIVES)
            self.state = 55
            self.match(StochmizeParser.T__0)
            self.state = 56
            self.objectives()
            self.state = 57
            self.match(StochmizeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Vars_defContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Vars_defContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.ID)
            else:
                return self.getToken(StochmizeParser.ID, i)

        def fixed_range_random(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.Fixed_range_randomContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.Fixed_range_randomContext,i)


        def getRuleIndex(self):
            return StochmizeParser.RULE_vars_def

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterVars_def(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitVars_def(self)




    def vars_def(self):

        localctx = StochmizeParser.Vars_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vars_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.match(StochmizeParser.ID)

                self.state = 60
                self.fixed_range_random()
                self.state = 61
                self.match(StochmizeParser.T__2)
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StochmizeParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fixed_range_randomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Fixed_range_randomContext, self).__init__(parent, invokingState)
            self.parser = parser

        def fixed(self):
            return self.getTypedRuleContext(StochmizeParser.FixedContext,0)


        def rang(self):
            return self.getTypedRuleContext(StochmizeParser.RangContext,0)


        def random(self):
            return self.getTypedRuleContext(StochmizeParser.RandomContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_fixed_range_random

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterFixed_range_random(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitFixed_range_random(self)




    def fixed_range_random(self):

        localctx = StochmizeParser.Fixed_range_randomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fixed_range_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            token = self._input.LA(1)
            if token in [StochmizeParser.T__3]:
                self.state = 67
                self.fixed()

            elif token in [StochmizeParser.T__5]:
                self.state = 68
                self.rang()

            elif token in [StochmizeParser.T__4]:
                self.state = 69
                self.random()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FixedContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.FixedContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(StochmizeParser.NUMBER, 0)

        def getRuleIndex(self):
            return StochmizeParser.RULE_fixed

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterFixed(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitFixed(self)




    def fixed(self):

        localctx = StochmizeParser.FixedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fixed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(StochmizeParser.T__3)
            self.state = 73
            self.match(StochmizeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RandomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.RandomContext, self).__init__(parent, invokingState)
            self.parser = parser

        def normal(self):
            return self.getTypedRuleContext(StochmizeParser.NormalContext,0)


        def unif(self):
            return self.getTypedRuleContext(StochmizeParser.UnifContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_random

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterRandom(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitRandom(self)




    def random(self):

        localctx = StochmizeParser.RandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(StochmizeParser.T__4)
            self.state = 78
            token = self._input.LA(1)
            if token in [StochmizeParser.NORMAL]:
                self.state = 76
                self.normal()

            elif token in [StochmizeParser.UNIF]:
                self.state = 77
                self.unif()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.RangContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.NUMBER)
            else:
                return self.getToken(StochmizeParser.NUMBER, i)

        def MINUS(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.MINUS)
            else:
                return self.getToken(StochmizeParser.MINUS, i)

        def getRuleIndex(self):
            return StochmizeParser.RULE_rang

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterRang(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitRang(self)




    def rang(self):

        localctx = StochmizeParser.RangContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rang)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(StochmizeParser.T__5)
            self.state = 81
            self.match(StochmizeParser.T__6)
            self.state = 83
            _la = self._input.LA(1)
            if _la==StochmizeParser.MINUS:
                self.state = 82
                self.match(StochmizeParser.MINUS)


            self.state = 85
            self.match(StochmizeParser.NUMBER)
            self.state = 86
            self.match(StochmizeParser.T__7)
            self.state = 88
            _la = self._input.LA(1)
            if _la==StochmizeParser.MINUS:
                self.state = 87
                self.match(StochmizeParser.MINUS)


            self.state = 90
            self.match(StochmizeParser.NUMBER)
            self.state = 91
            self.match(StochmizeParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NormalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.NormalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NORMAL(self):
            return self.getToken(StochmizeParser.NORMAL, 0)

        def normal_params(self):
            return self.getTypedRuleContext(StochmizeParser.Normal_paramsContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_normal

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterNormal(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitNormal(self)




    def normal(self):

        localctx = StochmizeParser.NormalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_normal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(StochmizeParser.NORMAL)
            self.state = 94
            self.match(StochmizeParser.T__6)
            self.state = 95
            self.normal_params()
            self.state = 96
            self.match(StochmizeParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnifContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.UnifContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNIF(self):
            return self.getToken(StochmizeParser.UNIF, 0)

        def unif_params(self):
            return self.getTypedRuleContext(StochmizeParser.Unif_paramsContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_unif

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterUnif(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitUnif(self)




    def unif(self):

        localctx = StochmizeParser.UnifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_unif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(StochmizeParser.UNIF)
            self.state = 99
            self.match(StochmizeParser.T__6)
            self.state = 100
            self.unif_params()
            self.state = 101
            self.match(StochmizeParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Normal_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Normal_paramsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.NUMBER)
            else:
                return self.getToken(StochmizeParser.NUMBER, i)

        def getRuleIndex(self):
            return StochmizeParser.RULE_normal_params

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterNormal_params(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitNormal_params(self)




    def normal_params(self):

        localctx = StochmizeParser.Normal_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_normal_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(StochmizeParser.T__9)
            self.state = 104
            self.match(StochmizeParser.T__3)
            self.state = 105
            self.match(StochmizeParser.NUMBER)
            self.state = 106
            self.match(StochmizeParser.T__7)
            self.state = 107
            self.match(StochmizeParser.T__10)
            self.state = 108
            self.match(StochmizeParser.T__3)
            self.state = 109
            self.match(StochmizeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unif_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Unif_paramsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.NUMBER)
            else:
                return self.getToken(StochmizeParser.NUMBER, i)

        def getRuleIndex(self):
            return StochmizeParser.RULE_unif_params

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterUnif_params(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitUnif_params(self)




    def unif_params(self):

        localctx = StochmizeParser.Unif_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unif_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(StochmizeParser.T__11)
            self.state = 112
            self.match(StochmizeParser.T__3)
            self.state = 113
            self.match(StochmizeParser.NUMBER)
            self.state = 114
            self.match(StochmizeParser.T__7)
            self.state = 115
            self.match(StochmizeParser.T__12)
            self.state = 116
            self.match(StochmizeParser.T__3)
            self.state = 117
            self.match(StochmizeParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubjtoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.SubjtoContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.ExprContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.ExprContext,i)


        def SUBJTO_DEF(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.SUBJTO_DEF)
            else:
                return self.getToken(StochmizeParser.SUBJTO_DEF, i)

        def NUMBER(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.NUMBER)
            else:
                return self.getToken(StochmizeParser.NUMBER, i)

        def getRuleIndex(self):
            return StochmizeParser.RULE_subjto

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterSubjto(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitSubjto(self)




    def subjto(self):

        localctx = StochmizeParser.SubjtoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_subjto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.expr()
                self.state = 120
                self.match(StochmizeParser.SUBJTO_DEF)
                self.state = 121
                self.match(StochmizeParser.NUMBER)
                self.state = 122
                self.match(StochmizeParser.T__2)
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StochmizeParser.T__6) | (1 << StochmizeParser.MINUS) | (1 << StochmizeParser.ID) | (1 << StochmizeParser.NUMBER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ObjectivesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.ObjectivesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def min_max(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.Min_maxContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.Min_maxContext,i)


        def ID(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.ID)
            else:
                return self.getToken(StochmizeParser.ID, i)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.ExprContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.ExprContext,i)


        def getRuleIndex(self):
            return StochmizeParser.RULE_objectives

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterObjectives(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitObjectives(self)




    def objectives(self):

        localctx = StochmizeParser.ObjectivesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_objectives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 128
                self.min_max()
                self.state = 129
                self.match(StochmizeParser.ID)
                self.state = 130
                self.match(StochmizeParser.T__3)
                self.state = 131
                self.expr()
                self.state = 132
                self.match(StochmizeParser.T__2)
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StochmizeParser.MAX or _la==StochmizeParser.MIN):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Min_maxContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Min_maxContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MAX(self):
            return self.getToken(StochmizeParser.MAX, 0)

        def MIN(self):
            return self.getToken(StochmizeParser.MIN, 0)

        def getRuleIndex(self):
            return StochmizeParser.RULE_min_max

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterMin_max(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitMin_max(self)




    def min_max(self):

        localctx = StochmizeParser.Min_maxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_min_max)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==StochmizeParser.MAX or _la==StochmizeParser.MIN):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr_content(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.Expr_contentContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.Expr_contentContext,i)


        def operators(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.OperatorsContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.OperatorsContext,i)


        def getRuleIndex(self):
            return StochmizeParser.RULE_expr

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterExpr(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitExpr(self)




    def expr(self):

        localctx = StochmizeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expr_content()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StochmizeParser.PLUS) | (1 << StochmizeParser.MINUS) | (1 << StochmizeParser.POW) | (1 << StochmizeParser.PROD) | (1 << StochmizeParser.DIV))) != 0):
                self.state = 141
                self.operators()
                self.state = 142
                self.expr_content()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_contentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.Expr_contentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(StochmizeParser.ID, 0)

        def NUMBER(self):
            return self.getToken(StochmizeParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(StochmizeParser.ExprContext,0)


        def MINUS(self):
            return self.getToken(StochmizeParser.MINUS, 0)

        def expr_content(self):
            return self.getTypedRuleContext(StochmizeParser.Expr_contentContext,0)


        def getRuleIndex(self):
            return StochmizeParser.RULE_expr_content

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterExpr_content(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitExpr_content(self)




    def expr_content(self):

        localctx = StochmizeParser.Expr_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr_content)
        self._la = 0 # Token type
        try:
            self.state = 156
            token = self._input.LA(1)
            if token in [StochmizeParser.ID, StochmizeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==StochmizeParser.ID or _la==StochmizeParser.NUMBER):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [StochmizeParser.T__6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(StochmizeParser.T__6)
                self.state = 151
                self.expr()
                self.state = 152
                self.match(StochmizeParser.T__8)

            elif token in [StochmizeParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.match(StochmizeParser.MINUS)
                self.state = 155
                self.expr_content()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(StochmizeParser.OperatorsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(StochmizeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(StochmizeParser.MINUS, 0)

        def PROD(self):
            return self.getToken(StochmizeParser.PROD, 0)

        def DIV(self):
            return self.getToken(StochmizeParser.DIV, 0)

        def POW(self):
            return self.getToken(StochmizeParser.POW, 0)

        def getRuleIndex(self):
            return StochmizeParser.RULE_operators

        def enterRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.enterOperators(self)

        def exitRule(self, listener):
            if isinstance( listener, StochmizeListener ):
                listener.exitOperators(self)




    def operators(self):

        localctx = StochmizeParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StochmizeParser.PLUS) | (1 << StochmizeParser.MINUS) | (1 << StochmizeParser.POW) | (1 << StochmizeParser.PROD) | (1 << StochmizeParser.DIV))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




