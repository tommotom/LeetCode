function subarraysDivByK(nums: number[], k: number): number {
    const counter = new Map();
    counter.set(0, 1);
    let ans = 0, sum = 0;
    for (const num of nums) {
        sum += num;
        if (sum < 0) {
            sum += Math.ceil(Math.abs(sum) / k) * k;
        }
        const mod = sum % k;
        if (!counter.has(mod)) {
            counter.set(mod, 0);
        }
        ans += counter.get(mod);
        counter.set(mod, counter.get(mod) + 1);
    }
    return ans;
};
