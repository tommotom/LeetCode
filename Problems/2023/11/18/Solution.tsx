function maxFrequency(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let l = 0, ans = 0, sum = 0;
    for (let r = 0; r < nums.length; r++) {
        while (l < r && (r - l) * nums[r] - sum > k) {
            sum -= nums[l++];
        }
        ans = Math.max(ans, r - l + 1);
        sum += nums[r];
    }
    return ans;
};
