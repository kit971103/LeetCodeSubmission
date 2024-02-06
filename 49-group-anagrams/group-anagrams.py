class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            seen["".join(sorted(s))].append(s)
        return list(seen.values())
