from generated_src.PJP_LanguageVisitor import PJP_LanguageVisitor
from generated_src.PJP_LanguageParser import PJP_LanguageParser
from TypeCheckVisitor import TypeCheckVisitor


class InstructionGeneratorVisitor(PJP_LanguageVisitor):
    def __init__(self, type_check_visitor: TypeCheckVisitor):
        self.instructions = []
        self.label_count = 0
        self.defaultValues = {
            "int": "0",
            "float": "0.0",
            "string": '""',
            "bool": "true"
        }
        self.typeCheckVisitor = type_check_visitor

    def new_label(self):
        self.label_count += 1
        return f"{self.label_count}"

    def visitStart(self, ctx: PJP_LanguageParser.StartContext):
        for child in ctx.children:
            self.visit(child)
        return self.instructions

    def visitBaseExpr(self, ctx: PJP_LanguageParser.BaseExprContext):
        self.visit(ctx.expr())
        self.instructions.append("pop")
        #self.instructions.append("print 1")

    def visitId(self, ctx: PJP_LanguageParser.IdContext):
        self.instructions.append(f"load {ctx.getText()} ")

    def visitDeclaration(self, ctx: PJP_LanguageParser.DeclarationContext):
        declaredType = ctx.primitiveType().getText()
        for varCtx in ctx.IDENTIFIER():
            varName = varCtx.getText()
            self.instructions.append(f"push {declaredType[0].upper()} {self.defaultValues[declaredType]}")
            self.instructions.append(f"save {varName}")

    def visitIfElse(self, ctx: PJP_LanguageParser.IfElseContext):
        end_label = self.new_label()
        else_label = self.new_label() if ctx.neg else end_label

        self.visit(ctx.expr())  # Condition
        self.instructions.append(f"fjmp {else_label}")
        self.visit(ctx.pos)  # If-part
        self.instructions.append(f"jmp {end_label}")
        self.instructions.append(f"label {else_label}")
        if ctx.neg:
            self.visit(ctx.neg)  # Else-part
        self.instructions.append(f"label {end_label}")

    def visitTernaryIfElse(self, ctx:PJP_LanguageParser.TernaryIfElseContext):
        end_label = self.new_label()
        else_label = self.new_label() if ctx.neg else end_label

        self.visit(ctx.expr(0))
        self.instructions.append(f"fjmp {else_label}")
        self.visit(ctx.expr(1))
        self.instructions.append(f"jmp {end_label}")
        self.instructions.append(f"label {else_label}")
        self.visit(ctx.expr(2))
        self.instructions.append(f"label {end_label}")


    def visitWhile(self, ctx: PJP_LanguageParser.WhileContext):
        start_label = self.new_label()
        end_label = self.new_label()

        self.instructions.append(f"label {start_label}")
        self.visit(ctx.expr())  # Condition
        self.instructions.append(f"fjmp {end_label}")
        self.visit(ctx.statement())  # Body
        self.instructions.append(f"jmp {start_label}")
        self.instructions.append(f"label {end_label}")

    def visitAssignment(self, ctx: PJP_LanguageParser.AssignmentContext):
        self.visit(ctx.expr(1))
        self.checkIntConversion(ctx)
        varName = ctx.expr(0).getText()
        if self.instructions[-1] == "pop":
            self.instructions[-1] = f"save {varName}"
        else:
            self.instructions.append(f"save {varName}")
        self.instructions.append(f"load {varName}")
        if isinstance(ctx.expr(0), PJP_LanguageParser.IdContext):
            #self.instructions.append("pop")
            pass

    def visitAddSubCon(self, ctx: PJP_LanguageParser.AddSubConContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.checkIntConversion(ctx)
        operation_type = self.getOperationType(ctx.expr(0), ctx.expr(1))
        if ctx.op.type == PJP_LanguageParser.ADD:
            self.instructions.append("add " + operation_type)
        elif ctx.op.type == PJP_LanguageParser.SUB:
            self.instructions.append("sub " + operation_type)
        elif ctx.op.type == PJP_LanguageParser.CON:
            self.instructions.append("concat")

    def visitMulDivMod(self, ctx: PJP_LanguageParser.MulDivModContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.checkIntConversion(ctx)
        operation_type = self.getOperationType(ctx.expr(0), ctx.expr(1))
        if ctx.op.type == PJP_LanguageParser.MUL:
            self.instructions.append("mul " + operation_type)
        elif ctx.op.type == PJP_LanguageParser.DIV:
            self.instructions.append("div " + operation_type)
        elif ctx.op.type == PJP_LanguageParser.MOD:
            self.instructions.append("mod")

    def visitRelation(self, ctx: PJP_LanguageParser.RelationContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.checkIntConversion(ctx)
        if ctx.op.type == PJP_LanguageParser.LES:
            self.instructions.append("lt")
        elif ctx.op.type == PJP_LanguageParser.GRE:
            self.instructions.append("gt")

    def visitComparison(self, ctx: PJP_LanguageParser.ComparisonContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.checkIntConversion(ctx)
        if ctx.op.type == PJP_LanguageParser.EQ:
            self.instructions.append("eq")
        elif ctx.op.type == PJP_LanguageParser.NEQ:
            self.instructions.append("eq")
            self.instructions.append("not")

    def visitLogicalAnd(self, ctx: PJP_LanguageParser.LogicalAndContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.instructions.append("and")

    def visitLogicalOr(self, ctx: PJP_LanguageParser.LogicalOrContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        self.instructions.append("or")

    def visitNegation(self, ctx: PJP_LanguageParser.NegationContext):
        self.visit(ctx.expr())
        self.instructions.append("not")

    def visitUnaryMinus(self, ctx: PJP_LanguageParser.UnaryMinusContext):
        self.visit(ctx.expr())
        self.instructions.append("uminus")

    def visitInt(self, ctx: PJP_LanguageParser.IntContext):
        self.instructions.append(f"push I {ctx.getText()}")

    def visitFloat(self, ctx: PJP_LanguageParser.FloatContext):
        self.instructions.append(f"push F {ctx.getText()}")

    def visitString(self, ctx: PJP_LanguageParser.StringContext):
        self.instructions.append(f"push S {ctx.getText()}")

    def visitBool(self, ctx: PJP_LanguageParser.BoolContext):
        self.instructions.append(f"push B {ctx.getText()}")

    def visitWriteStatement(self, ctx: PJP_LanguageParser.WriteStatementContext):
        count = len(ctx.expr())
        for child in ctx.children:
            self.visit(child)
        self.instructions.append("print " + str(count))

    def visitReadStatement(self, ctx: PJP_LanguageParser.ReadStatementContext):
        for identifier in ctx.IDENTIFIER():
            identifier_type = self.typeCheckVisitor.getVarType(identifier.getText())
            self.instructions.append(f"read {identifier_type[0].upper()}")
            self.instructions.append(f"save {identifier}")

    def getOperationType(self, first, second):
        first_type = self.typeCheckVisitor.visit(first)
        second_type = self.typeCheckVisitor.visit(second)
        if first_type == 'float' or second_type == 'float':
            return 'F'
        return 'I'

    def checkIntConversion(self, ctx):
        leftType = self.typeCheckVisitor.visit(ctx.expr(0))
        rightType = self.typeCheckVisitor.visit(ctx.expr(1))
        if leftType != rightType:
            if rightType == 'int':
                self.instructions.append("itof")
            else:
                self.instructions.insert(-1, "itof")


    def saveInstructions(self, filename):
        with open(filename, 'w') as f:
            for instr in self.instructions:
                f.write(f"{instr}\n")

    def getInstructions(self):
        return self.instructions
