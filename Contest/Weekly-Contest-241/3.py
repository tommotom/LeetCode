class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.count1 = Counter(nums1)
        self.keys = sorted(self.count1.keys())
        self.count2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.count2[self.nums2[index]] -= 1
        self.nums2[index] += val
        if not self.nums2[index] in self.count2:
            self.count2[self.nums2[index]] = 0
        self.count2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.keys:
            if num > tot: break
            if tot - num in self.count2:
                print(tot-num, num)
                ans += self.count2[tot-num] * self.count1[num]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
