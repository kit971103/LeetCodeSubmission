class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def heap_key(pass_: int, total: int) -> float:
            return -(total - pass_)/(total*(total+1))
            # return pass_/total

        heap = [(heap_key(*class_), index) for index, class_ in enumerate(classes)]
        heapq.heapify(heap)
        
        for _ in range(extraStudents):
            _, class_to_added = heapq.heappop(heap)
            classes[class_to_added][0] += 1
            classes[class_to_added][1] += 1
            heap_item = heap_key(*classes[class_to_added]), class_to_added
            heapq.heappush(heap, heap_item)
        
        return sum(pass_/total for pass_ ,total in classes)/len(classes)





        