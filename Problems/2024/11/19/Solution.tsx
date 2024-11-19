function maximumSubarraySum(nums: number[], k: number): number {
    const counter = new Map();
    let sum = 0, ans = 0;

    for (let i = 0; i < nums.length; i++) {
        if (i >= k) {
            counter.set(nums[i-k], counter.get(nums[i-k]) - 1);
            if (counter.get(nums[i-k]) === 0) {
                counter.delete(nums[i-k]);
            }
            sum -= nums[i-k];
        }

        if (!counter.has(nums[i])) {
            counter.set(nums[i], 0);
        }
        counter.set(nums[i], counter.get(nums[i]) + 1);
        sum += nums[i];

        if (counter.size === k) {
            ans = Math.max(ans, sum);
        }
    }

    return ans;
};
