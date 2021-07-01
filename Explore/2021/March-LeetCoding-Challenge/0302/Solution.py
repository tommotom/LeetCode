from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        arr = [0,0]
        for i in range(1, len(nums)+1):
            if i not in counter: arr[1] = i
            elif counter[i] == 2: arr[0] = i
        return arr
