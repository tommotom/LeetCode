class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = seats.index(1)
        ans = last

        for i in range(last+1, len(seats)):
            if seats[i] == 1:
                ans = max(ans, (i-last)//2)
                last = i

        return max(ans, len(seats)-last-1)
