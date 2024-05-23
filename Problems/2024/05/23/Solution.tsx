function beautifulSubsets(nums: number[], k: number): number {
    const isValid = bit => {
        const seen = new Set();
        for (let i = 0; i < nums.length; i++) {
            if ((bit & (1 << i)) === 0) {
                continue;
            }
            if (seen.has(nums[i] - k) || seen.has(nums[i] + k)) {
                return false;
            }
            seen.add(nums[i]);
        }
        return true;
    }

    let ans = 0;
    for (let bit = 1; bit < Math.pow(2, nums.length); bit++) {
        if (isValid(bit)) {
            ans++;
        }
    }

    return ans;
};
