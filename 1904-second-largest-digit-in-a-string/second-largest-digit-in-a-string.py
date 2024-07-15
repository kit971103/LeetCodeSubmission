class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set(filter(lambda c: c.isdigit(), s))
        return sorted(map(int, nums))[-2] if len(nums) >= 2 else -1

                
        