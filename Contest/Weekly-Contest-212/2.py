class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            length = r[i] - l[i] + 1
            if length < 2:
                ans.append(False)
                continue

            tmp = sorted(nums[l[i]: r[i]+1])
            j, diff = 1, tmp[1] - tmp[0]
            while j < length and tmp[j] - tmp[j-1] == diff:
                j += 1

            if j == length: ans.append(True)
            else: ans.append(False)

        return ans
