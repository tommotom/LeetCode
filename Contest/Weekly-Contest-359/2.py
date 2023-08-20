class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        arr = set()
        num = 1
        while len(arr) < n:
            if not (k-num) in arr:
                arr.add(num)
            num += 1
        return sum(arr)
