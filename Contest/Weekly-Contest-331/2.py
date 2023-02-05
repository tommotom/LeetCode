class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'i', 'u', 'e', 'o'])

        cum = [0]
        for word in words:
            cum.append(cum[-1])
            if word[0] in vowels and word[-1] in vowels:
                cum[-1] += 1
        cum = cum[1:]

        ans = []
        for l, r in queries:
            ans.append(cum[r] - (cum[l-1] if l > 0 else 0))

        return ans
