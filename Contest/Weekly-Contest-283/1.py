class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for alpha in range(ord(s[0]), ord(s[3])+1):
            for num in range(int(s[1]), int(s[4])+1):
                ans.append(chr(alpha) + str(num))
        return ans
