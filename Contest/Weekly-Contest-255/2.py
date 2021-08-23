class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        exists = set([0])
        for i in range(len(mat)):
            next_exists = set()
            for j in range(len(mat[0])):
                for s in exists:
                    next_exists.add(s+mat[i][j])
            exists = next_exists
        diff = float('inf')
        for item in exists:
            diff = min(diff, abs(target - item))
        return diff
