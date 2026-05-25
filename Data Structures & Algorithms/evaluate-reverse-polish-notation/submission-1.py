class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:               
            if token == '+':
                a,b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif token == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif token == '*':
                a,b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif token == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a)) # the order of the inputs
            else: stack.append(int(token)) # the given input is string, make sure to convert to int.             
        return stack[0]