class DetectSquares:

    def __init__(self):
        self.x_to_y = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_to_y[x][y] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        ret = 0
        visited = set()
        for y1 in self.x_to_y[x0]:
            if y0 == y1: continue
            length = abs(y1 - y0)

            if x0 + length in self.x_to_y and y0 in self.x_to_y[x0+length] and y1 in self.x_to_y[x0+length]:
                x2 = x0 + length
                key = tuple(sorted([(x0, y0), (x0, y1), (x2, y0), (x2, y1)]))
                if not key in visited:
                    visited.add(key)
                    ret += self.x_to_y[x0][y1] * self.x_to_y[x2][y0] * self.x_to_y[x2][y1]

            if x0 - length in self.x_to_y and y0 in self.x_to_y[x0-length] and y1 in self.x_to_y[x0-length]:
                x2 = x0 - length
                key = tuple(sorted([(x0, y0), (x0, y1), (x2, y0), (x2, y1)]))
                if not key in visited:
                    visited.add(key)
                    ret += self.x_to_y[x0][y1] * self.x_to_y[x2][y0] * self.x_to_y[x2][y1]
        return ret


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
