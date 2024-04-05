# Generated from PJP_Language.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,130,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,5,1,19,8,1,10,1,12,1,22,9,1,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,44,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,
        1,56,8,1,10,1,12,1,59,9,1,1,1,1,1,1,1,1,1,1,1,5,1,66,8,1,10,1,12,
        1,69,9,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,96,8,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,119,8,2,10,2,12,2,122,9,2,1,3,1,3,1,3,1,3,3,3,
        128,8,3,1,3,0,1,4,4,0,2,4,6,0,5,1,0,5,6,1,0,15,17,2,0,14,14,18,19,
        1,0,20,21,1,0,23,24,156,0,9,1,0,0,0,2,76,1,0,0,0,4,95,1,0,0,0,6,
        127,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,
        11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,
        0,0,16,20,3,2,1,0,17,19,3,2,1,0,18,17,1,0,0,0,19,22,1,0,0,0,20,18,
        1,0,0,0,20,21,1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,2,0,0,
        24,77,1,0,0,0,25,26,3,6,3,0,26,31,5,32,0,0,27,28,5,13,0,0,28,30,
        5,32,0,0,29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,12,0,0,35,77,1,0,0,0,36,37,5,
        29,0,0,37,38,5,3,0,0,38,39,3,4,2,0,39,40,5,4,0,0,40,43,3,2,1,0,41,
        42,5,30,0,0,42,44,3,2,1,0,43,41,1,0,0,0,43,44,1,0,0,0,44,77,1,0,
        0,0,45,46,5,31,0,0,46,47,5,3,0,0,47,48,3,4,2,0,48,49,5,4,0,0,49,
        50,3,2,1,0,50,77,1,0,0,0,51,52,5,27,0,0,52,57,5,32,0,0,53,54,5,13,
        0,0,54,56,5,32,0,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,60,1,0,0,0,59,57,1,0,0,0,60,77,5,12,0,0,61,62,5,28,
        0,0,62,67,3,4,2,0,63,64,5,13,0,0,64,66,3,4,2,0,65,63,1,0,0,0,66,
        69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,
        0,70,71,5,12,0,0,71,77,1,0,0,0,72,73,3,4,2,0,73,74,5,12,0,0,74,77,
        1,0,0,0,75,77,5,12,0,0,76,15,1,0,0,0,76,25,1,0,0,0,76,36,1,0,0,0,
        76,45,1,0,0,0,76,51,1,0,0,0,76,61,1,0,0,0,76,72,1,0,0,0,76,75,1,
        0,0,0,77,3,1,0,0,0,78,79,6,2,-1,0,79,96,5,32,0,0,80,96,7,0,0,0,81,
        82,5,3,0,0,82,83,3,4,2,0,83,84,5,4,0,0,84,96,1,0,0,0,85,96,5,34,
        0,0,86,96,5,33,0,0,87,96,5,36,0,0,88,89,5,19,0,0,89,96,3,4,2,10,
        90,91,5,22,0,0,91,96,3,4,2,9,92,93,5,32,0,0,93,94,5,7,0,0,94,96,
        3,4,2,2,95,78,1,0,0,0,95,80,1,0,0,0,95,81,1,0,0,0,95,85,1,0,0,0,
        95,86,1,0,0,0,95,87,1,0,0,0,95,88,1,0,0,0,95,90,1,0,0,0,95,92,1,
        0,0,0,96,120,1,0,0,0,97,98,10,8,0,0,98,99,7,1,0,0,99,119,3,4,2,9,
        100,101,10,7,0,0,101,102,7,2,0,0,102,119,3,4,2,8,103,104,10,6,0,
        0,104,105,7,3,0,0,105,119,3,4,2,7,106,107,10,5,0,0,107,108,7,4,0,
        0,108,119,3,4,2,6,109,110,10,4,0,0,110,111,5,25,0,0,111,119,3,4,
        2,5,112,113,10,3,0,0,113,114,5,26,0,0,114,119,3,4,2,4,115,116,10,
        1,0,0,116,117,5,7,0,0,117,119,3,4,2,1,118,97,1,0,0,0,118,100,1,0,
        0,0,118,103,1,0,0,0,118,106,1,0,0,0,118,109,1,0,0,0,118,112,1,0,
        0,0,118,115,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,
        0,0,121,5,1,0,0,0,122,120,1,0,0,0,123,128,5,8,0,0,124,128,5,9,0,
        0,125,128,5,10,0,0,126,128,5,11,0,0,127,123,1,0,0,0,127,124,1,0,
        0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,7,1,0,0,0,11,11,20,31,43,
        57,67,76,95,118,120,127
    ]

