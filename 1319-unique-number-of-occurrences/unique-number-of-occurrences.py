class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        seen = set()
        for val in count.values():
            if val in seen:
                return False
            seen.add(val)
        return True
        