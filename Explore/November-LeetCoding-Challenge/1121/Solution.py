class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits.sort()
        n = str(n)
        length = len(n)
        nums = [0] * length
        i = 0
        while i < length:
            tmp = ""
            for num in nums:
                tmp += digits[num]
            if tmp > n:
                if nums[i] > 0: nums[i] -= 1
                i += 1
            else:
                if nums[i] + 1 < len(digits): nums[i] += 1
                else: i += 1
        ans = 0
        for j in range(1, length+1):
            ans += len(digits) ** j

        mul = 1
        for i, num in enumerate(nums[::-1]):
            ans -= (len(digits) - int(num) - 1) * mul
            mul *= len(digits)

        tmp = ""
        for num in nums:
            tmp += digits[num]
        if tmp > n: ans -= 1

        return ans
