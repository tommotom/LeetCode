class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        using = batteries[len(batteries)-n:len(batteries)]
        rest = sum(batteries[:len(batteries)-n])

        charge = 0
        minimum = using[0]
        while True:
            while charge+1 < n and using[charge+1] == minimum:
                charge += 1

            if charge == n-1:
                return minimum + rest // n

            diff = using[charge+1] - minimum
            if rest < diff * (charge+1):
                return minimum + rest // (charge+1)

            minimum = minimum + diff
            rest -= diff * (charge+1)
