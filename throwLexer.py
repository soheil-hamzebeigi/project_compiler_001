# Generated from F:/Antlr/session 4/OpenUnderstand-master/openunderstand/analysis_passes\throw.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("%\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\6\5\33\n")
        buf.write("\5\r\5\16\5\34\3\5\6\5 \n\5\r\5\16\5!\5\5$\n\5\2\2\6\3")
        buf.write("\3\5\4\7\5\t\6\3\2\4\3\2c|\3\2C\\\2\'\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\20\3\2")
        buf.write("\2\2\7\27\3\2\2\2\t#\3\2\2\2\13\f\7x\2\2\f\r\7q\2\2\r")
        buf.write("\16\7k\2\2\16\17\7f\2\2\17\4\3\2\2\2\20\21\7v\2\2\21\22")
        buf.write("\7j\2\2\22\23\7t\2\2\23\24\7q\2\2\24\25\7y\2\2\25\26\7")
        buf.write("u\2\2\26\6\3\2\2\2\27\30\7\"\2\2\30\b\3\2\2\2\31\33\t")
        buf.write("\2\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35$\3\2\2\2\36 \t\3\2\2\37\36\3\2\2\2 !\3\2\2")
        buf.write("\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#\32\3\2\2\2#\37\3")
        buf.write("\2\2\2$\n\3\2\2\2\6\2\34!#\2")
        return buf.getvalue()


class throwLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    L = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'throws'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "L" ]

    ruleNames = [ "T__0", "T__1", "T__2", "L" ]

    grammarFileName = "throw.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


