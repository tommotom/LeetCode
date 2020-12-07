class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[None] * n for _ in range(n)]
        num, square = 1, n * n
        direction = "right"
        i = j = 0
        while True:
            arr[i][j] = num
            if num == square: break
            num += 1
            while arr[i][j]:
                if direction == "right":
                    if j + 1 < n and not arr[i][j+1]:
                        j += 1
                    else:
                        direction = "down"
                elif direction == "down":
                    if i + 1 < n and not arr[i+1][j]:
                        i += 1
                    else:
                        direction = "left"
                elif direction == "left":
                    if j > 0 and not arr[i][j-1]:
                        j -= 1
                    else:
                        direction = "up"
                elif direction == "up":
                    if i > 0 and not arr[i-1][j]:
                        i -= 1
                    else:
                        direction = "right"
        return arr
