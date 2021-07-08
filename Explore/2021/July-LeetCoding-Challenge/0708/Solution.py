class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        mod = (1 << 128) - 159
        unit = 1 << 7

        def rollingHash(arr, length):
            nonlocal mod, unit

            val = 0
            for i in range(length):
                val *= unit
                val += arr[i]
                val %= mod

            ret = {val}
            max_digit = (1 << ((length-1) * 7))
            for i in range(len(arr)-length):
                val -= max_digit * arr[i]
                val *= unit
                val += arr[i+length]
                val %= mod
                ret.add(val)

            return ret

        l, r = 0, min(n, m)+1
        while l+1 < r:
            m = (l+r) // 2
            set1, set2 = rollingHash(nums1, m), rollingHash(nums2, m)
            if set1 & set2:
                l = m
            else:
                r = m
        return l
