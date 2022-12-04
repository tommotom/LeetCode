class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split(" ")
        for i in range(len(arr)-1):
            if arr[i][-1] != arr[i+1][0]: return False
        return arr[0][0] == arr[-1][-1]
