function numWaterBottles(numBottles: number, numExchange: number): number {
    let empty = 0, ans = 0;
    while (numBottles > 0) {
        ans += numBottles;
        empty += numBottles;
        numBottles = Math.floor(empty / numExchange);
        empty = empty % numExchange;
    }
    return ans;
};
