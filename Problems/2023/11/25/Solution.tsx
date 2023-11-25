function getSumAbsoluteDifferences(nums: number[]): number[] {
    let left = 0, right = nums.reduce((a, b) => a + b);
    const ans = [];
    for (let i = 0; i < nums.length; i++) {
        left += nums[i];
        right -= nums[i];
        ans.push(right - nums[i] * (nums.length - i - 1) + nums[i] * (i+1) - left);
    }
    return ans;
};
