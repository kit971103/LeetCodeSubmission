class Solution:
    def maxScore(self, s: str) -> int:
        left_zero = 1 if s[0] is "0" else 0
        right_one = s.count("1") - 1 + left_zero
        res = 0
        for c in itertools.islice(s,1, None):
            res = max(res, left_zero+right_one)
            if c == "1":
                right_one-=1
            else:
                left_zero+=1
        return res
        