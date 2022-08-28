class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        counter = defaultdict(int)
        for g in garbage:
            for c in g:
                counter[c] += 1

        def collect(a):
            nonlocal counter
            i = 0
            time = counter[a]
            while counter[a] > 0:
                counter[a] -= garbage[i].count(a)
                if counter[a] == 0: break
                time += travel[i]
                i += 1
            return time

        return collect("M") + collect("P") + collect("G")
