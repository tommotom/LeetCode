class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(['a', 'i', 'u', 'e', 'o'])
        n = len(word)
        dp = [0 for _ in range(n)]
        for i, w in enumerate(word):
            if i == 0:
                if w in vowels:
                    dp[i] = 1
                else:
                    dp[i] = 0
            else:
                if w in vowels:
                    dp[i] = dp[i-1] + i + 1
                else:
                    dp[i] = dp[i-1]
        return sum(dp)
