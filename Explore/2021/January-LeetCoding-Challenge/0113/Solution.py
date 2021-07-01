class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        while people:
            weight = people.pop()
            candidate = bisect.bisect_left(people, limit - weight)
            if people:
                idx = bisect.bisect_left(people, limit - weight)
                if idx > 0: idx -= 1
                if people[idx] <= limit - weight:
                    people.pop(idx)
            ans += 1
        return ans
