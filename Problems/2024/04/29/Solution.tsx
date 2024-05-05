function minOperations(nums: number[], k: number): number {
    const xor = nums.reduce((a, b) => a ^ b);
    let ans = 0;
    for (let i = 0; i < 32; i++) {
        if ((xor & (1 << i)) !== (k & (1 << i))) {
            ans++;
        }
    }
    return ans;
};