class PJP_LanguageParser ( Parser ):

    grammarFileName = "PJP_Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "'true'", 
                     "'false'", "'='", "'int'", "'float'", "'string'", "'bool'", 
                     "';'", "','", "'.'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'<'", "'>'", "'!'", "'=='", "'!='", "'&&'", "'||'", 
                     "'read'", "'write'", "'if'", "'else'", "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT_KEYWORD", "FLOAT_KEYWORD", "STRING_KEYWORD", 
                      "BOOL_KEYWORD", "SEMI", "COMMA", "CON", "MUL", "DIV", 
                      "MOD", "ADD", "SUB", "LES", "GRE", "NEG", "EQ", "NEQ", 
                      "AND", "OR", "READ", "WRITE", "IF", "ELSE", "WHILE", 
                      "IDENTIFIER", "FLOAT", "INT", "BOOL", "STRING", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_primitiveType = 3

    ruleNames =  [ "program", "statement", "expr", "primitiveType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    INT_KEYWORD=8
    FLOAT_KEYWORD=9
    STRING_KEYWORD=10
    BOOL_KEYWORD=11
    SEMI=12
    COMMA=13
    CON=14
    MUL=15
    DIV=16
    MOD=17
    ADD=18
    SUB=19
    LES=20
    GRE=21
    NEG=22
    EQ=23
    NEQ=24
    AND=25
    OR=26
    READ=27
    WRITE=28
    IF=29
    ELSE=30
    WHILE=31
    IDENTIFIER=32
    FLOAT=33
    INT=34
    BOOL=35
    STRING=36
    WS=37
    COMMENT=38
    LINE_COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PJP_LanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PJP_LanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 101875982186) != 0)):
                    break

            self.state = 13
            self.match(PJP_LanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(PJP_LanguageParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.COMMA)
            else:
                return self.getToken(PJP_LanguageParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockOfStatementsContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockOfStatements" ):
                listener.enterBlockOfStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockOfStatements" ):
                listener.exitBlockOfStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockOfStatements" ):
                return visitor.visitBlockOfStatements(self)
            else:
                return visitor.visitChildren(self)


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(PJP_LanguageParser.READ, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.IDENTIFIER)
            else:
                return self.getToken(PJP_LanguageParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.COMMA)
            else:
                return self.getToken(PJP_LanguageParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(PJP_LanguageParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)

        def statement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(PJP_LanguageParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.IDENTIFIER)
            else:
                return self.getToken(PJP_LanguageParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.COMMA)
            else:
                return self.getToken(PJP_LanguageParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.pos = None # StatementContext
            self.neg = None # StatementContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(PJP_LanguageParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(PJP_LanguageParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = PJP_LanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = PJP_LanguageParser.BlockOfStatementsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(PJP_LanguageParser.T__0)
                self.state = 16
                self.statement()
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 101875982186) != 0):
                    self.state = 17
                    self.statement()
                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 23
                self.match(PJP_LanguageParser.T__1)
                pass
            elif token in [8, 9, 10, 11]:
                localctx = PJP_LanguageParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.primitiveType()
                self.state = 26
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 27
                    self.match(PJP_LanguageParser.COMMA)
                    self.state = 28
                    self.match(PJP_LanguageParser.IDENTIFIER)
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.match(PJP_LanguageParser.SEMI)
                pass
            elif token in [29]:
                localctx = PJP_LanguageParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(PJP_LanguageParser.IF)
                self.state = 37
                self.match(PJP_LanguageParser.T__2)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.match(PJP_LanguageParser.T__3)
                self.state = 40
                localctx.pos = self.statement()
                self.state = 43
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 41
                    self.match(PJP_LanguageParser.ELSE)
                    self.state = 42
                    localctx.neg = self.statement()


                pass
            elif token in [31]:
                localctx = PJP_LanguageParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(PJP_LanguageParser.WHILE)
                self.state = 46
                self.match(PJP_LanguageParser.T__2)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(PJP_LanguageParser.T__3)
                self.state = 49
                self.statement()
                pass
            elif token in [27]:
                localctx = PJP_LanguageParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.match(PJP_LanguageParser.READ)
                self.state = 52
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 53
                    self.match(PJP_LanguageParser.COMMA)
                    self.state = 54
                    self.match(PJP_LanguageParser.IDENTIFIER)
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(PJP_LanguageParser.SEMI)
                pass
            elif token in [28]:
                localctx = PJP_LanguageParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 61
                self.match(PJP_LanguageParser.WRITE)
                self.state = 62
                self.expr(0)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==13:
                    self.state = 63
                    self.match(PJP_LanguageParser.COMMA)
                    self.state = 64
                    self.expr(0)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self.match(PJP_LanguageParser.SEMI)
                pass
            elif token in [3, 5, 6, 19, 22, 32, 33, 34, 36]:
                localctx = PJP_LanguageParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(PJP_LanguageParser.SEMI)
                pass
            elif token in [12]:
                localctx = PJP_LanguageParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.match(PJP_LanguageParser.SEMI)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def MUL(self):
            return self.getToken(PJP_LanguageParser.MUL, 0)
        def DIV(self):
            return self.getToken(PJP_LanguageParser.DIV, 0)
        def MOD(self):
            return self.getToken(PJP_LanguageParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)

        def NEG(self):
            return self.getToken(PJP_LanguageParser.NEG, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def EQ(self):
            return self.getToken(PJP_LanguageParser.EQ, 0)
        def NEQ(self):
            return self.getToken(PJP_LanguageParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PJP_LanguageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PJP_LanguageParser.IDENTIFIER, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def AND(self):
            return self.getToken(PJP_LanguageParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PJP_LanguageParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(PJP_LanguageParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class RelationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def LES(self):
            return self.getToken(PJP_LanguageParser.LES, 0)
        def GRE(self):
            return self.getToken(PJP_LanguageParser.GRE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def ADD(self):
            return self.getToken(PJP_LanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(PJP_LanguageParser.SUB, 0)
        def CON(self):
            return self.getToken(PJP_LanguageParser.CON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubCon" ):
                listener.enterAddSubCon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubCon" ):
                listener.exitAddSubCon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubCon" ):
                return visitor.visitAddSubCon(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.prefix = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)

        def SUB(self):
            return self.getToken(PJP_LanguageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(PJP_LanguageParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)

        def OR(self):
            return self.getToken(PJP_LanguageParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PJP_LanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = PJP_LanguageParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 79
                self.match(PJP_LanguageParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = PJP_LanguageParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = PJP_LanguageParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 81
                self.match(PJP_LanguageParser.T__2)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(PJP_LanguageParser.T__3)
                pass

            elif la_ == 4:
                localctx = PJP_LanguageParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 85
                self.match(PJP_LanguageParser.INT)
                pass

            elif la_ == 5:
                localctx = PJP_LanguageParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.match(PJP_LanguageParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = PJP_LanguageParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.match(PJP_LanguageParser.STRING)
                pass

            elif la_ == 7:
                localctx = PJP_LanguageParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                localctx.prefix = self.match(PJP_LanguageParser.SUB)
                self.state = 89
                self.expr(10)
                pass

            elif la_ == 8:
                localctx = PJP_LanguageParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                localctx.prefix = self.match(PJP_LanguageParser.NEG)
                self.state = 91
                self.expr(9)
                pass

            elif la_ == 9:
                localctx = PJP_LanguageParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 93
                self.match(PJP_LanguageParser.T__6)
                self.state = 94
                self.expr(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 118
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = PJP_LanguageParser.MulDivModContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 97
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PJP_LanguageParser.AddSubConContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 802816) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = PJP_LanguageParser.RelationContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 103
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 104
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 105
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = PJP_LanguageParser.ComparisonContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 106
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 107
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 108
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = PJP_LanguageParser.LogicalAndContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 109
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 110
                        self.match(PJP_LanguageParser.AND)
                        self.state = 111
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = PJP_LanguageParser.LogicalOrContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 112
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 113
                        self.match(PJP_LanguageParser.OR)
                        self.state = 114
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = PJP_LanguageParser.AssignmentContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 115
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 116
                        self.match(PJP_LanguageParser.T__6)
                        self.state = 117
                        self.expr(1)
                        pass

             
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT_KEYWORD(self):
            return self.getToken(PJP_LanguageParser.INT_KEYWORD, 0)

        def FLOAT_KEYWORD(self):
            return self.getToken(PJP_LanguageParser.FLOAT_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(PJP_LanguageParser.STRING_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(PJP_LanguageParser.BOOL_KEYWORD, 0)

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = PJP_LanguageParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primitiveType)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                localctx.type_ = self.match(PJP_LanguageParser.INT_KEYWORD)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                localctx.type_ = self.match(PJP_LanguageParser.FLOAT_KEYWORD)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                localctx.type_ = self.match(PJP_LanguageParser.STRING_KEYWORD)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                localctx.type_ = self.match(PJP_LanguageParser.BOOL_KEYWORD)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         




