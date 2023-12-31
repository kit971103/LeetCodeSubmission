class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter(itertools.chain.from_iterable(words))
        n = len(words)
        if count.total()%n:
            return False
        for c in count:
            if count[c]%n:
                return False
        return True