class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        candidates = []
        if nums[0] == x: candidates.append(1)
        if nums[-1] == x: candidates.append(1)

        fromRight = [num for num in nums]
        for i in range(n-2, -1, -1):
            fromRight[i] += fromRight[i+1]
            if fromRight[i] == x: candidates.append(n-i)

        fromLeft = [num for num in nums]
        for i in range(n-1):
            fromLeft[i+1] += fromLeft[i]
            if fromLeft[i+1] == x: candidates.append(i+2)

        numMap = {}
        for i in range(n):
            if fromRight[i] == x:
                candidates.append(n-i)
            elif x-fromRight[i] in numMap:
                candidates.append((numMap[x-fromRight[i]]+1) + (n-i))
            numMap[fromLeft[i]] = i


        if candidates: return min(candidates)
        else: return -1
