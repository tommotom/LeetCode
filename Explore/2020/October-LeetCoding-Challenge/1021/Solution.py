from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = deque([])

        for asteroid in asteroids:
            if asteroid > 0:
                ans.append(asteroid)
                continue

            while ans and ans[-1] > 0 and ans[-1] < abs(asteroid):
                ans.pop()

            if ans and ans[-1] > 0 and ans[-1] == abs(asteroid):
                ans.pop()
                continue
            elif ans and ans[-1] > 0 and ans[-1] > abs(asteroid):
                continue

            ans.append(asteroid)

        return ans
