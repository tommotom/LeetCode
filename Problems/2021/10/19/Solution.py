class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num1 in nums1:
            found = False
            for num2 in nums2:
                if num1 == num2:
                    found = True
                elif found and num1 < num2:
                    ans.append(num2)
                    break
            else:
                ans.append(-1)
        return ans
