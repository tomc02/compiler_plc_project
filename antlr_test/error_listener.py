# create error listener for antlr4

def create_error_listener():
    class ErrorListener(ConsoleErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            raise Exception(f"line {line}:{column} {msg}")

    return ErrorListener()