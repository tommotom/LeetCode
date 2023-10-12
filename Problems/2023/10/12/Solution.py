# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, M: 'MountainArray') -> int:
        n = M.length()
        l, r = 1, n-1
        while l < r:
            m = l + (r - l) // 2
            a, b, c = M.get(m-1), M.get(m), M.get(m+1)
            if a < b > c:
                l = r = m
            elif a < b < c:
                l = m + 1
            else:
                r = m - 1

        p = l

        l, r = 0, p+1
        while l < r:
            m = l + (r - l) // 2
            num = M.get(m)
            if num == target: return m
            if num < target:
                l = m + 1
            else:
                r = m

        l, r = p, n
        while l < r:
            m = l + (r - l) // 2
            num = M.get(m)
            if num == target: return m
            if num > target:
                l = m + 1
            else:
                r = m

        return -1
