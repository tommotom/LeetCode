function checkArithmeticSubarrays(nums: number[], l: number[], r: number[]): boolean[] {
    const ans = [];
    for (let i = 0; i < l.length; i++) {
        const seq = [];
        for (let j = l[i]; j <= r[i]; j++) {
            seq.push(nums[j]);
        }
        seq.sort((a, b) => a - b);

        let valid = true;
        for (let j = 1; j < seq.length-1; j++) {
            if (seq[j+1] - seq[j] !== seq[1] - seq[0]) {
                valid = false;
                break;
            }
        }

        ans.push(valid);
    }

    return ans;
};
