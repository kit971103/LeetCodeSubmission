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
                #clear the stack as it cant connectto others
                if not stack:
                    continue
                if x >= y:
                    # all "ab" should have been handeled above, only handle "ba" here
                    total += y * min(stack.count("a"), stack.count("b"))
                else:
                    total += x * min(stack.count("a"), stack.count("b"))
                stack.clear()
        if x >= y:
            # all "ab" should have been handeled above, only handle "ba" here
            total += y * min(stack.count("a"), stack.count("b"))
        else:
            total += x * min(stack.count("a"), stack.count("b"))


        return total