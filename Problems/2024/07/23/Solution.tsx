function frequencySort(nums: number[]): number[] {
    const counter = new Map();
    for (const num of nums) {
        if (!counter.has(num)) {
            counter.set(num, 0);
        }
        counter.set(num, counter.get(num) + 1);
    }
    return nums.sort((a, b) => counter.get(a) === counter.get(b) ? b - a : counter.get(a) - counter.get(b));
};
