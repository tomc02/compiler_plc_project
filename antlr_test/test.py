import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.error.ErrorListener import ConsoleErrorListener

def create_error_listener():
    class ErrorListener(ConsoleErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            raise Exception(f"line {line}:{column} {msg}")

    return ErrorListener()

def main(argv):
    input_stream = FileStream("in.txt")
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    error_listener = create_error_listener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    

    tree = parser.start_()

    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)