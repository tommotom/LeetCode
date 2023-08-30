function minimumReplacement(nums: number[]): number {
    let ans = 0, last = nums.pop();
    while (nums.length > 0) {
        let cur = nums.pop();
        const operations = Math.floor((cur + last - 1) / last);
        ans += operations - 1;
        last = Math.floor(cur / operations);
    }
    return ans;
};
