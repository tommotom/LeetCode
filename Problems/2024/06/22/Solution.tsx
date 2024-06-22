function numberOfSubarrays(nums: number[], k: number): number {
    const odds = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % 2 === 1) {
            odds.push(i);
        }
    }

    let ans = 0, l = 0;
    for (let r = k-1; r < odds.length; r++) {
        const left = odds[r-k+1] - (r === k - 1 ? -1 : odds[r - k]);
        const right = (r === odds.length - 1 ? nums.length : odds[r+1]) - odds[r];
        ans += left * right;
    }
    return ans;
};
