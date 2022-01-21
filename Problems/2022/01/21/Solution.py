class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cum = minimum = 0
        idx = -1
        for i in range(len(gas)):
            cum += gas[i] - cost[i]
            if cum < minimum:
                minimum = cum
                idx = i

        cum = 0
        for i in range(idx+1, len(gas)):
            cum += gas[i] - cost[i]
            if cum < 0: return -1
        for i in range(idx+1):
            cum += gas[i] - cost[i]
            if cum < 0: return -1

        return idx + 1
