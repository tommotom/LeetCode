function checkSubarraySum(nums: number[], k: number): boolean {
    let sum = 0, last = 0;
    const seen = new Set();
    for (const n of nums) {
        sum = (sum + n) % k;
        if (seen.has(sum)) {
            return true;
        }
        seen.add(last);
        last = sum;
    }
    return false;
};
