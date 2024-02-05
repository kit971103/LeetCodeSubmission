class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uni=set()
        seen=set()

        for c in s:
            if c not in seen:
                if c not in uni: uni.add(c)
                else: 
                    uni.discard(c)
                    seen.add(c)
        
        if len(uni)==0: return -1
        for i, c in enumerate(s):
            if c in uni: return i