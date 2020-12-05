class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        continuous_space = 1
        can_plant = 0
        for planted in flowerbed:
            if planted:
                can_plant += (continuous_space - 1) // 2
                continuous_space = 0
            else:
                continuous_space += 1
        can_plant += continuous_space // 2
        return can_plant >= n
