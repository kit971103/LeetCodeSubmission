operation = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for token in tokens:
            if token not in operation:
                stack.append(int(token))
            else:
                right = stack.pop()
                left  = stack.pop()
                stack.append(int(operation[token](left, right)))
        return stack[-1]