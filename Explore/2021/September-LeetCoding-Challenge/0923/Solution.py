class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2: return ""
        palindrome = list(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i] != "a" and not (len(palindrome) % 2 == 1 and i * 2 + 1 == len(palindrome)):
                palindrome[i] = "a"
                return "".join(palindrome)

        for i in range(len(palindrome)-1, -1, -1):
            if palindrome[i] == "a" and not (len(palindrome) % 2 == 1 and i * 2 + 1 == len(palindrome)):
                palindrome[i] = "b"
                return "".join(palindrome)
