class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ret = []
        for i in range(1, len(num)):
            tmp = int(num[:i])
            if len(str(tmp)) != i: break
            ret += self.helper(num[i:], target - tmp, tmp, num[:i])
        if len(num) == len(str(int(num))) and int(num) == target:
            ret.append(num)

        return ret

    def helper(self, num: str, target: int, last: int, org: str) -> List[str]:
        ret = []
        for i in range(1, len(num)):
            tmp = int(num[:i])

            if len(str(tmp)) != len(num[:i]): break

            plus = self.helper(num[i:], target - tmp, tmp, num[:i])
            for p in plus:
                ret.append(org + "+" + p)

            minus = self.helper(num[i:], tmp + target, -tmp, num[:i])
            for m in minus:
                ret.append(org + "-" + m)

            times = self.helper(num[i:], target - (last * (tmp-1)), last*tmp, num[:i])
            for t in times:
                ret.append(org + "*" + t)

        tmp = int(num)
        if str(tmp) != num: return ret

        if target == tmp:
            ret.append(org + "+" + num)
        if -target == tmp:
            ret.append(org + "-" + num)
        if target == (last * (tmp-1)):
            ret.append(org + "*" + num)

        return ret
