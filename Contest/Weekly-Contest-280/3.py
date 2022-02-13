class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        cum = [beans[0]]
        for i in range(1, len(beans)):
            cum.append(beans[i])
            cum[i] += cum[i-1]

        ans = float('inf')
        for i in range(len(beans)):
            tmp = cum[i-1] if i > 0 else 0
            level = beans[i]
            tmp += (cum[-1] - cum[i]) - (len(beans)-i-1)*level
            ans = min(ans, tmp)

        return ans
