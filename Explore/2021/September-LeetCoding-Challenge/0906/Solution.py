class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_pressed = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1,len(releaseTimes)):
            pressed = releaseTimes[i] - releaseTimes[i-1]
            if pressed > max_pressed:
                max_pressed = pressed
                ans = keysPressed[i]
            elif pressed == max_pressed:
                ans = max(ans, keysPressed[i])
        return ans
