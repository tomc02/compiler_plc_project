from generated_src.PJP_LanguageVisitor import PJP_LanguageVisitor
from generated_src.PJP_LanguageParser import PJP_LanguageParser


class SemanticVisitor(PJP_LanguageVisitor):
    def __init__(self):
        self.symbolTable = {}
        self.initialValues = {
            'int': 0,
            'float': 0.0,
            'bool': False,
            'string': ''
        }

    def visitDeclaration(self, ctx: PJP_LanguageParser.DeclarationContext):
        declaredType = ctx.primitiveType().getText()
        for varCtx in ctx.IDENTIFIER():
            varName = varCtx.getText()
            self.symbolTable[varName] = {
                'type': declaredType,
                'value': self.initialValues[declaredType]
            }
        return None

    def visitAssignment(self, ctx: PJP_LanguageParser.AssignmentContext):
        # Right associative handling
        leftExpr = ctx.expr(0)
        rightExpr = ctx.expr(1)
        rightType = self.visit(rightExpr)

        # Assuming leftExpr is always an ID in this context
        varName = leftExpr.getText()
        if varName not in self.symbolTable:
            raise Exception(f"Variable '{varName}' not declared.")

        varType = self.symbolTable[varName]['type']
        if varType == 'float' and rightType == 'int':
            # Automatic int to float conversion
            pass
        elif varType != rightType:
            raise Exception(f"Type mismatch: cannot assign {rightType} to {varType} variable '{varName}'.")


        self.symbolTable[varName]['value'] = rightExpr.getText()

        return varType

    def visitId(self, ctx: PJP_LanguageParser.IdContext):
        varName = ctx.IDENTIFIER().getText()
        if varName not in self.symbolTable:
            raise Exception(f"Variable '{varName}' not declared.")
        return self.symbolTable[varName]['type']

    def visitInt(self, ctx: PJP_LanguageParser.IntContext):
        return 'int'

    def visitFloat(self, ctx: PJP_LanguageParser.FloatContext):
        return 'float'

    def visitString(self, ctx: PJP_LanguageParser.StringContext):
        return 'string'

    def visitBool(self, ctx: PJP_LanguageParser.BoolContext):
        return 'bool'

    # Implement visit methods for each operator, e.g., for addition:
    def visitAddSubCon(self, ctx: PJP_LanguageParser.AddSubConContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))

        if ctx.op.type == PJP_LanguageParser.CON:
            if leftType == rightType == 'string':
                return 'string'
            raise Exception("Concatenation requires string operands.")
        elif leftType == 'float' or rightType == 'float':
            return 'float'  # Automatic int to float conversion
        elif leftType == rightType == 'int':
            return 'int'
        else:
            raise Exception("Type mismatch in addition/subtraction.")


    # Similar methods for visitMulDivMod, visitComparison, etc.

    # Implement visit methods for logical operations, e.g., AND, OR
    def visitLogicalAnd(self, ctx: PJP_LanguageParser.LogicalAndContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType == 'bool':
            return 'bool'
        raise Exception("Logical 'AND' requires boolean operands.")

    def visitLogicalOr(self, ctx: PJP_LanguageParser.LogicalOrContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType == 'bool':
            return 'bool'
        raise Exception("Logical 'OR' requires boolean operands.")

    def visitComparison(self, ctx: PJP_LanguageParser.ComparisonContext):
        leftType = self.visit(ctx.expr(0))
        rightType = self.visit(ctx.expr(1))
        if leftType == rightType:
            return 'bool'
        raise Exception("Type mismatch in comparison operation.")

    def visitIfElse(self, ctx: PJP_LanguageParser.IfElseContext):
        conditionType = self.visit(ctx.expr())
        if conditionType != 'bool':
            raise Exception("If condition must be a boolean expression.")
        return None

    def printError(self, message, ctx=None):
        if ctx is not None:
            print(f"Error at line {ctx.start.line}, column {ctx.start.column}: {message}")
        else:
            print(f"Error: {message}")

    def printSymbolTable(self):
        print("Symbol Table:")
        for varName, varData in self.symbolTable.items():
            print(f"{varName} ({varData['type']}): {varData['value']}")


