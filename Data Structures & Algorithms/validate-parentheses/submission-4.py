class Solution:
    def push(self, stack, x):
        return stack.append(x)

    def pop(self, stack):
        if stack:
            return stack.pop()
        else:
            return 'invalid'

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                self.push(stack, char)
            else:
                if not stack:
                    return False
                else:
                    if (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']'):
                        self.pop(stack)
                    else:
                        return False
        if stack:
            return False
        else:
            return True
        