class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [key for key, val in counter.items() if val == 1 and key+1 not in counter and key-1 not in counter]
