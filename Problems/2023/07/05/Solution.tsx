function longestSubarray(nums: number[]): number {
    if (nums.length === nums.reduce((a, b) => a + b)) {
        return nums.length - 1;
    }

    let last = 0, cur = 0, ans = 0;
    for (const num of nums) {
        if (num === 1) {
            cur++;
        } else {
            last = cur;
            cur = 0;
        }
        ans = Math.max(ans, last + cur);
    }
    return ans;
};
