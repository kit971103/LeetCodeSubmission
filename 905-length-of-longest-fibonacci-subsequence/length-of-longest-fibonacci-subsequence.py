class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 2
        quick_check = set(arr)
        for i in range(len(arr)):
            for ii in range(i+1, len(arr)):
                x0 = arr[i]
                x1 = arr[ii]
                length = 2
                while (x0+x1) in quick_check:
                    x0, x1 = x1, x0+x1
                    length+=1
                
                if length > res:
                    res = length
        
        return res if res > 2 else 0




        