class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in itertools.zip_longest(itertools.chain(*word1), itertools.chain(*word2)):
            if c1!=c2: 
                return False
        return True
        