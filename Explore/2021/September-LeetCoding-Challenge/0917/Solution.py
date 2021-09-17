class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = Counter(nums1), Counter(nums2)
        ans = []
        for key in nums1.keys():
            if key in nums2:
                for _ in range(min(nums1[key], nums2[key])):
                    ans.append(key)
        return ans
