class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # count = Counter(nums):
        # sort_items = sorted(count.items())
        # max_freq = sort_items[0][1]

        # for n, freq in sort_items:
        nums.sort()
        n = len(nums)
        l = r = area = 0
        h = nums[0]
        res = 1

        while r < n:
            h = nums[r]
            area += h
            while area + k < (r-l+1)*h and l < r: 
                area -= nums[l]
                l+=1
            if r-l+1 > res: res = r-l+1
            r+=1
        return res




        