function getAverages(nums: number[], k: number): number[] {
    const ans: Array<number> = new Array(nums.length);
    for (let i = 0; i < ans.length; i++) {
        ans[i] = -1;
    }
    if (2*k+1 > nums.length) {
        return ans;
    }

    let sum = 0;
    for (let i = 0; i < 2*k+1; i++) {
        sum += nums[i];
    }
    for (let i = 2*k+1; i < nums.length; i++) {
        ans[i-k-1] = Math.floor(sum / (2*k+1));
        sum -= nums[i-2*k-1]
        sum += nums[i];
    }
    ans[nums.length-k-1] = Math.floor(sum / (2*k+1));
    return ans;
};
