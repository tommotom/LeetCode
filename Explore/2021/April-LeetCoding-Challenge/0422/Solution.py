class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        dic[0] = 0
        for i in range(len(wall)):
            if len(wall[i]) == 1: continue
            x = 0
            for j in range(len(wall[i][:-1])):
                x += wall[i][j]
                dic[x] += 1
        return len(wall) - max(dic.values())
