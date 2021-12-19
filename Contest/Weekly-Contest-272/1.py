class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            return word and word == word[::-1]

        for word in words:
            if isPalindrome(word): return word
        return ""
