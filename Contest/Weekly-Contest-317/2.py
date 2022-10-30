class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        total = defaultdict(int)
        highest = defaultdict(int)
        best = defaultdict()
        for j in range(len(creators)):
            c, i, v = creators[j], ids[j], views[j]
            total[c] += v
            if highest[c] < v:
                highest[c] = v
                best[c] = i
            elif highest[c] == v:
                best[c] = i if c not in best else min(best[c], i)

        m = max(total.values())

        ans = []
        for c, v in total.items():
            if v == m:
                ans.append([c, best[c]])

        return ans
