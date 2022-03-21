class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def calcPoint(bit):
            ret = 0
            for i in range(1, 12):
                if bit & (1 << (i-1)):
                    ret += i
            return ret

        def genArr(bit):
            ret = [0] * 12
            ret[0] = numArrows
            for i in range(1, 12):
                if bit & (1 << (i-1)):
                    ret[i] += aliceArrows[i] + 1
                    ret[0] -= aliceArrows[i] + 1
            return ret

        def requiredArrow(bit):
            arrow = 0
            for i in range(1, 12):
                if bit & (1 << (i-1)):
                    arrow += aliceArrows[i] + 1
            return arrow

        def isValid(bit):
            return requiredArrow(bit) <= numArrows

        ans = []
        point = 0
        for bit in range(1, pow(2, 12)-1):
            if isValid(bit):
                p = calcPoint(bit)
                if point < p:
                    point = p
                    ans = genArr(bit)

        return ans
