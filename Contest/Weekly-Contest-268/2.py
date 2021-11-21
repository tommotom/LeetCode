class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity
        for i, w in enumerate(plants):
            if water < w:
                water = capacity
                steps += 2*i
            steps += 1
            water -= w
        return steps
