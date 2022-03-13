class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        def is_k_distant_index(i):
            if nums[i] == key: return True
            for j in range(max(0, i-k), i):
                if nums[j] == key: return True
            for j in range(i+1, min(len(nums), i+k+1)):
                if nums[j] == key: return True
            return False

        return [i for i in range(len(nums)) if is_k_distant_index(i)]
