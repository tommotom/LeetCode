class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = ""
        mutating = False
        for i, n in enumerate(num):
            if not mutating:
                if n < str(change[int(n)]):
                    mutating = True
                    ans += str(change[int(n)])
                else:
                    ans += n
            elif mutating:
                if n > str(change[int(n)]):
                    ans += num[i:]
                    break
                else:
                    ans += str(change[int(n)])
        return ans
