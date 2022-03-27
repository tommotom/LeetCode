class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [[s1 for s1 in set1 if s1 not in set2], [s2 for s2 in set2 if s2 not in set1]]
