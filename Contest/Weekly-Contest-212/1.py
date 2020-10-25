from collections import defaultdict

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        pressed = defaultdict(lambda: 0)
        pressed[keysPressed[0]] = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            pressed[keysPressed[i]] = max(pressed[keysPressed[i]], releaseTimes[i] - releaseTimes[i-1])

        time, ans = 0, ""
        for k,v in pressed.items():
            if v > time:
                time = v
                ans = k
            elif v == time:
                if k > ans: ans = k

        return ans
