class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        oneFlips = 0
        zeroFlips = s.count("0")

        result = zeroFlips

        for c in s:
            oneFlips += c == "1"
            zeroFlips -= c == "0"
            result = min(result, oneFlips + zeroFlips)

        return result
