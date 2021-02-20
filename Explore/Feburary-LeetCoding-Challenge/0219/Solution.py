class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = right = 0
        arr = []
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == right: continue
                right += 1
            arr.append(c)

        left = right = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] == ")":
                right += 1
            elif arr[i] == "(":
                if left == right: arr[i] = ""
                else: left += 1

        return "".join(arr)
