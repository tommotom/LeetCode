function minSubArrayLen(target: number, nums: number[]): number {
    if (nums.reduce((a, b) => a + b) < target) {
        return 0;
    }
    let l = 0, r = 0, sum = 0, ans = undefined;
    while (r <= nums.length) {
        if (sum < target) {
            if (r === nums.length) {
                break;
            }
            sum += nums[r++];
        } else {
            ans = ans === undefined ? r - l : Math.min(ans, r - l);
            sum -= nums[l++]
        }
    }
    return ans === undefined ? 0 : ans;
};
