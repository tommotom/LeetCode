class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        length = 0
        current = "a"
        ans = 0
        for c in word:
            if current == "" and c == "a":
                current = c
                length += 1
            elif current == "a" and c == "e":
                current = c
                length += 1
            elif current == "e" and c == "i":
                current = c
                length += 1
            elif current == "i" and c == "o":
                current = c
                length += 1
            elif current == "o" and c == "u":
                current = c
                length += 1
            elif c == current:
                length += 1
            else:
                if c == "a":
                    current = c
                    length = 1
                else:
                    current = ""
                    length = 0
            if current == "u": ans = max(ans, length)
        if current == "u": ans = max(ans, length)
        return ans
