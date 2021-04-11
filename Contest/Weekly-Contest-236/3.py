

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        lane1, lane2, lane3 = [], [], []
        for i, o in enumerate(obstacles):
            if o == 1: heapq.heappush(lane1, i)
            if o == 2: heapq.heappush(lane2, i)
            if o == 3: heapq.heappush(lane3, i)

        lane = 2
        jump = 0
        for i in range(len(obstacles)-1):
            while lane1 and lane1[0] < i: heapq.heappop(lane1)
            while lane2 and lane2[0] < i: heapq.heappop(lane2)
            while lane3 and lane3[0] < i: heapq.heappop(lane3)

            if lane == 1 and lane1 and lane1[0] == i+1:
                if not lane2: lane = 2
                elif not lane3: lane = 3
                elif lane2[0] < lane3[0]: lane = 3
                else: lane = 2
                jump += 1
            elif lane == 2 and lane2 and lane2[0] == i+1:
                if not lane1: lane = 1
                elif not lane3: lane = 3
                elif lane1[0] < lane3[0]: lane = 3
                else: lane = 1
                jump += 1
            elif lane == 3 and lane3 and lane3[0] == i+1:
                if not lane1: lane = 1
                elif not lane2: lane = 2
                elif lane1[0] < lane2[0]: lane = 2
                else: lane = 1
                jump += 1
        return jump
