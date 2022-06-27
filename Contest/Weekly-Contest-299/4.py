class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n, m = len(nums), len(edges)
        graph = defaultdict(list)
        deg = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            deg[u] += 1
            deg[v] += 1

        whole = reduce(xor, nums)
        seen = set()
        q = deque([])
        for k, v in graph.items():
            if len(v) == 1:
                seen.add(k)
                q.append(k)

        children = defaultdict(set)
        xors = nums[:]
        while q:
            k = q.popleft()
            for nei in graph[k]:
                if nei not in seen:
                    children[nei].add(k)
                    children[nei] |= children[k]
                    xors[nei] ^= xors[k]
                deg[nei] -= 1

                if deg[nei] == 1 and len(seen) != n-1:
                    seen.add(nei)
                    q.append(nei)

        ans = float('inf')
        for i in range(len(edges)-1):
            for j in range(i+1, len(edges)):
                a, b = edges[i]
                if b in children[a]: a, b = b, a

                c, d = edges[j]
                if d in children[c]: c, d = d, c

                if c in children[a]:
                    cur = [xors[c], xors[a]^xors[c], whole^xors[a]]
                elif a in children[c]:
                    cur = [xors[a], xors[c]^xors[a], whole^xors[c]]
                else:
                    cur = [xors[a], xors[c], whole^xors[a]^xors[c]]
                ans = min(ans, max(cur) - min(cur))

        return ans
