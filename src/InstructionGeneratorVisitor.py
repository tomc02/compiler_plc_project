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
        return f"label_{self.label_count}"

    def visitStart(self, ctx:PJP_LanguageParser.StartContext):
        for child in ctx.children:
            self.visit(child)
        return self.instructions

    def visitBaseExpr(self, ctx:PJP_LanguageParser.BaseExprContext):
        self.visit(ctx.expr())
        #self.instructions.append("print 1")

    def visitId(self, ctx:PJP_LanguageParser.IdContext):
        self.instructions.append(f"load {ctx.getText()} ")

    def visitDeclaration(self, ctx:PJP_LanguageParser.DeclarationContext):
        declaredType = ctx.primitiveType().getText()
        for varCtx in ctx.IDENTIFIER():
            varName = varCtx.getText()
            self.instructions.append(f"push {declaredType[0].upper()} {self.defaultValues[declaredType]}")
            self.instructions.append(f"save {varName}")

    def visitIfElse(self, ctx:PJP_LanguageParser.IfElseContext):
        end_label = self.new_label()
        else_label = self.new_label() if ctx.neg else end_label

        self.visit(ctx.expr())  # Condition
        self.instructions.append(f"fjmp {else_label}")
        self.visit(ctx.pos)  # If-part
        if ctx.neg:
            self.instructions.append(f"jmp {end_label}")
            self.instructions.append(f"label {else_label}")
            self.visit(ctx.neg)  # Else-part
        self.instructions.append(f"label {end_label}")

    def visitWhile(self, ctx:PJP_LanguageParser.WhileContext):
        start_label = self.new_label()
        end_label = self.new_label()

        self.instructions.append(f"label {start_label}")
        self.visit(ctx.expr())  # Condition
        self.instructions.append(f"fjmp {end_label}")
        self.visit(ctx.statement())  # Body
        self.instructions.append(f"jmp {start_label}")
        self.instructions.append(f"label {end_label}")

    def visitAssignment(self, ctx:PJP_LanguageParser.AssignmentContext):
        self.visit(ctx.expr(1))
        leftType = self.typeCheckVisitor.visit(ctx.expr(0))
        rightType = self.typeCheckVisitor.visit(ctx.expr(1))
        print(leftType, rightType)
        if leftType != rightType:
            self.instructions.append("itof")
        varName = ctx.expr(0).getText()
        self.instructions.append(f"save {varName}")
        self.instructions.append(f"load {varName}")
        self.instructions.append("pop")

    def visitAddSubCon(self, ctx:PJP_LanguageParser.AddSubConContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        if ctx.op.type == PJP_LanguageParser.ADD:
            self.instructions.append("add")
        elif ctx.op.type == PJP_LanguageParser.SUB:
            self.instructions.append("sub")
        elif ctx.op.type == PJP_LanguageParser.CON:
            self.instructions.append("concat")

    def visitMulDivMod(self, ctx:PJP_LanguageParser.MulDivModContext):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        leftType = self.typeCheckVisitor.visit(ctx.expr(0))
        rightType = self.typeCheckVisitor.visit(ctx.expr(1))
        if leftType != rightType:
            self.instructions.append("itof")
        if ctx.op.type == PJP_LanguageParser.MUL:
            self.instructions.append("mul")
        elif ctx.op.type == PJP_LanguageParser.DIV:
            self.instructions.append("div")
        elif ctx.op.type == PJP_LanguageParser.MOD:
            self.instructions.append("mod")

    def visitUnaryMinus(self, ctx:PJP_LanguageParser.UnaryMinusContext):
        self.visit(ctx.expr())
        self.instructions.append("uminus")

    def visitInt(self, ctx:PJP_LanguageParser.IntContext):
        self.instructions.append(f"push I {ctx.getText()}")

    def visitFloat(self, ctx:PJP_LanguageParser.FloatContext):
        self.instructions.append(f"push F {ctx.getText()}")

    def visitString(self, ctx:PJP_LanguageParser.StringContext):
        self.instructions.append(f"push S {ctx.getText()}")

    def visitBool(self, ctx:PJP_LanguageParser.BoolContext):
        print(ctx.getText())
        self.instructions.append(f"push B {ctx.getText()}")
        print(self.instructions[-1])

    def visitWriteStatement(self, ctx:PJP_LanguageParser.WriteStatementContext):
        count = len(ctx.expr())
        for child in ctx.children:
            self.visit(child)
        self.instructions.append("print " + str(count))

    def saveInstructions(self, filename):
        with open(filename, 'w') as f:
            for instr in self.instructions:
                f.write(f"{instr}\n")

