function singleNumber(nums: number[]): number {
    let ans = 0
    for (let i = 0; i < 32; i++) {
        let sum = 0;
        for (const num of nums) {
            sum += (num >> i) & 1;
        }
        sum %= 3;
        ans |= (sum << i);
    }
    return ans
};
