class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        return len(set( "".join(sorted(string[::2])) + "".join(sorted(string[1::2])) for string in words))

        