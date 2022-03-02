class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]
        while len(ans) < n+1:
            new_ans = list(ans)
            for i in range(len(ans)):
                new_ans.append(ans[i]+1)
            ans = new_ans
        return ans[:n+1]
