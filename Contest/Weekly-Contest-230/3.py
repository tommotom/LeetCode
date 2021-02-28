from collections import Counter

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2: return 0
        elif sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        dic1 = Counter(nums1)
        dic2 = Counter(nums2)

        print(nums1, nums2, sum1, sum2)

        ops = 0
        if 1 in dic1:
            o = min(ceil((sum2-sum1)/5), dic1[1])
            ops += o
            sum1 += 5*o
            print(sum1, sum2)
            if sum2 <= sum1: return ops
        if 6 in dic2:
            o = min(ceil((sum2-sum1)/5), dic2[6])
            ops += o
            sum2 -= 5*o
            print(sum1, sum2)
            if sum2 <= sum1: return ops
        if 2 in dic1:
            o = min(ceil((sum2-sum1)/4), dic1[2])
            ops += o
            sum1 += 4*o
            if sum2 <= sum1: return ops
        if 5 in dic2:
            o = min(ceil((sum2-sum1)/4), dic2[5])
            ops += o
            sum2 -= 4*o
            if sum2 <= sum1: return ops
        if 3 in dic1:
            o = min(ceil((sum2-sum1)/3), dic1[3])
            ops += o
            sum1 += 3*o
            if sum2 <= sum1: return ops
        if 4 in dic2:
            o = min(ceil((sum2-sum1)/3), dic2[4])
            ops += o
            sum2 -= 3*o
            if sum2 <= sum1: return ops
        if 4 in dic1:
            o = min(ceil((sum2-sum1)/2), dic1[4])
            ops += o
            sum1 += 2*o
            if sum2 <= sum1: return ops
        if 3 in dic2:
            o = min(ceil((sum2-sum1)/2), dic2[3])
            ops += o
            sum2 -= 2*o
            if sum2 <= sum1: return ops
        if 5 in dic1:
            o = min(ceil((sum2-sum1)/1), dic1[5])
            ops += o
            sum1 += 1*o
            if sum2 <= sum1: return ops
        if 2 in dic2:
            o = min(ceil((sum2-sum1)/1), dic2[2])
            ops += o
            sum2 -= 1*o
            if sum2 <= sum1: return ops

        return -1
