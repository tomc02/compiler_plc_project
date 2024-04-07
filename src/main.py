import sys
from antlr4 import *
from generated_src.PJP_LanguageParser import PJP_LanguageParser
from generated_src.PJP_LanguageLexer import PJP_LanguageLexer
from TypeCheckVisitor import TypeCheckVisitor
from SemanticVisitor import SemanticVisitor


def main(argv):
    input_stream = FileStream("inputs/in.txt")
    lexer = PJP_LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PJP_LanguageParser(stream)

    tree = parser.program()

    visitor = TypeCheckVisitor()
    visitor.visit(tree)

    semantic_visitor = SemanticVisitor()
    semantic_visitor.visit(tree)
    semantic_visitor.printSymbolTable()

    print(tree.toStringTree(recog=parser))



if __name__ == '__main__':
    main(sys.argv)