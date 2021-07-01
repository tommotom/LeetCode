class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i < len(arr):
            j = 0
            while j < len(pieces):
                if pieces[j][0] == arr[i]: break
                j += 1
            else: return False

            if pieces[j] == arr[i:i+len(pieces[j])]:
                i += len(pieces.pop(j))
            else: return False
        return True
