class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        while seats[i] != 1:
            i += 1
        ans = i

        prev = i
        i += 1
        while i < len(seats):
            if seats[i] == 1:
                ans = max(ans, (i-prev)//2)
                prev = i
            i += 1

        if seats[-1] == 0:
            ans = max(ans, len(seats) - prev - 1)

        return ans
