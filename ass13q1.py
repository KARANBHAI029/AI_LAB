class SymbolLogic:
    def __init__(self, postfix_expression, readable_name):
        self.postfix_expression = postfix_expression
        self.readable_name = readable_name
        self.variables = []
        for char in self.postfix_expression:
            if char.isalpha() and char not in self.variables:
                self.variables.append(char)
        self.variables.sort()

    def evaluate_stack(self, truth_values):
        stack = []
        for char in self.postfix_expression:
            if char.isalpha():
                stack.append(truth_values[char])
            elif char == '~':
                val = stack.pop()
                stack.append(not val)
            else:
                right = stack.pop()
                left = stack.pop()
                if char == '&':
                    stack.append(left and right)
                elif char == '|':
                    stack.append(left or right)
                elif char == '>':
                    stack.append((not left) or right)
                elif char == '=':
                    stack.append(left == right)
        return stack.pop()

    def print_truth_table(self):
        print(f"\nTruth Table for: {self.readable_name}")
        headers = []
        for var in self.variables:
            headers.append(f'"{var}"')
        headers.append(f'"{self.readable_name}"')
        print(",".join(headers))
        
        num_vars = len(self.variables)
        total_rows = 2 ** num_vars
        
        for i in range(total_rows):
            binary_str = bin(i)[2:].zfill(num_vars)
            truth_values = {}
            for j in range(num_vars):
                truth_values[self.variables[j]] = (binary_str[j] == '1')
            
            result = self.evaluate_stack(truth_values)
            row = []
            for var in self.variables:
                row.append('"T"' if truth_values[var] else '"F"')
            row.append('"T"' if result else '"F"')
            print(",".join(row))

if __name__ == "__main__":
    q1 = SymbolLogic("P~Q>", "~P -> Q")
    q1.print_truth_table()

    q2 = SymbolLogic("P~Q~&", "-P ^ -Q")
    q2.print_truth_table()

    q3 = SymbolLogic("PQ~|", "P v -Q")
    q3.print_truth_table()

    q4 = SymbolLogic("P~Q>", "-P -> Q")
    q4.print_truth_table()

    q5 = SymbolLogic("P~Q~=", "-P <-> -Q")
    q5.print_truth_table()

    q6 = SymbolLogic("PQ|P~Q>&", "(P v Q) ^ (-P -> Q)")
    q6.print_truth_table()

    q7 = SymbolLogic("PQ|R~>", "((P v Q) -> -R)")
    q7.print_truth_table()

    q8 = SymbolLogic("PQ|R~>P~Q~&R~>=", "(((P v Q) -> -R) <-> ((-P ^ -Q) -> -R))")
    q8.print_truth_table()

    q9 = SymbolLogic("PQ>QR>&QR>>", "(((P -> Q) ^ (Q -> R)) -> (Q -> R))")
    q9.print_truth_table()

    q10 = SymbolLogic("PQR|>P~Q~&R~&>", "(((P -> (Q v R)) -> (-P ^ -Q ^ -R)))")
    q10.print_truth_table()