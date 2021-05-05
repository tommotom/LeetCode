class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        i, j = 0, 1
        skipped = False
        while j < len(nums):
            if nums[i] > nums[j]:
                if skipped: break
                elif i == 0 or (i > 0 and nums[i-1] <= nums[j]):
                    i += 1
                    j += 1
                    skipped = True
                else:
                    break
            else:
                i += 1
                j += 1
        else:
            return True

        i, j = 0, 1
        skipped = False
        while j < len(nums):
            if nums[i] > nums[j]:
                if skipped: break
                elif j == len(nums) - 1 or (j < len(nums) and nums[i] <= nums[j+1]):
                    i += 2
                    j += 2
                    skipped = True
                else:
                    break
            else:
                i += 1
                j += 1
        else:
            return True

        return False
