class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s)//2], s[len(s)//2:]
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        a_count = 0
        for c in a:
            if c in vowels: a_count += 1

        b_count = 0
        for c in b:
            if c in vowels: b_count += 1

        return a_count == b_count
