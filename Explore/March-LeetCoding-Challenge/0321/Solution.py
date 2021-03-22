from collections import Counter

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        target = Counter(str(N))

        n = 0

        while len(str(N)) > len(str(2 ** n)):
            n += 1

        while len(str(N)) == len(str(2 ** n)):
            digits = Counter(str(2 ** n))
            if set(target.keys()) == set(digits.keys()):
                for d, c in digits.items():
                    if c != target[d]: break
                else: return True
            n += 1

        return False
