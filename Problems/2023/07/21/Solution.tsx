function findNumberOfLIS(nums: number[]): number {
    const lengthes = [];
    const counts = [];

    for (let i = 0; i < nums.length; i++) {
        let l = 1;
        let c = 1;
        for (let j = 0; j < lengthes.length; j++) {
            if (nums[j] >= nums[i]) {continue;}
            if (l == lengthes[j] + 1) {
                c += counts[j];
            } else if (l < lengthes[j] + 1) {
                l = lengthes[j] + 1;
                c = counts[j];
            }
        }
        lengthes.push(l);
        counts.push(c);
    }

    const len = lengthes.reduce((a, b) => Math.max(a, b));
    let ans = 0;
    for (let i = 0; i < counts.length; i++) {
        ans = lengthes[i] == len ? ans + counts[i] : ans;
    }
    return ans;
};
