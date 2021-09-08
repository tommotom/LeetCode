class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2, -1, -1):
            shifts[i] += shifts[i+1]
        return "".join([chr((ord(c)+shifts[i]-ord('a'))%26 + ord('a')) for i, c in enumerate(s)])
