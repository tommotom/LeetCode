class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        hot = "".join(el*(freq//k) for el, freq in Counter(s).items())

        substrings = set()
        for l in range(len(hot)+1):
            for comb in combinations(hot, l):
                for perm in permutations(comb):
                    substrings.add("".join(perm))

        substrings = sorted(substrings, key=lambda x: (len(x), x), reverse=True)
        print(substrings)
        for substring in substrings:
            if self.isSubsequence(substring*k, s):
                return substring

    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(char in t for char in s)
