class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        cum = [candiesCount[0]]
        for i in range(1, len(candiesCount)):
            cum.append(candiesCount[i] + cum[-1])
        ans = []
        for i, day, cap in queries:
            maximum = (day + 1) * cap
            if cum[i] <= day:
                ans.append(False)
            elif i > 0 and cum[i-1] >= maximum:
                ans.append(False)
            else:
                ans.append(True)
        return ans
