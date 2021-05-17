class Solution:
    def sortSentence(self, s: str) -> str:
        arr = sorted(s.split(), key=lambda x:x[-1])
        for i in range(len(arr)):
            arr[i] = arr[i][:-1]
        return " ".join(arr)
