class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for num in nums[1:]:
            if math.gcd(ans[-1], num) == 1:
                ans.append(num)
            else:
                ans[-1] = math.lcm(ans[-1], num)

            while len(ans) > 1 and math.gcd(ans[-1], ans[-2]) > 1:
                ans[-2] = math.lcm(ans[-2], ans[-1])
                ans.pop()

        return ans
