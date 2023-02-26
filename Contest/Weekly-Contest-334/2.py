class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        s, mod = 0, 1000000007
        for w in list(word):
            s = s * 10 + int(w)
            ans.append(1 if s % m == 0 else 0)
            s %= m
        return ans
