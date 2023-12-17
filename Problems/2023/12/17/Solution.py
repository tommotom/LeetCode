class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.q = defaultdict(list)
        self.r = {}
        self.f_to_c = {}
        for f, c, r in zip(foods, cuisines, ratings):
            heapq.heappush(self.q[c], (-r, f))
            self.r[f] = r
            self.f_to_c[f] = c

    def changeRating(self, food: str, newRating: int) -> None:
        self.r[food] = newRating
        heapq.heappush(self.q[self.f_to_c[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        r, f = self.q[cuisine][0]
        while -r != self.r[f]:
            heapq.heappop(self.q[cuisine])
            r, f = self.q[cuisine][0]
        return f


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
