from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        counter = Counter(s)

        def minusDelete(char, count):
            nonlocal counter
            counter[char] -= count
            if counter[char] <= 0: del counter[char]


        ans = ["" for _ in range(10)]

        if "z" in counter:
            tmp = counter["z"]
            ans[0] = "0" * tmp
            for char in nums[0]:
                minusDelete(char, tmp)

        if "w" in counter:
            tmp = counter["w"]
            ans[2] = "2" * tmp
            for char in nums[2]:
                minusDelete(char, tmp)

        if "u" in counter:
            tmp = counter["u"]
            ans[4] = "4" * tmp
            for char in nums[4]:
                minusDelete(char, tmp)

        if "x" in counter:
            tmp = counter["x"]
            ans[6] = "6" * tmp
            for char in nums[6]:
                minusDelete(char, tmp)

        if "s" in counter:
            tmp = counter["s"]
            ans[7] = "7" * tmp
            for char in nums[7]:
                minusDelete(char, tmp)

        if "v" in counter:
            tmp = counter["v"]
            ans[5] = "5" * tmp
            for char in nums[5]:
                minusDelete(char, tmp)

        if "g" in counter:
            tmp = counter["g"]
            ans[8] = "8" * tmp
            for char in nums[8]:
                minusDelete(char, tmp)

        if "h" in counter:
            tmp = counter["h"]
            ans[3] = "3" * tmp
            for char in nums[3]:
                minusDelete(char, tmp)

        if "i" in counter:
            tmp = counter["i"]
            ans[9] = "9" * tmp
            for char in nums[9]:
                minusDelete(char, tmp)

        if "o" in counter:
            tmp = counter["o"]
            ans[1] = "1" * tmp
            for char in nums[1]:
                minusDelete(char, tmp)

        return "".join(ans)
