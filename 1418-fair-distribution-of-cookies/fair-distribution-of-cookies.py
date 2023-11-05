class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if n == k: return max(cookies)
        if n == k+1: 
            cookies.sort()
            return max(cookies[0] + cookies[1], cookies[-1])
        
        def distribute_ith_cookie(i):
            nonlocal min_unfairness
            if i == n:
                min_unfairness = min(min_unfairness, max(children))
                return
            if len(children) < k:
                children.append( cookies[i] )
                distribute_ith_cookie(i+1)
                children.pop()
            for j in range(len(children)):
                children[j] += cookies[i]
                # if children[j] >= min_unfairness:
                #     children[j] -= cookies[i]
                #     return
                distribute_ith_cookie(i+1)
                children[j] -= cookies[i]

        children = []
        min_unfairness = sum(cookies)
        distribute_ith_cookie(0)

        return min_unfairness