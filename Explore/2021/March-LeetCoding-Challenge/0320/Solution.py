class UndergroundSystem:

    def __init__(self):
        self.traveling = {}
        self.totalTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.traveling[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        a = self.traveling[id][0]
        b = stationName

        if not (a, b) in self.totalTime:
            self.totalTime[(a, b)] = [0, 0]

        self.totalTime[(a, b)][0] += t - self.traveling[id][1]
        self.totalTime[(a, b)][1] += 1

        del self.traveling[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.totalTime[(startStation, endStation)][0] / self.totalTime[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
