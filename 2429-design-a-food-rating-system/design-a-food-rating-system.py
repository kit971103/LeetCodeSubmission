class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # if not(len(foods) == len(cuisines) == len(ratings)):
        #     raise Exception(f"Not same length {len(foods)=}, {len(cuisines)=}, {len(ratings)=}")
        
        self.mapper = dict() #see https://docs.python.org/3/library/heapq.html, about Priority Queue Implementation.
        self.priority_queue = defaultdict(list)
        for item in zip(foods, cuisines, ratings):
            self._additem(*item)

    def _additem(self, food, cuisine, rating):
        entry = [-rating, food, False]
        self.mapper[food] = (entry, cuisine)
        heapq.heappush(self.priority_queue[cuisine], entry)

    def changeRating(self, food: str, newRating: int) -> None:
        entry, cuisine = self.mapper[food]
        entry[2] = True
        self._additem(food, cuisine, newRating)

    def highestRated(self, cuisine: str) -> str:
        while self.priority_queue[cuisine][0][2]:
            heapq.heappop(self.priority_queue[cuisine])
        return self.priority_queue[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)