from collections import defaultdict

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counter = defaultdict(list)
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 0: break
                count += 1
            counter[count].append(i)

        ans = []
        for i, v in sorted(counter.items(), key=lambda x: x[0]):
            for j in v:
                ans.append(j)
                if len(ans) == k: break
            else: continue
            break
        return ans
