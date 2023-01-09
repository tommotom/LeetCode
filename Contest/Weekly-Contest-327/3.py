class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        if len(c1) < len(c2): c1, c2 = c2, c1


        def dec(c1, w):
            return c1[w] == 1

        def inc(c2, w):
            return w not in c2

        if len(c1) == len(c2):
            for w1, v1 in c1.items():
                for w2, v2 in c2.items():
                    if w1 == w2: return True
                    diff = dec(c1, w1) - dec(c2, w2) + inc(c2, w1) - inc(c1, w2)
                    if diff == 0: return True

        for w1, v1 in c1.items():
            for w2, v2 in c2.items():
                if w1 == w2: continue
                diff = dec(c1, w1) - dec(c2, w2) + inc(c2, w1) - inc(c1, w2)
                if diff == len(c1) - len(c2): return True

        return False
