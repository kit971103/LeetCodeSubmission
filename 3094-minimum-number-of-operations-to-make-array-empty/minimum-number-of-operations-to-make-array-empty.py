class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum( (f+2)//3 for f in fs) if all(map(lambda x: x>1, fs:=Counter(nums).values())) else -1

        