class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # if not(len(foods) == len(cuisines) == len(ratings)):
        #     raise Exception(f"Not same length {len(foods)=}, {len(cuisines)=}, {len(ratings)=}")
        
        self.mapper = dict() #see https://docs.python.org/3/library/heapq.html, about Priority Queue Implementation.
        self.priority_queue = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            entry = [-rating, food, False]
            self.mapper[food] = (entry, cuisine)
            self.priority_queue[cuisine].append(entry)
        
        for cuisine in self.priority_queue:
            heapq.heapify(self.priority_queue[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        entry, cuisine = self.mapper[food]
        entry[2] = True
        newentry = [-newRating, food, False]
        self.mapper[food] = (newentry, cuisine)
        heapq.heappush(self.priority_queue[cuisine], newentry)

    def highestRated(self, cuisine: str) -> str:
        while self.priority_queue[cuisine][0][2]:
            heapq.heappop(self.priority_queue[cuisine])
        return self.priority_queue[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)