class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        mem = dict()
        res = []
        for left, right in queries:
            if (left, right) not in mem:
                ans = 0
                for n in range(left, right+1):
                    ans ^= arr[n]
                res.append(ans)
                mem[(left, right)] = ans
            else: res.append( mem[(left, right)] )
        return res


        