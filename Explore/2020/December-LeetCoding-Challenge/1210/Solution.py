class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        prev = arr[0]
        increased = decreasing = False
        for num in arr[1:]:
            if prev == num: return False
            if not decreasing:
                if prev < num: increased = True
                else: decreasing = True
            else:
                if prev < num: return False
            prev = num
        return increased and decreasing
