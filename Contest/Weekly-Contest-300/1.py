class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dic = {}
        c = 0
        for char in key:
            if char == ' ': continue
            if char in dic: continue
            dic[char] = chr(c+ord('a'))
            c += 1

        ans = []
        for char in message:
            if char == ' ': ans.append(char)
            else: ans.append(dic[char])

        return "".join(ans)
