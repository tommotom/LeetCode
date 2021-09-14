class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s_arr = list(s)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s_arr[l].isalpha():
                l += 1
            while l < r and not s_arr[r].isalpha():
                r -= 1
            if not l < r: break
            s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
            l += 1
            r -= 1
        return "".join(s_arr)
