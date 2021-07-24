class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not endWord in wordList: return []
        @lru_cache(None)
        def diff(a, b):
            if a > b: return diff(b, a)
            valid = False
            for i in range(len(a)):
                if a[i] != b[i]:
                    if valid: return False
                    valid = True
            return valid

        def bfs(pathes, visited):
            nonlocal wordList
            new = []
            for path in pathes:
                for word in wordList:
                    if word in visited: continue
                    if diff(word, path[-1]):
                        new.append([p for p in path] + [word])
            for n in new:
                visited.add(n[-1])
            return new, visited


        begin_pathes = [[beginWord]]
        end_pathes= [[endWord]]
        begin_visited = set([beginWord])
        end_visited = set([endWord])
        ans = []
        while begin_pathes and end_pathes:
            if len(begin_pathes) < len(end_pathes):
                begin_pathes, begin_visited = bfs(begin_pathes, begin_visited)
            else:
                end_pathes, end_visited = bfs(end_pathes, end_visited)
            for b in begin_pathes:
                for e in end_pathes:
                    if b[-1] == e[-1]:
                        ans.append(b[:-1] + e[::-1])
            if ans: break
        return ans
