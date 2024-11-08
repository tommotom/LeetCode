function getMaximumXor(nums: number[], maximumBit: number): number[] {
    const ans = [];
    let xor = nums.reduce((a, b) => a ^ b);
    for (let i = nums.length-1; i >= 0; i--) {
        let k = 0;
        for (let bit = 0; bit < maximumBit; bit++) {
            if ((Math.pow(2, bit) & xor) === 0) {
                k |= Math.pow(2, bit);
            }
        }
        ans.push(k);
        xor ^= nums[i];
    }
    return ans;
};
