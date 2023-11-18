class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        # res = []
        # for n in count:
        #     if count[n] == 1 and n-1 noy in count and n+1 not in count: res.append(n)

        # return res
        return [ n for n in count if count[n] == 1 and n-1 not in count and n+1 not in count]
        