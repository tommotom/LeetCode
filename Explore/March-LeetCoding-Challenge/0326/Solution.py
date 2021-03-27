from collections import Counter
from collections import defaultdict

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        subsets = [Counter(b) for b in B]
        combine = defaultdict(lambda:0)
        for s in subsets:
            for c, count in s.items():
                combine[c] = max(combine[c], count)

        ans = []
        for a in A:
            subset = Counter(a)
            for c, count in combine.items():
                if not c in subset or not subset[c] >= count: break
            else:
                ans.append(a)
        return ans
