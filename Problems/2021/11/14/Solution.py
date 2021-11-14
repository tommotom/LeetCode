class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.indexes = [i for i in range(combinationLength)]
        self.deadend = [i + len(characters) - combinationLength for i in range(combinationLength)]

    def next(self) -> str:
        val = "".join(self.chars[i] for i in self.indexes)

        if self.indexes == self.deadend:
            self.indexes = None
        else:
            self.nextPerm()

        return val

    def hasNext(self) -> bool:
        return bool(self.indexes)

    def nextPerm(self):
        i = len(self.indexes) - 1
        self.indexes[i] += 1
        while i > 0 and self.indexes[i] >= len(self.chars) + i - len(self.indexes) + 1:
            self.indexes[i-1] += 1
            i -= 1

        i += 1
        while i < len(self.indexes):
            self.indexes[i] = self.indexes[i-1] + 1
            i += 1



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
