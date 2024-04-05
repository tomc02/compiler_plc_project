# Generated from PJP_Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PJP_LanguageParser import PJP_LanguageParser
else:
    from PJP_LanguageParser import PJP_LanguageParser

# This class defines a complete generic visitor for a parse tree produced by PJP_LanguageParser.

class PJP_LanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PJP_LanguageParser#program.
    def visitProgram(self, ctx:PJP_LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#statement.
    def visitStatement(self, ctx:PJP_LanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#blockOfStatements.
    def visitBlockOfStatements(self, ctx:PJP_LanguageParser.BlockOfStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#declaration.
    def visitDeclaration(self, ctx:PJP_LanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#ifElse.
    def visitIfElse(self, ctx:PJP_LanguageParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#while.
    def visitWhile(self, ctx:PJP_LanguageParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#for.
    def visitFor(self, ctx:PJP_LanguageParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#doWhile.
    def visitDoWhile(self, ctx:PJP_LanguageParser.DoWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#readStatement.
    def visitReadStatement(self, ctx:PJP_LanguageParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#writeStatement.
    def visitWriteStatement(self, ctx:PJP_LanguageParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#showExpr.
    def visitShowExpr(self, ctx:PJP_LanguageParser.ShowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#emptyStatement.
    def visitEmptyStatement(self, ctx:PJP_LanguageParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#mulDivMod.
    def visitMulDivMod(self, ctx:PJP_LanguageParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#parens.
    def visitParens(self, ctx:PJP_LanguageParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#negation.
    def visitNegation(self, ctx:PJP_LanguageParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#comparison.
    def visitComparison(self, ctx:PJP_LanguageParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#bool.
    def visitBool(self, ctx:PJP_LanguageParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#string.
    def visitString(self, ctx:PJP_LanguageParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#assignment.
    def visitAssignment(self, ctx:PJP_LanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#logicalAnd.
    def visitLogicalAnd(self, ctx:PJP_LanguageParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#float.
    def visitFloat(self, ctx:PJP_LanguageParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#int.
    def visitInt(self, ctx:PJP_LanguageParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#relation.
    def visitRelation(self, ctx:PJP_LanguageParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#addSubCon.
    def visitAddSubCon(self, ctx:PJP_LanguageParser.AddSubConContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#unaryMinus.
    def visitUnaryMinus(self, ctx:PJP_LanguageParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#id.
    def visitId(self, ctx:PJP_LanguageParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#logicalOr.
    def visitLogicalOr(self, ctx:PJP_LanguageParser.LogicalOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJP_LanguageParser#primitiveType.
    def visitPrimitiveType(self, ctx:PJP_LanguageParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)



del PJP_LanguageParser