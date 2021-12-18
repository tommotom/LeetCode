class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        indices, n = [], str(n)

        def helper(i):
            nonlocal indices

            cur = "".join([digits[i] for i in indices])

            if len(indices) == len(n): return indices if cur <= n else None

            if cur and cur < n[:len(indices)]:
                indices.append(len(digits)-1)
                return helper(i+1)

            j = 0
            while j < len(digits)-1 and digits[j+1] <= n[i]:
                j += 1

            indices.append(j)
            tmp = helper(i+1)
            if tmp: return tmp
            indices.pop()

            if j == 0: return

            indices.append(j-1)
            tmp = helper(i+1)
            if tmp: return tmp
            indices.pop()


        less = helper(0) or [len(digits)-1 for _ in range(len(n)-1)]

        if not less: return 0

        ans = 1
        for i in range(len(less)):
            ans += less[i] * pow(len(digits), len(less)-i-1)
            if i < len(less)-1:
                ans += pow(len(digits), i+1)
        return ans
