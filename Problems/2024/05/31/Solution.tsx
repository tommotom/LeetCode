function singleNumber(nums: number[]): number[] {
    const seen: Set<number> = new Set();
    for (const num of nums) {
        if (seen.has(num)) {
            seen.delete(num);
        } else {
            seen.add(num);
        }
    }
    return Array.from(seen.values());
};
