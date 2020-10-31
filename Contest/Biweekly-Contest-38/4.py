from _collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        word_len, target_len = len(words[0]), len(target)

        counter = {}
        for i in range(word_len):
            counter[i] = defaultdict(lambda :0)
            for word in words: counter[i][word[i]] += 1

        dp = [[0] * word_len for _ in range(target_len)]

        dp[0][0] = counter[0][target[0]] % (10**9 + 7)
        for j in range(1, word_len):
            dp[0][j] = (dp[0][j-1] + counter[j][target[0]]) % (10**9 + 7)

        for i in range(1, target_len):
            prev = dp[i-1][i-1]
            dp[i][i] = (counter[i][target[i]] * prev) % (10**9 + 7)
            for j in range(i+1, word_len):
                prev = dp[i-1][j-1]
                count = counter[j][target[i]]
                dp[i][j] = (count * prev + dp[i][j-1]) % (10**9 + 7)

        return dp[-1][-1]
