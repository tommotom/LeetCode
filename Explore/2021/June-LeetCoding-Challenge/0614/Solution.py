class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        idx = ans = 0
        while idx < len(boxTypes) and truckSize > 0:
            num = min(truckSize, boxTypes[idx][0])
            truckSize -= num
            ans += num * boxTypes[idx][1]
            idx += 1
        return ans
