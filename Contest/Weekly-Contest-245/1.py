class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counter = defaultdict(int)
        for word in words:
            for c in word:
                counter[c] += 1

        n = len(words)
        for v in counter.values():
            if not v % n == 0: return False
        return True
