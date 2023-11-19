class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = sorted(Counter(nums).items(), reverse = True)
        print(count)
        acc = 0
        res = 0
        for val, freq in count:
            acc += freq
            res += acc
        res -= acc
        return res

