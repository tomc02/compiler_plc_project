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
        4,1,43,195,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,
        2,1,2,1,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,77,8,3,10,3,12,3,80,9,3,1,3,1,3,3,
        3,84,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,93,8,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,5,8,121,8,8,10,8,12,8,124,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,5,9,132,8,9,10,9,12,9,135,9,9,1,9,1,9,1,10,1,10,1,
        10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,161,8,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,5,12,184,8,12,10,12,12,12,187,9,12,1,13,1,
        13,1,13,1,13,3,13,193,8,13,1,13,0,1,24,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,5,1,0,8,9,1,0,15,17,2,0,14,14,18,19,1,0,20,21,1,
        0,23,24,215,0,29,1,0,0,0,2,45,1,0,0,0,4,47,1,0,0,0,6,83,1,0,0,0,
        8,85,1,0,0,0,10,94,1,0,0,0,12,100,1,0,0,0,14,106,1,0,0,0,16,116,
        1,0,0,0,18,127,1,0,0,0,20,138,1,0,0,0,22,141,1,0,0,0,24,160,1,0,
        0,0,26,192,1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,31,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,
        0,35,46,3,4,2,0,36,46,3,6,3,0,37,46,3,8,4,0,38,46,3,10,5,0,39,46,
        3,12,6,0,40,46,3,14,7,0,41,46,3,16,8,0,42,46,3,18,9,0,43,46,3,20,
        10,0,44,46,3,22,11,0,45,35,1,0,0,0,45,36,1,0,0,0,45,37,1,0,0,0,45,
        38,1,0,0,0,45,39,1,0,0,0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,
        0,45,43,1,0,0,0,45,44,1,0,0,0,46,3,1,0,0,0,47,48,5,1,0,0,48,52,3,
        2,1,0,49,51,3,2,1,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,
        53,1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,56,5,2,0,0,56,5,1,0,0,
        0,57,58,3,26,13,0,58,63,5,40,0,0,59,60,5,28,0,0,60,62,5,40,0,0,61,
        59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,
        0,65,63,1,0,0,0,66,67,5,27,0,0,67,84,1,0,0,0,68,69,3,26,13,0,69,
        70,5,40,0,0,70,71,5,3,0,0,71,78,3,24,12,0,72,73,5,28,0,0,73,74,5,
        40,0,0,74,75,5,3,0,0,75,77,3,24,12,0,76,72,1,0,0,0,77,80,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,
        27,0,0,82,84,1,0,0,0,83,57,1,0,0,0,83,68,1,0,0,0,84,7,1,0,0,0,85,
        86,5,31,0,0,86,87,5,4,0,0,87,88,3,24,12,0,88,89,5,5,0,0,89,92,3,
        2,1,0,90,91,5,32,0,0,91,93,3,2,1,0,92,90,1,0,0,0,92,93,1,0,0,0,93,
        9,1,0,0,0,94,95,3,24,12,0,95,96,5,6,0,0,96,97,3,24,12,0,97,98,5,
        7,0,0,98,99,3,24,12,0,99,11,1,0,0,0,100,101,5,33,0,0,101,102,5,4,
        0,0,102,103,3,24,12,0,103,104,5,5,0,0,104,105,3,2,1,0,105,13,1,0,
        0,0,106,107,5,35,0,0,107,108,5,4,0,0,108,109,3,24,12,0,109,110,5,
        27,0,0,110,111,3,24,12,0,111,112,5,27,0,0,112,113,3,24,12,0,113,
        114,5,5,0,0,114,115,3,2,1,0,115,15,1,0,0,0,116,117,5,29,0,0,117,
        122,5,40,0,0,118,119,5,28,0,0,119,121,5,40,0,0,120,118,1,0,0,0,121,
        124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,
        122,1,0,0,0,125,126,5,27,0,0,126,17,1,0,0,0,127,128,5,30,0,0,128,
        133,3,24,12,0,129,130,5,28,0,0,130,132,3,24,12,0,131,129,1,0,0,0,
        132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,136,1,0,0,0,
        135,133,1,0,0,0,136,137,5,27,0,0,137,19,1,0,0,0,138,139,3,24,12,
        0,139,140,5,27,0,0,140,21,1,0,0,0,141,142,5,27,0,0,142,23,1,0,0,
        0,143,144,6,12,-1,0,144,161,5,40,0,0,145,161,7,0,0,0,146,147,5,4,
        0,0,147,148,3,24,12,0,148,149,5,5,0,0,149,161,1,0,0,0,150,161,5,
        36,0,0,151,161,5,37,0,0,152,161,5,38,0,0,153,154,5,19,0,0,154,161,
        3,24,12,10,155,156,5,22,0,0,156,161,3,24,12,9,157,158,5,40,0,0,158,
        159,5,3,0,0,159,161,3,24,12,2,160,143,1,0,0,0,160,145,1,0,0,0,160,
        146,1,0,0,0,160,150,1,0,0,0,160,151,1,0,0,0,160,152,1,0,0,0,160,
        153,1,0,0,0,160,155,1,0,0,0,160,157,1,0,0,0,161,185,1,0,0,0,162,
        163,10,8,0,0,163,164,7,1,0,0,164,184,3,24,12,9,165,166,10,7,0,0,
        166,167,7,2,0,0,167,184,3,24,12,8,168,169,10,6,0,0,169,170,7,3,0,
        0,170,184,3,24,12,7,171,172,10,5,0,0,172,173,7,4,0,0,173,184,3,24,
        12,6,174,175,10,4,0,0,175,176,5,25,0,0,176,184,3,24,12,5,177,178,
        10,3,0,0,178,179,5,26,0,0,179,184,3,24,12,4,180,181,10,1,0,0,181,
        182,5,3,0,0,182,184,3,24,12,1,183,162,1,0,0,0,183,165,1,0,0,0,183,
        168,1,0,0,0,183,171,1,0,0,0,183,174,1,0,0,0,183,177,1,0,0,0,183,
        180,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,
        25,1,0,0,0,187,185,1,0,0,0,188,193,5,10,0,0,189,193,5,11,0,0,190,
        193,5,12,0,0,191,193,5,13,0,0,192,188,1,0,0,0,192,189,1,0,0,0,192,
        190,1,0,0,0,192,191,1,0,0,0,193,27,1,0,0,0,13,31,45,52,63,78,83,
        92,122,133,160,183,185,192
    ]

