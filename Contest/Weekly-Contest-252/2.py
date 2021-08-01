class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maximum = total = 0
        for i in range(len(milestones)):
            maximum = max(maximum, milestones[i])
            total += milestones[i]
        rest = total - maximum
        if maximum > rest + 1:
            return 2 * rest + 1
        return total
