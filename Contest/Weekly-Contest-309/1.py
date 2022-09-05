class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)

        for i in range(26):
            c = chr(i + ord('a'))
            if not c in indices: continue
            a, b = indices[c]
            if b - a - 1 != distance[i]:
                return False

        return True