class PJP_LanguageParser ( Parser ):

    grammarFileName = "PJP_Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'='", "'('", "')'", "'?'", 
                     "':'", "'true'", "'false'", "'int'", "'float'", "'string'", 
                     "'bool'", "'.'", "'*'", "'/'", "'%'", "'+'", "'-'", 
                     "'<'", "'>'", "'!'", "'=='", "'!='", "'&&'", "'||'", 
                     "';'", "','", "'read'", "'write'", "'if'", "'else'", 
                     "'while'", "'do'", "'for'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT_KEYWORD", "FLOAT_KEYWORD", 
                      "STRING_KEYWORD", "BOOL_KEYWORD", "CON", "MUL", "DIV", 
                      "MOD", "ADD", "SUB", "LES", "GRE", "NEG", "EQ", "NEQ", 
                      "AND", "OR", "SEMI", "COMMA", "READ", "WRITE", "IF", 
                      "ELSE", "WHILE", "DO", "FOR", "INT", "FLOAT", "STRING", 
                      "BOOL", "IDENTIFIER", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_blockOfStatements = 2
    RULE_declaration = 3
    RULE_ifElse = 4
    RULE_ternaryIfElse = 5
    RULE_while = 6
    RULE_for = 7
    RULE_readStatement = 8
    RULE_writeStatement = 9
    RULE_baseExpr = 10
    RULE_emptyStatement = 11
    RULE_expr = 12
    RULE_primitiveType = 13

    ruleNames =  [ "start", "statement", "blockOfStatements", "declaration", 
                   "ifElse", "ternaryIfElse", "while", "for", "readStatement", 
                   "writeStatement", "baseExpr", "emptyStatement", "expr", 
                   "primitiveType" ]

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
    INT_KEYWORD=10
    FLOAT_KEYWORD=11
    STRING_KEYWORD=12
    BOOL_KEYWORD=13
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
    SEMI=27
    COMMA=28
    READ=29
    WRITE=30
    IF=31
    ELSE=32
    WHILE=33
    DO=34
    FOR=35
    INT=36
    FLOAT=37
    STRING=38
    BOOL=39
    IDENTIFIER=40
    WS=41
    COMMENT=42
    LINE_COMMENT=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
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
            return PJP_LanguageParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = PJP_LanguageParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1627394686738) != 0)):
                    break

            self.state = 33
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

        def blockOfStatements(self):
            return self.getTypedRuleContext(PJP_LanguageParser.BlockOfStatementsContext,0)


        def declaration(self):
            return self.getTypedRuleContext(PJP_LanguageParser.DeclarationContext,0)


        def ifElse(self):
            return self.getTypedRuleContext(PJP_LanguageParser.IfElseContext,0)


        def ternaryIfElse(self):
            return self.getTypedRuleContext(PJP_LanguageParser.TernaryIfElseContext,0)


        def while_(self):
            return self.getTypedRuleContext(PJP_LanguageParser.WhileContext,0)


        def for_(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ForContext,0)


        def readStatement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ReadStatementContext,0)


        def writeStatement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.WriteStatementContext,0)


        def baseExpr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.BaseExprContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.EmptyStatementContext,0)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PJP_LanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.blockOfStatements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.ifElse()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 38
                self.ternaryIfElse()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 39
                self.while_()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.for_()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 41
                self.readStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 42
                self.writeStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 43
                self.baseExpr()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 44
                self.emptyStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockOfStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_blockOfStatements

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




    def blockOfStatements(self):

        localctx = PJP_LanguageParser.BlockOfStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockOfStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PJP_LanguageParser.T__0)
            self.state = 48
            self.statement()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1627394686738) != 0):
                self.state = 49
                self.statement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(PJP_LanguageParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_declaration

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




    def declaration(self):

        localctx = PJP_LanguageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.primitiveType()
                self.state = 58
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 59
                    self.match(PJP_LanguageParser.COMMA)
                    self.state = 60
                    self.match(PJP_LanguageParser.IDENTIFIER)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(PJP_LanguageParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.primitiveType()
                self.state = 69
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 70
                self.match(PJP_LanguageParser.T__2)
                self.state = 71
                self.expr(0)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==28:
                    self.state = 72
                    self.match(PJP_LanguageParser.COMMA)
                    self.state = 73
                    self.match(PJP_LanguageParser.IDENTIFIER)
                    self.state = 74
                    self.match(PJP_LanguageParser.T__2)
                    self.state = 75
                    self.expr(0)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.match(PJP_LanguageParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pos = None # StatementContext
            self.neg = None # StatementContext

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

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_ifElse

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




    def ifElse(self):

        localctx = PJP_LanguageParser.IfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(PJP_LanguageParser.IF)
            self.state = 86
            self.match(PJP_LanguageParser.T__3)
            self.state = 87
            self.expr(0)
            self.state = 88
            self.match(PJP_LanguageParser.T__4)
            self.state = 89
            localctx.pos = self.statement()
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(PJP_LanguageParser.ELSE)
                self.state = 91
                localctx.neg = self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryIfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pos = None # ExprContext
            self.neg = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_ternaryIfElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryIfElse" ):
                listener.enterTernaryIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryIfElse" ):
                listener.exitTernaryIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryIfElse" ):
                return visitor.visitTernaryIfElse(self)
            else:
                return visitor.visitChildren(self)




    def ternaryIfElse(self):

        localctx = PJP_LanguageParser.TernaryIfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ternaryIfElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(PJP_LanguageParser.T__5)
            self.state = 96
            localctx.pos = self.expr(0)
            self.state = 97
            self.match(PJP_LanguageParser.T__6)
            self.state = 98
            localctx.neg = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(PJP_LanguageParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_while

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




    def while_(self):

        localctx = PJP_LanguageParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(PJP_LanguageParser.WHILE)
            self.state = 101
            self.match(PJP_LanguageParser.T__3)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.match(PJP_LanguageParser.T__4)
            self.state = 104
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(PJP_LanguageParser.FOR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PJP_LanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(PJP_LanguageParser.SEMI)
            else:
                return self.getToken(PJP_LanguageParser.SEMI, i)

        def statement(self):
            return self.getTypedRuleContext(PJP_LanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = PJP_LanguageParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(PJP_LanguageParser.FOR)
            self.state = 107
            self.match(PJP_LanguageParser.T__3)
            self.state = 108
            self.expr(0)
            self.state = 109
            self.match(PJP_LanguageParser.SEMI)
            self.state = 110
            self.expr(0)
            self.state = 111
            self.match(PJP_LanguageParser.SEMI)
            self.state = 112
            self.expr(0)
            self.state = 113
            self.match(PJP_LanguageParser.T__4)
            self.state = 114
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_readStatement

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




    def readStatement(self):

        localctx = PJP_LanguageParser.ReadStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_readStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(PJP_LanguageParser.READ)
            self.state = 117
            self.match(PJP_LanguageParser.IDENTIFIER)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 118
                self.match(PJP_LanguageParser.COMMA)
                self.state = 119
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(PJP_LanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_writeStatement

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




    def writeStatement(self):

        localctx = PJP_LanguageParser.WriteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_writeStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(PJP_LanguageParser.WRITE)
            self.state = 128
            self.expr(0)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 129
                self.match(PJP_LanguageParser.COMMA)
                self.state = 130
                self.expr(0)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(PJP_LanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_baseExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseExpr" ):
                listener.enterBaseExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseExpr" ):
                listener.exitBaseExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseExpr" ):
                return visitor.visitBaseExpr(self)
            else:
                return visitor.visitChildren(self)




    def baseExpr(self):

        localctx = PJP_LanguageParser.BaseExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_baseExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expr(0)
            self.state = 139
            self.match(PJP_LanguageParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(PJP_LanguageParser.SEMI, 0)

        def getRuleIndex(self):
            return PJP_LanguageParser.RULE_emptyStatement

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




    def emptyStatement(self):

        localctx = PJP_LanguageParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(PJP_LanguageParser.SEMI)
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


    class ParenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PJP_LanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PJP_LanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesis" ):
                listener.enterParenthesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesis" ):
                listener.exitParenthesis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = PJP_LanguageParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 144
                self.match(PJP_LanguageParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = PJP_LanguageParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = PJP_LanguageParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(PJP_LanguageParser.T__3)
                self.state = 147
                self.expr(0)
                self.state = 148
                self.match(PJP_LanguageParser.T__4)
                pass

            elif la_ == 4:
                localctx = PJP_LanguageParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.match(PJP_LanguageParser.INT)
                pass

            elif la_ == 5:
                localctx = PJP_LanguageParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 151
                self.match(PJP_LanguageParser.FLOAT)
                pass

            elif la_ == 6:
                localctx = PJP_LanguageParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.match(PJP_LanguageParser.STRING)
                pass

            elif la_ == 7:
                localctx = PJP_LanguageParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                localctx.prefix = self.match(PJP_LanguageParser.SUB)
                self.state = 154
                self.expr(10)
                pass

            elif la_ == 8:
                localctx = PJP_LanguageParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                localctx.prefix = self.match(PJP_LanguageParser.NEG)
                self.state = 156
                self.expr(9)
                pass

            elif la_ == 9:
                localctx = PJP_LanguageParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(PJP_LanguageParser.IDENTIFIER)
                self.state = 158
                self.match(PJP_LanguageParser.T__2)
                self.state = 159
                self.expr(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = PJP_LanguageParser.MulDivModContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 163
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 229376) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 164
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = PJP_LanguageParser.AddSubConContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 166
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 802816) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 167
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = PJP_LanguageParser.RelationContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 169
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = PJP_LanguageParser.ComparisonContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 171
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 172
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = PJP_LanguageParser.LogicalAndContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 174
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 175
                        self.match(PJP_LanguageParser.AND)
                        self.state = 176
                        self.expr(5)
                        pass

                    elif la_ == 6:
                        localctx = PJP_LanguageParser.LogicalOrContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 178
                        self.match(PJP_LanguageParser.OR)
                        self.state = 179
                        self.expr(4)
                        pass

                    elif la_ == 7:
                        localctx = PJP_LanguageParser.AssignmentContext(self, PJP_LanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 181
                        self.match(PJP_LanguageParser.T__2)
                        self.state = 182
                        self.expr(1)
                        pass

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_primitiveType)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                localctx.type_ = self.match(PJP_LanguageParser.INT_KEYWORD)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                localctx.type_ = self.match(PJP_LanguageParser.FLOAT_KEYWORD)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                localctx.type_ = self.match(PJP_LanguageParser.STRING_KEYWORD)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
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
        self._predicates[12] = self.expr_sempred
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
         




