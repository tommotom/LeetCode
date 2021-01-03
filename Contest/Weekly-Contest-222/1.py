class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        i = units = 0
        while i < len(boxTypes):
            if boxTypes[i][0] <= truckSize:
                units += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i += 1
            else:
                units += truckSize * boxTypes[i][1]
                break
        return units
