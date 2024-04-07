import sys
from antlr4 import *
from generated_src.PJP_LanguageParser import PJP_LanguageParser
from generated_src.PJP_LanguageLexer import PJP_LanguageLexer
from TypeCheckVisitor import TypeCheckVisitor


def main(argv):
    input_stream = FileStream("inputs/in.txt")
    lexer = PJP_LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PJP_LanguageParser(stream)

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax error(s) found, exiting.")
        return
    visitor = TypeCheckVisitor()
    visitor.visit(tree)

    if visitor.getNumberOfTypeErrors() > 0:
        print("Type error(s) found, exiting.")
        return

    print(tree.toStringTree(recog=parser))



if __name__ == '__main__':
    main(sys.argv)