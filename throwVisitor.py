# Generated from F:/Antlr/session 4/OpenUnderstand-master/openunderstand/analysis_passes\throw.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .throwParser import throwParser
else:
    from throwParser import throwParser

# This class defines a complete generic visitor for a parse tree produced by throwParser.

class throwVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by throwParser#prog.
    def visitProg(self, ctx:throwParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by throwParser#id1.
    def visitId1(self, ctx:throwParser.Id1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by throwParser#id2.
    def visitId2(self, ctx:throwParser.Id2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by throwParser#id3.
    def visitId3(self, ctx:throwParser.Id3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by throwParser#id4.
    def visitId4(self, ctx:throwParser.Id4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by throwParser#del1.
    def visitDel1(self, ctx:throwParser.Del1Context):
        return self.visitChildren(ctx)



del throwParser