class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def distribute_ith_cookie(i):
            nonlocal min_unfairness
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(children))
                return
            if len(children) < k:
                children.append( cookies[i] )
                distribute_ith_cookie(i+1)
                children.pop()
            for j in range(len(children)):
                children[j] += cookies[i]
                distribute_ith_cookie(i+1)
                children[j] -= cookies[i]

        children = []
        min_unfairness = sum(cookies)
        distribute_ith_cookie(0)

        return min_unfairness