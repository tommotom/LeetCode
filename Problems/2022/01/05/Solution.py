class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def helper(i, arr):
            nonlocal s, ans

            if i == len(s):
                ans.append(list(arr))

            j = i+1
            while j <= len(s):
                if s[i:j] == s[i:j][::-1]:
                    arr.append(s[i:j])
                    helper(j, arr)
                    arr.pop()
                j += 1

        helper(0, [])

        return ans
