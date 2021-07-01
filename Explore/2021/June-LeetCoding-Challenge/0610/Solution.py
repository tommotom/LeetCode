class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        l, r = 0, len(self.books)
        while l < r:
            m = (l + r) // 2
            if self.books[m][0] < start:
                l = m + 1
            else:
                r = m

        if not self.books:
            pass
        elif l == len(self.books):
            if not self.books[l-1][1] <= start:
                return False
        elif l == 0:
            if not end <= self.books[l][0]:
                return False
        elif 0 < l < len(self.books):
            if not (self.books[l-1][1] <= start and end <= self.books[l][0]):
                return False

        self.books.insert(l, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)