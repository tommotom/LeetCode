class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        maps = [[-1] * n for _ in range(n)]
        remain = defaultdict(set)
        for i in range(len(artifacts)):
            r1, c1, r2, c2 = artifacts[i]
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    maps[r][c] = i
                    remain[i].add((r, c))

        for r, c in dig:
            if maps[r][c] == -1: continue
            remain[maps[r][c]].remove((r, c))

        return len([v for v in remain.values() if len(v)==0])
