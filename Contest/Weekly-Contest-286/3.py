class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def ithNum(q, length):
            num = q + pow(10, length-1) - 1
            if len(str(num)) != length: return -1
            return num

        def helper(q, length):
            num = ithNum(q, (length+1)//2)
            if num == -1: return num
            if length %2 == 0:
                return int(str(num) + str(num)[::-1])
            else:
                return int(str(num) + str(num)[::-1][1:])

        return [helper(q, intLength) for q in queries]
