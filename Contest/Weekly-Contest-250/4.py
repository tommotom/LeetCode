class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        cur = self.root
        for w in word:
            if not w in cur:
                cur[w] = {}
            cur = cur[w]

    def max_genetic(self, target):
        cur = self.root
        res = 0
        for w in target:
            res <<= 1
            desired = "1" if w == "0" else "0"
            if desired in cur:
                res += 1
                cur = cur[desired]
            else:
                cur = cur[w]
        return res

    def delete(self, word):
        cur = self.root
        stack = []
        for w in word:
            stack.append(cur)
            cur = cur[w]
        del cur
        for w, cur in zip(word[::-1], stack[::-1]):
            if not cur[w]:
                del cur[w]
            else:
                break

class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        node_to_query = defaultdict(list)
        for i, (node, val) in enumerate(queries):
            node_to_query[node].append((i, val))

        graph = defaultdict(list)
        for i, node in enumerate(parents):
            graph[node].append(i)

        ans = [-1 for _ in range(len(queries))]
        t = Trie()

        def dfs(node):
            str_node = bin(node)[2:].zfill(20)
            t.add(str_node)
            for i, val in node_to_query[node]:
                ans[i] = t.max_genetic(bin(val)[2:].zfill(20))
            for next_node in graph[node]:
                dfs(next_node)
            t.delete(str_node)

        dfs(graph[-1][0])

        return ans
