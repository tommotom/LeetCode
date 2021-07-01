class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, worst, idx = 0, float('inf'), -1
        gas.append(gas[0])
        for i in range(len(cost)):
            tank -= cost[i]
            if tank < worst:
                worst = tank
                idx = i
            tank += gas[i+1]

        if tank >= 0: return (idx + 1) % len(cost)

        return -1
