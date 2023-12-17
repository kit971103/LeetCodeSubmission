class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # if not(len(foods) == len(cuisines) == len(ratings)):
        #     raise Exception(f"Not same length {len(foods)=}, {len(cuisines)=}, {len(ratings)=}")
        
        self.mapper = dict() #see https://docs.python.org/3/library/heapq.html, about Priority Queue Implementation.
        self.priority_queue = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.mapper[food] = [-rating, cuisine]
            heapq.heappush(self.priority_queue[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating, cuisine = self.mapper[food]
        self.mapper[food][0] = -newRating
        heapq.heappush(self.priority_queue[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.priority_queue[cuisine][0][0] !=  self.mapper[ self.priority_queue[cuisine][0][1] ][0]:
            heapq.heappop(self.priority_queue[cuisine])
        return self.priority_queue[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)