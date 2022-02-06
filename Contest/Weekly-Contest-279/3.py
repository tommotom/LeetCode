class Bitset:

    def __init__(self, size: int):
        self.arr = [0 for _ in range(size)]
        self.flipped = False
        self.zeros = size
        self.ones = 0

    def toZero(self, idx):
        if self.arr[idx] == 0:
            return
        self.zeros += 1
        self.ones -= 1
        self.arr[idx] = 0

    def toOne(self, idx):
        if self.arr[idx] == 1:
            return
        self.zeros -= 1
        self.ones += 1
        self.arr[idx] = 1

    def fix(self, idx: int) -> None:
        if self.flipped:
            self.toZero(idx)
        else:
            self.toOne(idx)

    def unfix(self, idx: int) -> None:
        if self.flipped:
            self.toOne(idx)
        else:
            self.toZero(idx)

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        if self.flipped:
            return self.zeros == len(self.arr)
        else:
            return self.ones == len(self.arr)

    def one(self) -> bool:
        if self.flipped:
            return self.zeros > 0
        else:
            return self.ones > 0

    def count(self) -> int:
        if self.flipped:
            return self.zeros
        else:
            return self.ones

    def toString(self) -> str:
        if self.flipped:
            return ''.join(map(str, [b^1 for b in self.arr]))
        else:
            return ''.join(map(str, self.arr))


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
