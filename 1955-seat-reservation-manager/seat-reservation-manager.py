class SeatManager:

    def __init__(self, n: int):
        # self.reservation = [Flase] * n
        self.freeseaat = []
        self.reservation_number = 0
        self.max_reservation = n
        

    def reserve(self) -> int:
        if self.freeseaat:
            return heapq.heappop(self.freeseaat)
        elif self.reservation_number < self.max_reservation:
            self.reservation_number += 1
            return self.reservation_number
        else:
            return -1
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.freeseaat, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)