class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = 0
        converted = ""
        for c in s:
            converted += str(ord(c) - ord("a") + 1)
        for _ in range(k):
            tmp = 0
            for num in converted:
                tmp += int(num)
            converted = str(tmp)
        return int(converted)
