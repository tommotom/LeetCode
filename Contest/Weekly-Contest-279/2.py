class Solution:
    def smallestNumber(self, num: int) -> int:
        num = list(str(num))
        if num[0] != "-":
            num.sort()
            idx = -1

            for i in range(len(num)):
                if num[i] != "0":
                    idx = i
                    break
            return int(num[idx] + "".join(sorted(num[:idx] + num[idx+1:])))
        else:
            return -1 * int(''.join(sorted(num[1:], reverse=True)))
