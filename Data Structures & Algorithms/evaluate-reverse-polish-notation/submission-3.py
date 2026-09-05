class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in ['+', '-', '*', '/']:
                stack.append(char)
            else:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                else:
                    stack.append(operand1/operand2)
        result = int(stack[-1])
        return result
                    