class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        h, m = int(startTime[:2]), int(startTime[3:])
        H, M = int(finishTime[:2]), int(finishTime[3:])
        game = False
        ans = 0
        while True:
            if h == H and m == M:
                break
            while m < 60:
                if m % 15 == 0:
                    if game:
                        ans += 1
                    game = True
                m += 1
                if h == H and m == M:
                    break
            else:
                m = 0
                h = (h+1) % 24
                continue
        if game and m % 15 == 0: ans += 1
        return ans
