class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O'])
        half = len(s) // 2
        a = b = 0
        for c in s[:half]:
            if c in vowels: a += 1
        for c in s[half:]:
            if c in vowels: b += 1
        return a == b
