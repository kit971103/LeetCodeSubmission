class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def sorce(pass_, total):
            return -(total - pass_)/(total*(total+1))
            # return pass_/total

        heap = [[sorce(pass_n, total_n), pass_n, total_n] for pass_n, total_n in classes]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            hiest_imporvemtn = heapq.heappop(heap)
            hiest_imporvemtn[1] += 1
            hiest_imporvemtn[2] += 1
            hiest_imporvemtn[0] = sorce(hiest_imporvemtn[1], hiest_imporvemtn[2])
            heapq.heappush(heap, hiest_imporvemtn)
        
        return sum(pass_/total for _,pass_ ,total in heap)/len(heap)





        