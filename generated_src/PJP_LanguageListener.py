# Generated from PJP_Language.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PJP_LanguageParser import PJP_LanguageParser
else:
    from PJP_LanguageParser import PJP_LanguageParser

# This class defines a complete listener for a parse tree produced by PJP_LanguageParser.
class PJP_LanguageListener(ParseTreeListener):

    # Enter a parse tree produced by PJP_LanguageParser#program.
    def enterProgram(self, ctx:PJP_LanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#program.
    def exitProgram(self, ctx:PJP_LanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#statement.
    def enterStatement(self, ctx:PJP_LanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#statement.
    def exitStatement(self, ctx:PJP_LanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#blockOfStatements.
    def enterBlockOfStatements(self, ctx:PJP_LanguageParser.BlockOfStatementsContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#blockOfStatements.
    def exitBlockOfStatements(self, ctx:PJP_LanguageParser.BlockOfStatementsContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#declaration.
    def enterDeclaration(self, ctx:PJP_LanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#declaration.
    def exitDeclaration(self, ctx:PJP_LanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#ifElse.
    def enterIfElse(self, ctx:PJP_LanguageParser.IfElseContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#ifElse.
    def exitIfElse(self, ctx:PJP_LanguageParser.IfElseContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#while.
    def enterWhile(self, ctx:PJP_LanguageParser.WhileContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#while.
    def exitWhile(self, ctx:PJP_LanguageParser.WhileContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#for.
    def enterFor(self, ctx:PJP_LanguageParser.ForContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#for.
    def exitFor(self, ctx:PJP_LanguageParser.ForContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#doWhile.
    def enterDoWhile(self, ctx:PJP_LanguageParser.DoWhileContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#doWhile.
    def exitDoWhile(self, ctx:PJP_LanguageParser.DoWhileContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#readStatement.
    def enterReadStatement(self, ctx:PJP_LanguageParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#readStatement.
    def exitReadStatement(self, ctx:PJP_LanguageParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#writeStatement.
    def enterWriteStatement(self, ctx:PJP_LanguageParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#writeStatement.
    def exitWriteStatement(self, ctx:PJP_LanguageParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#showExpr.
    def enterShowExpr(self, ctx:PJP_LanguageParser.ShowExprContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#showExpr.
    def exitShowExpr(self, ctx:PJP_LanguageParser.ShowExprContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#emptyStatement.
    def enterEmptyStatement(self, ctx:PJP_LanguageParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#emptyStatement.
    def exitEmptyStatement(self, ctx:PJP_LanguageParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#mulDivMod.
    def enterMulDivMod(self, ctx:PJP_LanguageParser.MulDivModContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#mulDivMod.
    def exitMulDivMod(self, ctx:PJP_LanguageParser.MulDivModContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#negation.
    def enterNegation(self, ctx:PJP_LanguageParser.NegationContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#negation.
    def exitNegation(self, ctx:PJP_LanguageParser.NegationContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#comparison.
    def enterComparison(self, ctx:PJP_LanguageParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#comparison.
    def exitComparison(self, ctx:PJP_LanguageParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#bool.
    def enterBool(self, ctx:PJP_LanguageParser.BoolContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#bool.
    def exitBool(self, ctx:PJP_LanguageParser.BoolContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#string.
    def enterString(self, ctx:PJP_LanguageParser.StringContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#string.
    def exitString(self, ctx:PJP_LanguageParser.StringContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#assignment.
    def enterAssignment(self, ctx:PJP_LanguageParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#assignment.
    def exitAssignment(self, ctx:PJP_LanguageParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#float.
    def enterFloat(self, ctx:PJP_LanguageParser.FloatContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#float.
    def exitFloat(self, ctx:PJP_LanguageParser.FloatContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#parenthesis.
    def enterParenthesis(self, ctx:PJP_LanguageParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#parenthesis.
    def exitParenthesis(self, ctx:PJP_LanguageParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#int.
    def enterInt(self, ctx:PJP_LanguageParser.IntContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#int.
    def exitInt(self, ctx:PJP_LanguageParser.IntContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#logical.
    def enterLogical(self, ctx:PJP_LanguageParser.LogicalContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#logical.
    def exitLogical(self, ctx:PJP_LanguageParser.LogicalContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#relation.
    def enterRelation(self, ctx:PJP_LanguageParser.RelationContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#relation.
    def exitRelation(self, ctx:PJP_LanguageParser.RelationContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#addSubCon.
    def enterAddSubCon(self, ctx:PJP_LanguageParser.AddSubConContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#addSubCon.
    def exitAddSubCon(self, ctx:PJP_LanguageParser.AddSubConContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#unaryMinus.
    def enterUnaryMinus(self, ctx:PJP_LanguageParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#unaryMinus.
    def exitUnaryMinus(self, ctx:PJP_LanguageParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#id.
    def enterId(self, ctx:PJP_LanguageParser.IdContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#id.
    def exitId(self, ctx:PJP_LanguageParser.IdContext):
        pass


    # Enter a parse tree produced by PJP_LanguageParser#primitiveType.
    def enterPrimitiveType(self, ctx:PJP_LanguageParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PJP_LanguageParser#primitiveType.
    def exitPrimitiveType(self, ctx:PJP_LanguageParser.PrimitiveTypeContext):
        pass



del PJP_LanguageParser