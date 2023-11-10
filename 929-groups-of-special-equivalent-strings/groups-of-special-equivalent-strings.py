class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        aset = set()
        for string in words:
            even = []
            odd = []
            for i, c in enumerate(string):
                if i%2: odd.append(c)
                else: even.append(c)
            even.sort()
            odd.sort()
            signature = "".join(even) + "-" + "".join(odd)
            aset.add(signature)
        return len(aset)

        