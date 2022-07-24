class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dic = defaultdict(list)
        self.ratings = {}
        self.foodToCuisine = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            heapq.heappush(self.dic[cuisine], (-rating, food))
            self.ratings[food] = rating
            self.foodToCuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        cuisine = self.foodToCuisine[food]
        heapq.heappush(self.dic[cuisine], (-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        food = self.dic[cuisine][0][1]
        while -self.dic[cuisine][0][0] != self.ratings[food]:
            heapq.heappop(self.dic[cuisine])
            food = self.dic[cuisine][0][1]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
