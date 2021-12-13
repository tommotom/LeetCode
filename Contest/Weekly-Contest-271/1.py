class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        for i in range(0,len(rings),2):
            color = rings[i]
            position = rings[i+1]
            rods[position].add(color)

        ans = 0
        for k, v in rods.items():
            if len(v) == 3:
                ans += 1
        return ans