class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        predict = defaultdict(list)
        for a, b in prerequisites:
            predict[a].append(b)

        ans = []
        visited = set()
        rest = [n for n in range(numCourses)]
        last = None
        while rest:
            if last == len(rest): return []
            last = len(rest)
            i = 0
            while i < len(rest):
                n = rest[i]
                if n not in predict or all(p in visited for p in predict[n]):
                    n = rest.pop(i)
                    visited.add(n)
                    ans.append(n)
                else:
                    i += 1

        return ans
