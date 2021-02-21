class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            count = 0
            for j, c in enumerate(boxes):
                if c == "1":
                    count += abs(i-j)
            ans.append(count)
        return ans
