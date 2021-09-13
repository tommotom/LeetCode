class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        for char in text:
            counter[char] += 1
        return min(counter["b"], counter["a"], counter["l"]//2, counter["o"]//2, counter["n"])
