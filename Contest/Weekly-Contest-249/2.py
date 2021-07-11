class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        counter = [[0] * 26 for _ in range(len(s))]
        min_idx = [-1] * 26
        max_idx = [-1] * 26
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            if min_idx[idx] == -1: min_idx[idx] = i
            max_idx[idx] = max(max_idx[idx], i)

            if i > 0:
                for j in range(26):
                    counter[i][j] = counter[i-1][j]
            counter[i][idx] += 1

        ans = 0
        for i in range(26):
            m, M = min_idx[i], max_idx[i]
            if m == -1 or m == M or m+1 == M: continue
            for j in range(26):
                if counter[M-1][j] > counter[m][j]: ans += 1
        return ans
