class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for q in queries:
            a = 0
            for i, num in enumerate(nums):
                if a + num > q:
                    ans.append(i)
                    break
                else:
                    a += num
            else:
                ans.append(len(nums))
        return ans
