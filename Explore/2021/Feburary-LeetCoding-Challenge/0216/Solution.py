class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        n = len(S)
        ans = []
        def helper(arr, idx):
            nonlocal S, n, ans

            if idx == n:
                ans.append("".join(arr))
                return

            if S[idx].isalpha():
                arr.append(S[idx].lower())
                helper(arr, idx+1)
                arr[-1] = S[idx].upper()
                helper(arr, idx+1)
            else:
                arr.append(S[idx])
                helper(arr, idx+1)
            arr.pop()

            return

        helper([], 0)

        return ans
