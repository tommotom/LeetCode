function minKBitFlips(nums: number[], k: number): number {
    let cur = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i >= 0 && nums[i-k] === 2) {
            cur--;
        }

        if (cur % 2 === nums[i]) {
            if (i + k > nums.length) {
                return -1;
            }
            nums[i] = 2;
            cur++;
            ans++;
        }
    }
    return ans;
};
