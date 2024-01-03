class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates >= len(costs)/2:
            costs.sort()
            return sum(costs[:k])
        
        res = 0
        minheap = []
        l, r = candidates, len(costs)-candidates-1
        
        for i in range(candidates):
            minheap.append( (costs[i], 0) )
            minheap.append( (costs[-i-1], 1) )
        
        heapq.heapify(minheap)
        
        for _ in range(k):

            n, L_bool = heapq.heappop(minheap)
            res += n

            if l > r:
                continue
            if L_bool == 0:
                heapq.heappush(minheap, (costs[l], 0) )
                l+=1
            else:
                heapq.heappush(minheap, (costs[r], 1) )
                r-=1

        return res

                
