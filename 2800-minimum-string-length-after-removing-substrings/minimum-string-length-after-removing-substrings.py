class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char == "A" or char == "C": stack.append(char)
            elif stack and (char == "B" or char == "D"):
                if (stack[-1] == "A" and char == "B") or (stack[-1] == "C" and char == "D"): 
                    count+=1
                    stack.pop()
                else: stack.clear()
            else: stack.clear()
        return len(s) - 2*count
        