function findMaxLength(nums: number[]): number {
    let ans = 0, count = 0;
    const seenAt = new Map();
    seenAt.set(0, -1);
    for (let i = 0; i < nums.length; i++) {
        count += nums[i] === 1 ? 1 : -1;
        if (seenAt.has(count)) {
            ans = Math.max(ans, i - seenAt.get(count));
        } else {
            seenAt.set(count, i);
        }
    }
    return ans;
};
