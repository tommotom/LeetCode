function largestPerimeter(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let ans = -1, sum = nums[0] + nums[1];
    for (const num of nums.slice(2)) {
        if (num < sum) {
            ans = sum + num;
        }
        sum += num;
    }
    return ans;
};
