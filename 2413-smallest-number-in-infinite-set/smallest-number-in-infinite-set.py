class SmallestInfiniteSet:

    def __init__(self):
        self.lowerbouind = 1
        self.heap = []
        
    def popSmallest(self) -> int:
        if self.heap : 
            return heapq.heappop(self.heap)
        else:
            self.lowerbouind +=1
            return self.lowerbouind -1
        

    def addBack(self, num: int) -> None:
        if num < self.lowerbouind and num not in self.heap: #O(n) membership test
            heapq.heappush(self.heap, num)
        return None
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)