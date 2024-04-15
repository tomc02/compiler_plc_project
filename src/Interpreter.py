class Interpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.labels = {}
        self.instructions = []
        self.pc = 0

    def load_instructions(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                instruction = line.strip().split()
                self.instructions.append(instruction)

    def load_labels(self):
        for i, instruction in enumerate(self.instructions):
            if instruction[0] == 'label':
                self.labels[int(instruction[1])] = i

    def execute(self):
        while self.pc < len(self.instructions):
            instruction = self.instructions[self.pc]
            code = instruction[0]

            if code == 'add':
                self.binary_operation(lambda x, y: x + y)
            elif code == 'sub':
                self.binary_operation(lambda x, y: x - y)
            elif code == 'mul':
                self.binary_operation(lambda x, y: x * y)
            elif code == 'div':
                self.binary_operation(lambda x, y: x / y)
            elif code == 'mod':
                self.binary_operation(lambda x, y: x % y)
            elif code == 'uminus':
                self.unary_operation(lambda x: -x)
            elif code == 'concat':
                self.binary_operation(lambda x, y: x + y)
            elif code == 'and':
                self.binary_operation(lambda x, y: x and y)
            elif code == 'or':
                self.binary_operation(lambda x, y: x or y)
            elif code == 'gt':
                self.binary_operation(lambda x, y: x > y)
            elif code == 'lt':
                self.binary_operation(lambda x, y: x < y)
            elif code == 'eq':
                self.binary_operation(lambda x, y: x == y)
            elif code == 'not':
                self.unary_operation(lambda x: not x)
            elif code == 'itof':
                value = self.stack.pop()
                self.stack.append(float(value))
            elif code == 'push':
                self.push_operation(instruction)
            elif code == 'pop':
                self.stack.pop()
            elif code == 'load':
                self.load_operation(instruction)
            elif code == 'save':
                self.save_operation(instruction)
            elif code == 'jmp':
                self.pc = self.labels[int(instruction[1])]
                continue
            elif code == 'fjmp':
                condition = self.stack.pop()
                if not condition:
                    self.pc = self.labels[int(instruction[1])]
                    continue
            elif code == 'print':
                self.print_operation(instruction)
            elif code == 'read':
                self.read_operation(instruction)

            self.pc += 1

    def binary_operation(self, operation):
        y = self.stack.pop()
        x = self.stack.pop()
        result = operation(x, y)
        self.stack.append(result)

    def unary_operation(self, operation):
        x = self.stack.pop()
        result = operation(x)
        self.stack.append(result)

    def push_operation(self, instruction):
        value_type = instruction[1]
        if value_type == 'I':
            value = int(instruction[2])
        elif value_type == 'F':
            value = float(instruction[2])
        elif value_type == 'S':
            string_inside_quotes = ' '.join(instruction[2:])
            value = string_inside_quotes[1:-1]  # Remove quotation marks
        elif value_type == 'B':
            value = instruction[2] == 'true'
        self.stack.append(value)

    def load_operation(self, instruction):
        var_name = instruction[1]
        value = self.variables.get(var_name, None)
        if value is not None:
            self.stack.append(value)
        else:
            print(f"Error: Variable '{var_name}' not defined.")

    def save_operation(self, instruction):
        var_name = instruction[1]
        value = self.stack.pop()
        self.variables[var_name] = value

    def print_operation(self, instruction):
        num_values = int(instruction[1])
        values = [self.stack.pop() for _ in range(num_values)]
        print(*reversed(values))

    def read_operation(self, instruction):
        value_type = instruction[1]
        if value_type == 'I':
            value = int(input("Enter an integer: "))
        elif value_type == 'F':
            value = float(input("Enter a float: "))
        elif value_type == 'S':
            value = input("Enter a string: ")
        elif value_type == 'B':
            value = input("Enter a boolean (true/false): ").lower() == 'true'
        self.stack.append(value)