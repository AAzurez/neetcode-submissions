import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            }
        def operation_func(a,b):
            return operation_func(a, b)

        stack = []

        for token in tokens:
            if token not in operator_map:
                stack.append(token)
            else:
                op = operator_map[token]

                second = int(stack.pop())
                first = int(stack.pop())

                curr = op(first, second)
                stack.append(curr)
        return int(stack[0])