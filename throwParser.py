# Generated from F:/Antlr/session 4/OpenUnderstand-master/openunderstand/analysis_passes\throw.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("!\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\32\2\16\3\2")
        buf.write("\2\2\4\26\3\2\2\2\6\30\3\2\2\2\b\32\3\2\2\2\n\34\3\2\2")
        buf.write("\2\f\36\3\2\2\2\16\17\5\4\3\2\17\20\5\f\7\2\20\21\5\6")
        buf.write("\4\2\21\22\5\f\7\2\22\23\5\b\5\2\23\24\5\f\7\2\24\25\5")
        buf.write("\n\6\2\25\3\3\2\2\2\26\27\7\3\2\2\27\5\3\2\2\2\30\31\7")
        buf.write("\6\2\2\31\7\3\2\2\2\32\33\7\4\2\2\33\t\3\2\2\2\34\35\7")
        buf.write("\6\2\2\35\13\3\2\2\2\36\37\7\5\2\2\37\r\3\2\2\2\2")
        return buf.getvalue()


class throwParser ( Parser ):

    grammarFileName = "throw.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void'", "'throws'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "L" ]

    RULE_prog = 0
    RULE_id1 = 1
    RULE_id2 = 2
    RULE_id3 = 3
    RULE_id4 = 4
    RULE_del1 = 5

    ruleNames =  [ "prog", "id1", "id2", "id3", "id4", "del1" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    L=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id1(self):
            return self.getTypedRuleContext(throwParser.Id1Context,0)


        def del1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(throwParser.Del1Context)
            else:
                return self.getTypedRuleContext(throwParser.Del1Context,i)


        def id2(self):
            return self.getTypedRuleContext(throwParser.Id2Context,0)


        def id3(self):
            return self.getTypedRuleContext(throwParser.Id3Context,0)


        def id4(self):
            return self.getTypedRuleContext(throwParser.Id4Context,0)


        def getRuleIndex(self):
            return throwParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = throwParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.id1()
            self.state = 13
            self.del1()
            self.state = 14
            self.id2()
            self.state = 15
            self.del1()
            self.state = 16
            self.id3()
            self.state = 17
            self.del1()
            self.state = 18
            self.id4()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return throwParser.RULE_id1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId1" ):
                listener.enterId1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId1" ):
                listener.exitId1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId1" ):
                return visitor.visitId1(self)
            else:
                return visitor.visitChildren(self)




    def id1(self):

        localctx = throwParser.Id1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_id1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(throwParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L(self):
            return self.getToken(throwParser.L, 0)

        def getRuleIndex(self):
            return throwParser.RULE_id2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId2" ):
                listener.enterId2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId2" ):
                listener.exitId2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId2" ):
                return visitor.visitId2(self)
            else:
                return visitor.visitChildren(self)




    def id2(self):

        localctx = throwParser.Id2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_id2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(throwParser.L)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return throwParser.RULE_id3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId3" ):
                listener.enterId3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId3" ):
                listener.exitId3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId3" ):
                return visitor.visitId3(self)
            else:
                return visitor.visitChildren(self)




    def id3(self):

        localctx = throwParser.Id3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_id3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(throwParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L(self):
            return self.getToken(throwParser.L, 0)

        def getRuleIndex(self):
            return throwParser.RULE_id4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId4" ):
                listener.enterId4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId4" ):
                listener.exitId4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId4" ):
                return visitor.visitId4(self)
            else:
                return visitor.visitChildren(self)




    def id4(self):

        localctx = throwParser.Id4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_id4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(throwParser.L)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Del1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return throwParser.RULE_del1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDel1" ):
                listener.enterDel1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDel1" ):
                listener.exitDel1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDel1" ):
                return visitor.visitDel1(self)
            else:
                return visitor.visitChildren(self)




    def del1(self):

        localctx = throwParser.Del1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_del1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(throwParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





