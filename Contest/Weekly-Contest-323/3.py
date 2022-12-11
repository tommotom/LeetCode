class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                count += 1
            else:
                count = 0

            if count == size:
                break
        else:
            return -1

        for j in range(i-count+1, i+1):
            self.memory[j] = mID

        return i-count+1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if (self.memory[i] == mID):
                self.memory[i] = 0
                count += 1
        return count

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
