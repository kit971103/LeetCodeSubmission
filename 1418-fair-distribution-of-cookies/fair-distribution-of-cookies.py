class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        if n == k: return max(cookies)
        if n == k+1: 
            cookies.sort()
            return max(cookies[0] + cookies[1], cookies[-1])
        
        min_unfairness = sum(cookies)

        for base_case in itertools.combinations(range(n), k):

            remainning_cookies = [cookies[i] for i in range(n) if i not in base_case]
            base_case = [ cookies[i] for i in base_case ]

            for distribution in itertools.product( range(k) , repeat = n-k ):
                
                children = base_case.copy()
                for i, cookiesLabel in enumerate(distribution):  children[cookiesLabel] += remainning_cookies[i]
                
                unfairness = max(children)
                if unfairness < min_unfairness : min_unfairness = unfairness


            print()
                
        return min_unfairness