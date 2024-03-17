function numSubarraysWithSum(nums: number[], goal: number): number {
    let l = 0, sum = 0, ans = 0;
    const ones = [];
    for (let r = 0; r < nums.length; r++) {
        if (nums[r] === 1) {
            ones.push(r);
            sum += 1;
        }
        if (sum > goal && ones.length > 0) {
            sum -= 1;
            l = ones.shift() + 1;
        }
        if (sum === goal) {
            ans += (ones.length > 0 ? ones[0] : nums.length) - l + 1;
        }
    }
    return ans;
};
