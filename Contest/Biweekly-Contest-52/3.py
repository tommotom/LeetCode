class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            l = r = 0
            while r < len(box[i]):
                if box[i][r] == "*":
                    box[i][l:r] = sorted(box[i][l:r], reverse=True)
                    l = r + 1
                r += 1
            box[i][l:r] = sorted(box[i][l:r], reverse=True)

        ans = []
        for j in range(len(box[0])):
            tmp = []
            for i in range(len(box)-1, -1, -1):
                tmp.append(box[i][j])
            ans.append(tmp)
        return ans
