def shunting_yard(tokens):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []
    last_token = None
    
    for token in tokens:
        if isinstance(token, int):
            if last_token == ')':
                return "ERROR"  
            output.append(token)
        elif token in "+-*/":
            while (operator_stack and operator_stack[-1] in "+-*/" and
                   priority[operator_stack[-1]] >= priority[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            if last_token and isinstance(last_token, int):
                return "ERROR"
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        last_token = token
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

def evaluate(expression):
    stack = []
    for token in expression:
        if isinstance(token, int):
            stack.append(token)
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    return "ERROR"
                stack.append(a // b)
    return stack[0] if stack else "ERROR"

def parse(expression):
    tokens = []
    number = ''
    for char in expression:
        if char.isdigit():
            number += char
        else:
            if number != '':
                tokens.append(int(number))
                number = ''
            if char in "+-*/()":
                tokens.append(char)
    if number != '':
        tokens.append(int(number))
    return tokens

def solve_expressions(inputs):
    results = []
    for expression in inputs:
        try:
            parsed = parse(expression)
            postfix = shunting_yard(parsed)
            result = evaluate(postfix)
            results.append(result)
        except Exception as e:
            results.append("ERROR")
    return results


if __name__ == "__main__":
    inputs = []
    count = int(input())
    while count > 0:
        inputs.append(str(input()))
        count -= 1
    print(solve_expressions(inputs))
