class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(k, n, arr, arrSum):
            if arr: tmp = arr[-1]
            else: tmp = 0

            for i in range(tmp + 1, min((n - arrSum)//k + 1, 10)):
                arr.append(i)
                arrSum += i
                if k == 1 and arrSum == n:
                    ans.append([j for j in arr])
                elif k > 1:
                    helper(k-1, n, arr, arrSum)
                arr.pop()
                arrSum -= i

        helper(k, n, [], 0)
        return ans