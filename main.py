import sys
from antlr4 import *
from generated.PJP_LanguageParser import PJP_LanguageParser
from generated.PJP_LanguageLexer import PJP_LanguageLexer



def main(argv):
    input_stream = FileStream("in.txt")
    lexer = PJP_LanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = PJP_LanguageParser(stream)

    tree = parser.program()

    print(tree.toStringTree(recog=parser))



if __name__ == '__main__':
    main(sys.argv)