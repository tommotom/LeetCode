class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stack = []
        res = [-1] * len(cars)
        for i in range(len(cars)-1, -1, -1):
            p, s = cars[i]
            while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        return res
