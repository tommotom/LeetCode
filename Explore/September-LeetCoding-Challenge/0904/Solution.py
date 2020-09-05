class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        for i in range(len(S)):
            if S[i] not in dic:
                dic[S[i]] = [i,i]
            else:
                dic[S[i]][1] = i

        ans = []
        now = set()
        start = 0
        for i in range(len(S)):
            if dic[S[i]][0] == i:
                now.add(S[i])
            if dic[S[i]][1] == i:
                now.remove(S[i])
            if not now:
                ans.append(i+1-start)
                start = i+1

        return ans