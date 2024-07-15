class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.t = timeToLive
        self.heap = []
        self.heap_map = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        item = [currentTime + self.t, tokenId]
        self.heap_map[tokenId] = item # if same tokenId is used, only keep the last map
        heapq.heappush(self.heap, item)
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.heap_map:
            return
        item = self.heap_map[tokenId]
        if item[0] > currentTime:
            item[0] = currentTime + self.t
            heapq.heapify(self.heap)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for item in self.heap if item[0] > currentTime)


        
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)