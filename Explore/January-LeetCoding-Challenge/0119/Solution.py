class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(left, right):
            if right == len(s) or not s[left] == s[right]: return 0

            while 0 < left and right < len(s) - 1 and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            return right - left + 1

        start = end = 0

        for i in range(len(s)):
            odd = helper(i, i)
            even = helper(i, i+1)
            length = max(odd, even)
            if length > end - start + 1:
                start = i - (length-1) // 2
                end = i + length // 2
        return s[start:end+1]
