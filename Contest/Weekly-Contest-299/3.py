class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def bestSplice(A, B):
            ans = [B[i] - A[i] for i in range(len(A))]
            best = -float('inf')
            start = end = cur = last = cur_start = 0
            for i in range(len(A)):
                if last <= 0: cur_start = i
                cur = ans[i] + max(last, 0)
                if cur >= best:
                    best = cur
                    start = cur_start
                    end = i
                last = cur
            ans = list(A)
            if best > 0:
                for i in range(start, end+1):
                    ans[i] = B[i]
            return ans

        return max(sum(bestSplice(nums1, nums2)), sum(bestSplice(nums2, nums1)))
