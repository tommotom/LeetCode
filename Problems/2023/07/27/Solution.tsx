function maxRunTime(n: number, batteries: number[]): number {
    batteries.sort((a, b) => a - b);
    let sum = batteries.reduce((a, b) => a + b);
    let k = 0, l = batteries.length;
    while (batteries[l-1-k] > sum / (n - k)) {
        sum -= batteries[l-1-k++];
    }
    return Math.floor(sum / (n - k));
};
