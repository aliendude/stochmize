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
        buf.write(u" \u008c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\2\6\2%\n\2")
        buf.write(u"\r\2\16\2&\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4;\n\4\3\4\3\4\6\4?")
        buf.write(u"\n\4\r\4\16\4@\3\5\3\5\3\5\3\6\3\6\3\6\5\6I\n\6\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write(u"\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write(u"\13\3\13\3\13\3\13\6\13j\n\13\r\13\16\13k\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\6\ft\n\f\r\f\16\fu\3\r\3\r\3\r\3\r\7\r|")
        buf.write(u"\n\r\f\r\16\r\177\13\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\5\16\u0088\n\16\3\17\3\17\3\17\2\2\20\2\4\6\b\n")
        buf.write(u"\f\16\20\22\24\26\30\32\34\2\5\3\2\27\30\3\2\36\37\3")
        buf.write(u"\2\31\35\u0086\2$\3\2\2\2\4*\3\2\2\2\6>\3\2\2\2\bB\3")
        buf.write(u"\2\2\2\nE\3\2\2\2\fJ\3\2\2\2\16O\3\2\2\2\20T\3\2\2\2")
        buf.write(u"\22\\\3\2\2\2\24i\3\2\2\2\26s\3\2\2\2\30w\3\2\2\2\32")
        buf.write(u"\u0087\3\2\2\2\34\u0089\3\2\2\2\36\37\7\21\2\2\37 \7")
        buf.write(u"\36\2\2 !\7\3\2\2!\"\5\4\3\2\"#\7\4\2\2#%\3\2\2\2$\36")
        buf.write(u"\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()")
        buf.write(u"\7\2\2\3)\3\3\2\2\2*+\7\22\2\2+,\7\3\2\2,-\5\6\4\2-.")
        buf.write(u"\7\4\2\2./\7\23\2\2/\60\7\3\2\2\60\61\5\24\13\2\61\62")
        buf.write(u"\7\4\2\2\62\63\7\24\2\2\63\64\7\3\2\2\64\65\5\26\f\2")
        buf.write(u"\65\66\7\4\2\2\66\5\3\2\2\2\67:\7\36\2\28;\5\b\5\29;")
        buf.write(u"\5\n\6\2:8\3\2\2\2:9\3\2\2\2;<\3\2\2\2<=\7\5\2\2=?\3")
        buf.write(u"\2\2\2>\67\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\7\3")
        buf.write(u"\2\2\2BC\7\6\2\2CD\7\37\2\2D\t\3\2\2\2EH\7\7\2\2FI\5")
        buf.write(u"\f\7\2GI\5\16\b\2HF\3\2\2\2HG\3\2\2\2I\13\3\2\2\2JK\7")
        buf.write(u"\25\2\2KL\7\b\2\2LM\5\20\t\2MN\7\t\2\2N\r\3\2\2\2OP\7")
        buf.write(u"\26\2\2PQ\7\b\2\2QR\5\22\n\2RS\7\t\2\2S\17\3\2\2\2TU")
        buf.write(u"\7\n\2\2UV\7\6\2\2VW\7\37\2\2WX\7\13\2\2XY\7\f\2\2YZ")
        buf.write(u"\7\6\2\2Z[\7\37\2\2[\21\3\2\2\2\\]\7\r\2\2]^\7\6\2\2")
        buf.write(u"^_\7\37\2\2_`\7\13\2\2`a\7\16\2\2ab\7\6\2\2bc\7\37\2")
        buf.write(u"\2c\23\3\2\2\2de\5\30\r\2ef\7 \2\2fg\7\37\2\2gh\7\5\2")
        buf.write(u"\2hj\3\2\2\2id\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2")
        buf.write(u"l\25\3\2\2\2mn\t\2\2\2no\7\36\2\2op\7\6\2\2pq\5\30\r")
        buf.write(u"\2qr\7\5\2\2rt\3\2\2\2sm\3\2\2\2tu\3\2\2\2us\3\2\2\2")
        buf.write(u"uv\3\2\2\2v\27\3\2\2\2w}\5\32\16\2xy\5\34\17\2yz\5\32")
        buf.write(u"\16\2z|\3\2\2\2{x\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3")
        buf.write(u"\2\2\2~\31\3\2\2\2\177}\3\2\2\2\u0080\u0088\t\3\2\2\u0081")
        buf.write(u"\u0082\7\b\2\2\u0082\u0083\5\30\r\2\u0083\u0084\7\t\2")
        buf.write(u"\2\u0084\u0088\3\2\2\2\u0085\u0086\7\32\2\2\u0086\u0088")
        buf.write(u"\5\32\16\2\u0087\u0080\3\2\2\2\u0087\u0081\3\2\2\2\u0087")
        buf.write(u"\u0085\3\2\2\2\u0088\33\3\2\2\2\u0089\u008a\t\4\2\2\u008a")
        buf.write(u"\35\3\2\2\2\n&:@Hku}\u0087")
        return buf.getvalue()


class StochmizeParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'{'", u"'}'", u"';'", u"'='", u"'~'", 
                     u"'('", u"')'", u"'m'", u"','", u"'v'", u"'a'", u"'b'", 
                     u"<INVALID>", u"<INVALID>", u"'model'", u"'vars'", 
                     u"'subjto'", u"'objectives'", u"'Normal'", u"'Unif'", 
                     u"'max'", u"'min'", u"'+'", u"'-'", u"'**'", u"'*'", 
                     u"'/'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"WHITESPACE", u"NEWLINE", u"MODEL", 
                      u"VARS_DEF", u"SUBJTO", u"OBJECTIVES", u"NORMAL", 
                      u"UNIF", u"MAX", u"MIN", u"PLUS", u"MINUS", u"POW", 
                      u"PROD", u"DIV", u"ID", u"NUMBER", u"SUBJTO_DEF" ]

    RULE_program = 0
    RULE_model = 1
    RULE_vars_def = 2
    RULE_fixed = 3
    RULE_random = 4
    RULE_normal = 5
    RULE_unif = 6
    RULE_normal_params = 7
    RULE_unif_params = 8
    RULE_subjto = 9
    RULE_objectives = 10
    RULE_expr = 11
    RULE_expr_content = 12
    RULE_operators = 13

    ruleNames =  [ u"program", u"model", u"vars_def", u"fixed", u"random", 
                   u"normal", u"unif", u"normal_params", u"unif_params", 
                   u"subjto", u"objectives", u"expr", u"expr_content", u"operators" ]

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
    WHITESPACE=13
    NEWLINE=14
    MODEL=15
    VARS_DEF=16
    SUBJTO=17
    OBJECTIVES=18
    NORMAL=19
    UNIF=20
    MAX=21
    MIN=22
    PLUS=23
    MINUS=24
    POW=25
    PROD=26
    DIV=27
    ID=28
    NUMBER=29
    SUBJTO_DEF=30

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
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.match(StochmizeParser.MODEL)
                self.state = 29
                self.match(StochmizeParser.ID)
                self.state = 30
                self.match(StochmizeParser.T__0)
                self.state = 31
                self.model()
                self.state = 32
                self.match(StochmizeParser.T__1)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==StochmizeParser.MODEL):
                    break

            self.state = 38
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
            self.state = 40
            self.match(StochmizeParser.VARS_DEF)
            self.state = 41
            self.match(StochmizeParser.T__0)
            self.state = 42
            self.vars_def()
            self.state = 43
            self.match(StochmizeParser.T__1)
            self.state = 44
            self.match(StochmizeParser.SUBJTO)
            self.state = 45
            self.match(StochmizeParser.T__0)
            self.state = 46
            self.subjto()
            self.state = 47
            self.match(StochmizeParser.T__1)
            self.state = 48
            self.match(StochmizeParser.OBJECTIVES)
            self.state = 49
            self.match(StochmizeParser.T__0)
            self.state = 50
            self.objectives()
            self.state = 51
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

        def fixed(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.FixedContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.FixedContext,i)


        def random(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(StochmizeParser.RandomContext)
            else:
                return self.getTypedRuleContext(StochmizeParser.RandomContext,i)


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
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.match(StochmizeParser.ID)
                self.state = 56
                token = self._input.LA(1)
                if token in [StochmizeParser.T__3]:
                    self.state = 54
                    self.fixed()

                elif token in [StochmizeParser.T__4]:
                    self.state = 55
                    self.random()

                else:
                    raise NoViableAltException(self)

                self.state = 58
                self.match(StochmizeParser.T__2)
                self.state = 62 
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
        self.enterRule(localctx, 6, self.RULE_fixed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(StochmizeParser.T__3)
            self.state = 65
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
        self.enterRule(localctx, 8, self.RULE_random)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(StochmizeParser.T__4)
            self.state = 70
            token = self._input.LA(1)
            if token in [StochmizeParser.NORMAL]:
                self.state = 68
                self.normal()

            elif token in [StochmizeParser.UNIF]:
                self.state = 69
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
        self.enterRule(localctx, 10, self.RULE_normal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(StochmizeParser.NORMAL)
            self.state = 73
            self.match(StochmizeParser.T__5)
            self.state = 74
            self.normal_params()
            self.state = 75
            self.match(StochmizeParser.T__6)
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
        self.enterRule(localctx, 12, self.RULE_unif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(StochmizeParser.UNIF)
            self.state = 78
            self.match(StochmizeParser.T__5)
            self.state = 79
            self.unif_params()
            self.state = 80
            self.match(StochmizeParser.T__6)
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
        self.enterRule(localctx, 14, self.RULE_normal_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(StochmizeParser.T__7)
            self.state = 83
            self.match(StochmizeParser.T__3)
            self.state = 84
            self.match(StochmizeParser.NUMBER)
            self.state = 85
            self.match(StochmizeParser.T__8)
            self.state = 86
            self.match(StochmizeParser.T__9)
            self.state = 87
            self.match(StochmizeParser.T__3)
            self.state = 88
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
        self.enterRule(localctx, 16, self.RULE_unif_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(StochmizeParser.T__10)
            self.state = 91
            self.match(StochmizeParser.T__3)
            self.state = 92
            self.match(StochmizeParser.NUMBER)
            self.state = 93
            self.match(StochmizeParser.T__8)
            self.state = 94
            self.match(StochmizeParser.T__11)
            self.state = 95
            self.match(StochmizeParser.T__3)
            self.state = 96
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
        self.enterRule(localctx, 18, self.RULE_subjto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.expr()
                self.state = 99
                self.match(StochmizeParser.SUBJTO_DEF)
                self.state = 100
                self.match(StochmizeParser.NUMBER)
                self.state = 101
                self.match(StochmizeParser.T__2)
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StochmizeParser.T__5) | (1 << StochmizeParser.MINUS) | (1 << StochmizeParser.ID) | (1 << StochmizeParser.NUMBER))) != 0)):
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


        def MAX(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.MAX)
            else:
                return self.getToken(StochmizeParser.MAX, i)

        def MIN(self, i=None):
            if i is None:
                return self.getTokens(StochmizeParser.MIN)
            else:
                return self.getToken(StochmizeParser.MIN, i)

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
        self.enterRule(localctx, 20, self.RULE_objectives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==StochmizeParser.MAX or _la==StochmizeParser.MIN):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 108
                self.match(StochmizeParser.ID)
                self.state = 109
                self.match(StochmizeParser.T__3)
                self.state = 110
                self.expr()
                self.state = 111
                self.match(StochmizeParser.T__2)
                self.state = 115 
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
        self.enterRule(localctx, 22, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expr_content()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << StochmizeParser.PLUS) | (1 << StochmizeParser.MINUS) | (1 << StochmizeParser.POW) | (1 << StochmizeParser.PROD) | (1 << StochmizeParser.DIV))) != 0):
                self.state = 118
                self.operators()
                self.state = 119
                self.expr_content()
                self.state = 125
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
        self.enterRule(localctx, 24, self.RULE_expr_content)
        self._la = 0 # Token type
        try:
            self.state = 133
            token = self._input.LA(1)
            if token in [StochmizeParser.ID, StochmizeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                _la = self._input.LA(1)
                if not(_la==StochmizeParser.ID or _la==StochmizeParser.NUMBER):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [StochmizeParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(StochmizeParser.T__5)
                self.state = 128
                self.expr()
                self.state = 129
                self.match(StochmizeParser.T__6)

            elif token in [StochmizeParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(StochmizeParser.MINUS)
                self.state = 132
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
        self.enterRule(localctx, 26, self.RULE_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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




