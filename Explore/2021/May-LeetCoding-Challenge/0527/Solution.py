class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = [(len(word), set(word)) for word in words]
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i][1].isdisjoint(words[j][1]):
                    ans = max(ans, words[i][0] * words[j][0])
        return ans
