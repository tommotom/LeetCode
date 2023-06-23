function longestArithSeqLength(nums: number[]): number {
    const seen: Map<number, number>[] = new Array(nums.length);
    for (let i = 0; i < nums.length; i++) {
        seen[i] = new Map();
    }

    let ans = 0;
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            const diff = nums[i] - nums[j];
            const prev = seen[j].has(diff) ? seen[j].get(diff) : 1;
            seen[i].set(diff, prev + 1);
            ans = Math.max(ans, prev + 1);
        }
    }
    return ans;
};
