class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        ans = float('inf')
        for i, c in enumerate(cards):
            if c in seen:
                ans = min(ans, i - seen[c] + 1)
            seen[c] = i
        return ans if ans != float('inf') else -1
