class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        avablerow = set([0])
        total = 0
        res = []
        while avablerow:
            
            avablerow_iter = sorted(avablerow, reverse = True)
            
            for row in avablerow_iter:
                col = total - row
                if col >= len(nums[row]):
                    avablerow.remove(row)
                else:
                    res.append(nums[row][col])
            total += 1
            if total < len(nums): avablerow.add(total)
        return res


