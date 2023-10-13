function minCostClimbingStairs(cost: number[]): number {
    const memo = new Map();
    function dp(i: number): number {
        if (i >= cost.length) {
            return 0;
        }
        if (!memo.has(i)) {
            memo.set(i, Math.min(dp(i+1), dp(i+2)) + cost[i]);
        }
        return memo.get(i);
    }
    return Math.min(dp(0), dp(1));
};
