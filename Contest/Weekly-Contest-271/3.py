class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a, b = 0, len(plants)-1
        waterA, waterB = capacityA, capacityB
        ans = 0
        while a < b:
            if plants[a] <= waterA:
                waterA -= plants[a]
            else:
                ans += 1
                waterA = capacityA - plants[a]

            if plants[b] <= waterB:
                waterB -= plants[b]
            else:
                ans += 1
                waterB = capacityB - plants[b]

            a += 1
            b -= 1

        if a == b and max(waterA, waterB) < plants[a]:
            ans += 1

        return ans
