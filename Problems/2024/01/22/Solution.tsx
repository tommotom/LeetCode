function findErrorNums(nums: number[]): number[] {
    const seen = new Set();
    const ans = [];
    let sum = 0;
    for (const num of nums) {
        if (seen.has(num)) {
            ans.push(num);
        }
        sum += num;
        seen.add(num);
    }
    const n = nums.length;
    ans.push((n * (n+1) / 2) - sum + ans[0]);
    return ans;
};
