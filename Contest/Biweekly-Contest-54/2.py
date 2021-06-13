class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        for i in range(len(chalk)-1):
            chalk[i+1] += chalk[i]
        k %= chalk[-1]
        return bisect.bisect_right(chalk, k)
