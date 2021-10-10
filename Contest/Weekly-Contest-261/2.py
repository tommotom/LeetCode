class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        target = mean * (m+n) - sum(rolls)
        ans = []
        while n > 0:
            for num in range(6, 1, -1):
                if target - num >= n-1:
                    target -= num
                    ans.append(num)
                    break
            else:
                target -= n
                ans += [1] * n
                break
            n -= 1
        return ans if target == 0 else []
