class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums12 = defaultdict(int)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                nums12[nums1[i]+nums2[j]] += 1

        nums34 = defaultdict(int)
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                nums34[nums3[i]+nums4[j]] += 1

        ans = 0
        for key in nums12:
            ans += nums12[key] * nums34[-key]
        return ans
