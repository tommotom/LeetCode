class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        visited = set()
        for num1 in counter:
            for num2 in (num1+k, num1-k):
                if not num2 in counter: continue
                key = tuple(sorted([num1,num2]))
                if key in visited: continue
                visited.add(key)
                if num1 == num2 and counter[num1] > 1:
                    ans += 1
                elif num1 != num2:
                    ans += 1

        return ans
