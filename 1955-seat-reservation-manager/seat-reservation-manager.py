class SeatManager:

    def __init__(self, n: int):
        self.freeseaat = []
        self.reservation_number = 0

    def reserve(self) -> int:
        if self.freeseaat:
            return heapq.heappop(self.freeseaat)
        else:
            self.reservation_number += 1
            return self.reservation_number

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.freeseaat, seatNumber)