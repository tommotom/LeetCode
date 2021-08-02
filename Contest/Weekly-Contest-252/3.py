class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        apples = 0
        i = 1
        while apples < neededApples:
            i += 1
            tmp = 3*i*i - 6*i + 3
            apples += tmp * 4
        return (2 * i - 2) * 4

