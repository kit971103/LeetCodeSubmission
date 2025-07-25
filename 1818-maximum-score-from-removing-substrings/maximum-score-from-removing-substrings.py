class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0
        stack = []
        for c in s:
            if c in "ab":
                # case where we have contious ab
                if not stack:
                    stack.append(c)
                elif x >= y and stack[-1] == "a" and c == "b":
                    total += x
                    stack.pop()
                elif y > x and stack[-1] == "b" and c == "a":
                    total += y
                    stack.pop()
                else:
                    stack.append(c)
            else:
                total += min(stack.count("a"), stack.count("b")) * min(x, y)
                stack.clear()
        total += min(stack.count("a"), stack.count("b")) * min(x, y)

        return total
