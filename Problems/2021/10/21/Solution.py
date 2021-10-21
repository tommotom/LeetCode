import random

class RandomizedSet:

    def __init__(self):
        self.elements = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.elements)
        self.elements.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        idx = self.indices[val]
        if idx != len(self.elements)-1:
            self.indices[self.elements[-1]] = idx
            self.elements[idx], self.elements[-1] = self.elements[-1], self.elements[idx]

        self.elements.pop()
        del self.indices[val]

        return True


    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
