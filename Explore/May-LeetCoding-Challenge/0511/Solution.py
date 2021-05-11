class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = sum(cardPoints[:k]), 0
        ans = left
        for i in range(k-1, -1, -1):
            left -= cardPoints[i]
            right += cardPoints[-(k-i)]
            ans = max(ans, left + right)
        return ans
