class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_location = defaultdict(list)
        for i, c in enumerate(s): 
            char_location[c].append(i)

        res = 0
        for p_c, p_location in char_location.items():
            if len(p_location) < 2: continue
            for mid_c, mid_location in char_location.items():
                if bisect_left(mid_location, p_location[0]) < bisect_left(mid_location, p_location[-1]):
                    res+=1
            if len(p_location) == 2: res -= 1
        return res

        

        