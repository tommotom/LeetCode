class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        idxes = defaultdict(list)
        for i, c in enumerate(s):
            idxes[c].append(i)

        ans = 0
        for word in words:
            idx = -1
            for c in word:
                if c not in idxes: break
                tmp = bisect.bisect_right(idxes[c], idx)
                if tmp == len(idxes[c]): break
                idx = idxes[c][tmp]
            else:
                ans += 1
        return ans
