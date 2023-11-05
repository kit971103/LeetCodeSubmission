class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        if n == k: return max(cookies)
        if n == k+1: 
            cookies.sort()
            return max(cookies[0] + cookies[1], cookies[-1])
        
        min_unfairness = sum(cookies)

        for base_case in itertools.combinations(range(n), k):

            remainning_cookies = [ i for i in range(n) if i not in base_case]

            for distribution in itertools.product( range(k) , repeat = n-k ):
                
                children = [ cookies[cookies_index1] + sum([ cookies[ remainning_cookies[cookies_index2] ] for cookies_index2 ,child_index2 in enumerate(distribution) if child_index2 ==  child_index1]) for child_index1, cookies_index1 in enumerate(base_case)]

                unfairness = max(children)
                if unfairness < min_unfairness : min_unfairness = unfairness
                
        return min_unfairness