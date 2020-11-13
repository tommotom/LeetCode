class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4: return False

        def calcEdge(a, b):
            return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

        four = [p1, p2, p3, p4]
        four.sort(key=lambda x: (x[0], x[1]))

        len01 = calcEdge(four[0], four[1])
        len02 = calcEdge(four[0], four[2])
        len13 = calcEdge(four[1], four[3])
        len23 = calcEdge(four[2], four[3])

        edge01 = [four[1][0] - four[0][0], four[1][1] - four[0][1]]
        edge02 = [four[2][0] - four[0][0], four[2][1] - four[0][1]]

        return (len01 == len02 == len13 == len23) and (edge01[0] * edge02[0] + edge01[1] * edge02[1]) == 0
