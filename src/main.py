import sys
import os
from antlr4 import *
from generated_src.PJP_LanguageParser import PJP_LanguageParser
from generated_src.PJP_LanguageLexer import PJP_LanguageLexer
from TypeCheckVisitor import TypeCheckVisitor


def main(argv):
    inputs_dir = "inputs/"
    for input_file in os.listdir(inputs_dir):
        print(f"Processing {input_file}")
        input_stream = FileStream("inputs/" + input_file)
        lexer = PJP_LanguageLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = PJP_LanguageParser(stream)

        tree = parser.start()

        if parser.getNumberOfSyntaxErrors() > 0:
            print("Syntax error(s) found, exiting.")
            print("***************************************************")
            continue
        visitor = TypeCheckVisitor()
        visitor.visit(tree)

        if visitor.getNumberOfTypeErrors() > 0:
            print("Type error(s) found, exiting.")
            print("***************************************************")
            continue

        print(tree.toStringTree(recog=parser))
        print("No errors found.")
        print("***************************************************")



if __name__ == '__main__':
    main(sys.argv)