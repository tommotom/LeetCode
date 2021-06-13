class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def isValid(tri, target):
            for i in range(3):
                if tri[i] > target[i]: return False
            return True

        candidate = []
        for i in range(3):
            t = target[i]
            c = []
            for tri in triplets:
                if tri[i] == t and isValid(tri, target):
                    c.append(i)
            candidate.append(c)

        for c in candidate:
            if not c: return False
        return True
