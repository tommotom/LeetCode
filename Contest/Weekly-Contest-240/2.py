class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(min(len(nums1), len(nums2))):
            l, r = i, len(nums2)-1
            while l+1 < r:
                m = (l + r) // 2
                if nums2[m] < nums1[i]:
                    r = m
                else:
                    l = m
            if nums1[i] <= nums2[r]:
                ans = max(ans, r - i)
            if nums1[i] <= nums2[l]:
                ans = max(ans, l - i)
        return ans
