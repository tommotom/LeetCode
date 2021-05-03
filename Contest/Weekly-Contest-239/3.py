class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def nextPerm(num: list) -> list:
            i = n-1
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            j = i
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            num[i:] = reversed(num[i:])
            return num

        n = len(num)
        nkt_k_perm = list(num)
        for _ in range(k):
            nkt_k_perm = nextPerm(nkt_k_perm)

        ans = 0
        num = list(num)
        for i in range(n):
            j = i
            while j < n and nkt_k_perm[i] != num[j]:
                j += 1
            ans += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return ans
