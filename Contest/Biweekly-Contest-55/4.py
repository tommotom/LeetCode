from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.shops = defaultdict(SortedList)
        self.shop_movie = {}
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.shops[movie].add((price, shop))
            self.shop_movie[shop, movie] = price

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.shops[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].remove((price, shop))
        self.rented.add((price, shop, movie))


    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie[shop, movie]
        self.shops[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
