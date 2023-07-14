function longestSubsequence(arr: number[], difference: number): number {
    const dp: Map<number, number> = new Map();
    for (const num of arr) {
        const prev = dp.has(num - difference) ? dp.get(num - difference) : 0;
        if (dp.has(num)) {
            dp.set(num, Math.max(dp.get(num), prev + 1));
        } else {
            dp.set(num, prev + 1);
        }
    }
    return Array.from(dp.values()).reduce((a, b) => Math.max(a, b));
};
