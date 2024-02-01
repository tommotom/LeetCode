function divideArray(nums: number[], k: number): number[][] {
    nums.sort((a, b) => a - b);
    const ans = [];
    let i = 0;
    while (i < nums.length) {
        const arr = [];
        arr.push(nums[i++]);
        arr.push(nums[i++]);
        arr.push(nums[i++]);
        if (arr[2] - arr[0] > k) {
            return [];
        }
        ans.push(arr);
    }
    return ans;
};
