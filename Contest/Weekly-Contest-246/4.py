class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def isValid(num, left, right):
            nonlocal num_to_idx
            arr = num_to_idx[num]
            l = bisect.bisect_left(arr, left)
            r = bisect.bisect_right(arr, right)
            if l == r: return False
            return True


        num_to_idx = defaultdict(list)
        for i, num in enumerate(nums):
            num_to_idx[num].append(i)
        reduce = sorted([num for num in set(nums)])

        ans = []

        for l, r in queries:
            tmp_arr = []
            for red in reduce:
                if isValid(red, l, r):
                    tmp_arr.append(red)
            if len(tmp_arr) < 2:
                ans.append(-1)
                continue
            tmp = float('inf')
            for i in range(1, len(tmp_arr)):
                tmp = min(tmp, abs(tmp_arr[i] - tmp_arr[i-1]))
            ans.append(tmp)

        return ans
