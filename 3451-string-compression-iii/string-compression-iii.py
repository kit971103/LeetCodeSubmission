class Solution:
    def compressedString(self, word: str) -> str:
        result = []
        for c, group in itertools.groupby(word):
            length = len(list(group))
            result.extend(f"9{c}" for _ in range(length // 9))
            r = length % 9
            if r:
                result.append(f"{r}{c}")
        return "".join(result)