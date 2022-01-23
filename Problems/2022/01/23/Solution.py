class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        def genSeqs(length):
            ret = []
            for start in range(1, 11 - length):
                num = start
                for _ in range(length-1):
                    start += 1
                    num *= 10
                    num += start
                ret.append(num)
            return ret

        ans = []
        for length in range(len(str(low)), len(str(high))+1):
            tmp = genSeqs(length)
            for t in tmp:
                if low <= t <= high:
                    ans.append(t)
        return ans
