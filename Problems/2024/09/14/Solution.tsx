function longestSubarray(nums: number[]): number {
    const max = nums.reduce((a, b) => Math.max(a, b));
    let ans = 0, cur = 0;
    for (const num of nums) {
        if (max === num) {
            cur++;
        } else {
            cur = 0;
        }
        ans = Math.max(ans, cur);
    }
    return ans;
};
