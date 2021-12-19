class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = j = 0
        arr = []
        while i < len(s):
            if j < len(spaces) and i == spaces[j]:
                arr.append(" ")
                j += 1
            arr.append(s[i])
            i += 1
        return "".join(arr)
