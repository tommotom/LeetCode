class Solution:
    def finalString(self, s: str) -> str:
        arr = []
        for c in s:
            if c == "i":
                arr = arr[::-1]
            else:
                arr.append(c)
        return "".join(arr)
