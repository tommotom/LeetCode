class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = current = len(arr)
        counter = Counter(arr)
        ans = 0
        for count in sorted(counter.values(), reverse=True):
            ans += 1
            current -= count
            if current <= length//2:
                break
        return ans
