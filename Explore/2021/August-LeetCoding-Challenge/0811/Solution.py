class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for key in sorted(counter.keys()):
            if counter[key] > 0:
                if key > 0:
                    double = key*2
                elif key %2 == 1: return False
                else:
                    double = key // 2

                if double not in counter or counter[key] > counter[double]: return False
                counter[double] -= counter[key]
                counter[key] = 0
        return True
