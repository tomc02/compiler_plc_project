from generated_src.PJP_LanguageVisitor import PJP_LanguageVisitor
from generated_src.PJP_LanguageParser import PJP_LanguageParser


class TypeCheckVisitor(PJP_LanguageVisitor):
    def __init__(self):
        self.symbolTable = {}
        self.numberOfTypeErrors = 0

    def visitDeclaration(self, ctx: PJP_LanguageParser.DeclarationContext):
        declaredType = ctx.primitiveType().getText()
        for varCtx in ctx.IDENTIFIER():
            varName = varCtx.getText()
            if varName in self.symbolTable:
                self.printError(f"Variable '{varName}' already declared.", ctx)
            else:
                self.symbolTable[varName] = declaredType
        return None

    def visitAssignment(self, ctx: PJP_LanguageParser.AssignmentContext):
        # This method assumes the context of expr '=' expr
        # The left side of the assignment is another expr which could be an ID or another assignment
        leftExpr = ctx.expr(0)
        rightExpr = ctx.expr(1)

        # Evaluate the right side to get its type and value
        rightType = self.visit(rightExpr)

        def handleLeftExpr(leftCtx):
            # If the left expression is an identifier, we're at the end of the chain
            if isinstance(leftCtx, PJP_LanguageParser.IdContext):
                varName = leftCtx.IDENTIFIER().getText()
                if varName not in self.symbolTable:
                    self.printError(f"Variable '{varName}' not declared.", leftCtx)
                    return None
                declaredType = self.symbolTable[varName]
                if declaredType != rightType:
                    # Assign int to float is allowed
                    if not (declaredType == 'float' and rightType == 'int'):
                        self.printError(f"Type mismatch: cannot assign {rightType} to {declaredType}.", leftCtx)
                # No need to return anything for type checking purposes
            elif isinstance(leftCtx, PJP_LanguageParser.AssignmentContext):
                # If it's another assignment, recursively handle it
                leftType = self.visit(leftCtx)
                if leftType != rightType:
                    self.printError(f"Type mismatch in assignment chain.", leftCtx)
            else:
                self.printError("Invalid assignment target.", leftCtx)

        # Handle the left expression, which could trigger recursion for chained assignments
        handleLeftExpr(leftExpr)

        # The type of the assignment expression itself is the type of the right-hand side
        return rightType

    def visitInt(self, ctx: PJP_LanguageParser.IntContext):
        return 'int'

    def visitFloat(self, ctx: PJP_LanguageParser.FloatContext):
        return 'float'

    def visitString(self, ctx: PJP_LanguageParser.StringContext):
        return 'string'

    def visitBool(self, ctx: PJP_LanguageParser.BoolContext):
        return 'bool'

    def visitId(self, ctx: PJP_LanguageParser.IdContext):
        varName = ctx.IDENTIFIER().getText()
        if varName not in self.symbolTable:
            self.printError(f"Variable '{varName}' not declared.", ctx)
        return self.symbolTable[varName]

    def visitMulDivMod(self, ctx: PJP_LanguageParser.MulDivModContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))

        if (leftType == 'int' and rightType == 'float') or (leftType == 'float' and rightType == 'int'):
            return 'float'  # Result of operation between int and float is float
        elif leftType == rightType:
            return leftType  # Both ints or both floats

        self.printError(f"Type mismatch in multiplication/division/modulus operation.", ctx)

    def visitAddSubCon(self, ctx: PJP_LanguageParser.AddSubConContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))

        # Handle concatenation separately if applicable
        if ctx.op.type == PJP_LanguageParser.CON:
            if leftType == rightType == 'string':
                return 'string'
            self.printError(f"Concatenation operation requires string types.", ctx)

        # Allow int + float, float + int, and same-type arithmetic
        if (leftType == 'int' and rightType == 'float') or (leftType == 'float' and rightType == 'int'):
            return 'float'
        elif leftType == rightType and leftType in ['int', 'float']:
            return leftType  # Both ints or both floats

        self.printError(f"Type mismatch in add/sub operation: {leftType}, {rightType}.", ctx)

    def visitComparison(self, ctx: PJP_LanguageParser.ComparisonContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType:
            return 'bool'
        self.printError("Type mismatch in comparison operation.", ctx)

    def visitRelation(self, ctx:PJP_LanguageParser.RelationContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType or (leftType in ['int', 'float'] and rightType in ['int', 'float']):
            return 'bool'
        self.printError(f"Type mismatch in relation operation {leftType} and {rightType}.", ctx)

    def visitLogicalAnd(self, ctx:PJP_LanguageParser.LogicalAndContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType == 'bool':
            return 'bool'
        self.printError(f"Logical operation requires boolean types.", ctx)

    def visitLogicalOr(self, ctx:PJP_LanguageParser.LogicalOrContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType == 'bool':
            return 'bool'
        self.printError(f"Logical operation requires boolean types.", ctx)

    def visitNegation(self, ctx:PJP_LanguageParser.NegationContext):
        exprType = self.visit(ctx.expr())
        if exprType == 'bool':
            return 'bool'
        self.printError(f"Negation operation requires boolean type.", ctx)

    def visitParenthesis(self, ctx:PJP_LanguageParser.ParenthesisContext):
        return self.visit(ctx.expr())

    def visitIfElse(self, ctx:PJP_LanguageParser.IfElseContext):
        conditionType = self.visit(ctx.expr())
        if conditionType != 'bool':
            self.printError(f"If statement condition must be boolean.", ctx)
        return None

    def visitWhile(self, ctx:PJP_LanguageParser.WhileContext):
        conditionType = self.visit(ctx.expr())
        if conditionType != 'bool':
            self.printError(f"While loop condition must be boolean.", ctx)
        return None


    def printError(self, message, ctx=None):
        self.numberOfTypeErrors += 1
        if ctx is not None:
            line = ctx.start.line
            charPositionInLine = ctx.start.column
            message = f"Error {line}:{charPositionInLine} - {message}"
        else:
            message = f"Error - {message}"

        print(message)

    def getNumberOfTypeErrors(self):
        return self.numberOfTypeErrors
