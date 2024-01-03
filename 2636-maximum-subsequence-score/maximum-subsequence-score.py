class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = total = 0
        heap = []
        for n2, n1 in sorted(zip(nums2, nums1), reverse=True):
            total += n1
            heapq.heappush(heap, n1)
            if len(heap) == k:
                res = max(res, total*n2)
                total-=heapq.heappop(heap)
        return res

        


        


        