class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = Counter()
        for word in words:
            count.update(word)

        n = len(words)
        if count.total()%n:
            return False
        for c in count:
            if count[c]%n:
                return False
        return True