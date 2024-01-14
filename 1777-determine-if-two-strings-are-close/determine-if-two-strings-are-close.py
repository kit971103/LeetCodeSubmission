class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        
        set1=set(word1)
        set2=set(word2)
        if set1 != set2: return False

        l1=[]
        l2=[]
        for c in set1:
            l1.append(word1.count(c))
            l2.append(word2.count(c))

        return sorted(l1) == sorted(l2)