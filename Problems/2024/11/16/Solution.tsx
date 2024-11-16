function resultsArray(nums: number[], k: number): number[] {
    const ans = [];
    let len = 1;
    for (let i = 1; i < k - 1; i++) {
        if (nums[i-1] === nums[i] - 1) {
            len++;
        } else {
            len = 1;
        }
    }
    for (let i = k - 1; i < nums.length; i++) {
        if (nums[i-1] === nums[i] - 1) {
            len++;
        } else {
            len = 1;
        }
        ans.push(len >= k ? nums[i] : -1);
    }
    return ans;
};
