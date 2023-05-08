class FrequencyTracker:

    def __init__(self):
        self.counter = defaultdict(int)
        self.freqs = defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.counter:
            self.freqs[self.counter[number]] -= 1
            if self.freqs[self.counter[number]] == 0:
                del self.freqs[self.counter[number]]
        self.counter[number] += 1
        self.freqs[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if not number in self.counter: return
        self.freqs[self.counter[number]] -= 1
        if self.freqs[self.counter[number]] == 0:
            del self.freqs[self.counter[number]]
        self.counter[number] -= 1
        if self.counter[number] == 0:
            del self.counter[number]
        elif self.counter[number] > 0:
            self.freqs[self.counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freqs


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
