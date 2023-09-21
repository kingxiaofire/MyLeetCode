from operator import add, sub, mul

class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x/y)}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))
        return stack.pop()