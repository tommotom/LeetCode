function maxFrequencyElements(nums: number[]): number {
    const count = new Map();
    nums.forEach((num) => {
        if (!count.has(num)) {
            count.set(num, 0);
        }
        count.set(num, count.get(num) + 1);
    });
    const freqs = Array.from(count.values());
    const max = freqs.reduce((a, b) => Math.max(a, b));
    return freqs.filter(a => a === max).reduce((a, b) => a + b);
};
