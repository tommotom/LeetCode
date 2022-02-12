class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isSameCount(c1, c2):
            for k, c in c1.items():
                if k not in c2: return False
                if c2[k] != c: return False
            return True

        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        for c in s2[:len(s1)]:
            s2_counter[c] += 1

        if isSameCount(s1_counter, s2_counter): return True

        for i in range(len(s1), len(s2)):
            s2_counter[s2[i-len(s1)]] -= 1
            s2_counter[s2[i]] += 1
            if isSameCount(s1_counter, s2_counter): return True
        return False
