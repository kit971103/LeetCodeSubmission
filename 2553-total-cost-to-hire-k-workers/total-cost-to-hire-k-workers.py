class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates >= len(costs)/2:
            costs.sort()
            return sum(costs[:k])
        
        res = 0
        minheap = [(n, 0) for n in costs[:candidates]] + [(n, 1) for n in costs[-candidates:]]
        heapq.heapify(minheap)
        l, r = candidates, len(costs)-candidates-1
        
        for _ in range(k):

            n, L_bool = heapq.heappop(minheap)
            res += n

            if l > r:
                continue
            if L_bool:
                heapq.heappush(minheap, (costs[r], 1) )
                r-=1
            else:
                heapq.heappush(minheap, (costs[l], 0) )
                l+=1
        
        return res

