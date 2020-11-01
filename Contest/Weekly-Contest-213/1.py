class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i < len(arr) - 1:
            j = i + 1
            while j < len(arr)+1:
                tmp = arr[i:j]
                if tmp in pieces:
                    i = j
                    break
                j += 1
            else:
                return False
        return True
