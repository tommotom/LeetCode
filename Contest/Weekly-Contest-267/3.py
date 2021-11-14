class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        ans = []
        for col in range(cols):
            c = col
            r = 0
            while r < rows and c < cols:
                i = c+r*cols
                ans.append(encodedText[i])
                c += 1
                r += 1

        return "".join(ans).rstrip()