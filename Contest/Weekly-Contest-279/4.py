class Solution:
    def minimumTime(self, s: str) -> int:
        left = [0 for _ in range(len(s)+1)]
        for i in range(len(s)):
            if s[i] == "1":
                left[i+1] = min(left[i]+2, i+1)
            else:
                left[i+1] = left[i]

        right = [0 for _ in range(len(s)+1)]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                right[i] = min(right[i+1]+2, len(s)-i)
            else:
                right[i] = right[i+1]

        return min(left[i] + right[i] for i in range(len(s)+1))
