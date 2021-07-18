class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0 if rungs[0] <= dist else math.ceil((rungs[0] - dist) / dist)
        for i in range(1, len(rungs)):
            tmp = rungs[i] - rungs[i-1]
            if tmp <= dist:
                continue
            ans += math.ceil((tmp - dist) / dist)
        return ans
