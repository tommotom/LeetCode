function numIdenticalPairs(nums: number[]): number {
    const counter = new Map();
    for (const num of nums) {
        if (!counter.has(num)) {
            counter.set(num, 0);
        }
        counter.set(num, counter.get(num) + 1);
    }
    return Array.from(counter.values()).map(a => Math.floor(a * (a - 1) / 2)).reduce((a, b) => a + b);
};
