class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows-1):
            this = [1]
            for a,b in itertools.pairwise(ans[-1]):
                this.append(a+b)
            this.append(1)
            ans.append(this)
        return ans