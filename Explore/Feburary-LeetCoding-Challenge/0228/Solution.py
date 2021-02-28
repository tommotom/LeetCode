from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.counter = defaultdict(lambda:0)
        self.stack = defaultdict(list)
        self.freq = []

    def push(self, x: int) -> None:
        self.counter[x] += 1
        self.stack[self.counter[x]].append(x)
        heapq.heappush(self.freq, -self.counter[x])

    def pop(self) -> int:
        freq = -heapq.heappop(self.freq)
        x = self.stack[freq].pop()
        if len(self.stack[freq]) == 0: del self.stack[freq]
        self.counter[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
