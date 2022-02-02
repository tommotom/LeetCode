class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []

        def isAnagram(c1, c2):
            for key in c1:
                if key not in c2 or c1[key] != c2[key]: return False
            return True


        pc = Counter(p)
        sc = defaultdict(int)
        for i in range(len(p)):
            sc[s[i]] += 1

        ans = []
        if isAnagram(pc, sc): ans.append(0)

        for i in range(len(p), len(s)):
            sc[s[i]] += 1
            sc[s[i-len(p)]] -= 1
            if isAnagram(pc, sc): ans.append(i-len(p)+1)

        return ans
