from generated.PJP_LanguageVisitor import PJP_LanguageVisitor
from generated.PJP_LanguageParser import PJP_LanguageParser


class TypeCheckVisitor(PJP_LanguageVisitor):
    def __init__(self):
        self.symbolTable = {}

    def visitDeclaration(self, ctx: PJP_LanguageParser.DeclarationContext):
        declaredType = ctx.primitiveType().getText()
        for varCtx in ctx.IDENTIFIER():
            varName = varCtx.getText()
            self.symbolTable[varName] = declaredType
        return None

    def visitAssignment(self, ctx: PJP_LanguageParser.AssignmentContext):
        # This method assumes the context of expr '=' expr
        # The left side of the assignment is another expr which could be an ID or another assignment
        leftExpr = ctx.expr(0)
        rightExpr = ctx.expr(1)

        # Evaluate the right side to get its type and value
        rightType = self.visit(rightExpr)

        # Now, handle the left side, which might be a chain of assignments
        def handleLeftExpr(leftCtx):
            # If the left expression is an identifier, we're at the end of the chain
            if isinstance(leftCtx, PJP_LanguageParser.IdContext):
                varName = leftCtx.IDENTIFIER().getText()
                if varName not in self.symbolTable:
                    print(f"Variable '{varName}' not declared.")
                declaredType = self.symbolTable[varName]
                if declaredType != rightType:
                    line = leftCtx.IDENTIFIER().getSymbol().line
                    # Assign int to float is allowed
                    if not (declaredType == 'float' and rightType == 'int'):
                        print(f"Type mismatch: cannot assign {rightType} to {declaredType} on line {line}.")
                # No need to return anything for type checking purposes
            elif isinstance(leftCtx, PJP_LanguageParser.AssignmentContext):
                # If it's another assignment, recursively handle it
                leftType = self.visit(leftCtx)
                if leftType != rightType:
                    print(f"Type mismatch in assignment chain.")
            else:
                print("Invalid assignment target.")

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
            print(f"Variable '{varName}' not declared.")
        return self.symbolTable[varName]

    def visitMulDivMod(self, ctx: PJP_LanguageParser.MulDivModContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))

        if (leftType == 'int' and rightType == 'float') or (leftType == 'float' and rightType == 'int'):
            return 'float'  # Result of operation between int and float is float
        elif leftType == rightType:
            return leftType  # Both ints or both floats

        print("Type mismatch in multiplication/division/modulus operation.")

    def visitAddSubCon(self, ctx: PJP_LanguageParser.AddSubConContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))

        # Handle concatenation separately if applicable
        if ctx.op.type == PJP_LanguageParser.CON:
            if leftType == rightType == 'string':
                return 'string'
            print("Concatenation operation requires string types.")

        # Allow int + float, float + int, and same-type arithmetic
        if (leftType == 'int' and rightType == 'float') or (leftType == 'float' and rightType == 'int'):
            return 'float'
        elif leftType == rightType:
            return leftType  # Both ints or both floats

        print(f"Type mismatch in addition/subtraction operation: {leftType}, {rightType}")

    def visitComparison(self, ctx: PJP_LanguageParser.ComparisonContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType:
            return 'bool'
        print("Type mismatch in comparison operation.")

    # Implement other visit methods as necessary
