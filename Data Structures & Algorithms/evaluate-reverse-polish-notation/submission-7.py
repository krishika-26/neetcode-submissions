class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [ ]
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    result = a + b
                    stack.append(result)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    result = a * b
                    stack.append(result)
                elif i =='-':
                    a = stack.pop()
                    b = stack.pop()
                    result = b - a
                    stack.append(result)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    result = int(b / a)
                    stack.append(result)
        return stack.pop()

        
        