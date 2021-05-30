class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = 0
        for i, w in enumerate(firstWord):
            first += (ord(w) - ord('a')) * 10 ** (len(firstWord)-i-1)
        second = 0
        for i, w in enumerate(secondWord):
            second += (ord(w) - ord('a')) * 10 ** (len(secondWord)-i-1)
        target = 0
        for i, w in enumerate(targetWord):
            target += (ord(w) - ord('a')) * 10 ** (len(targetWord)-i-1)
        return first + second == target
