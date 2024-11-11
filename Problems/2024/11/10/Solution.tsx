function minimumSubarrayLength(nums: number[], k: number): number {
    const bitOf = num => {
        const ret = [];
        while (num > 0) {
            ret.push(num % 2);
            num = Math.floor(num / 2);
        }
        return ret;
    }

    const isValid = bits => {
        let bit = 0, num = 0;
        for (const count of bits) {
            if (count > 0) {
                num |= (1 << bit);
            }
            bit++;
        }
        return num >= k;
    }

    let ans = Number.MAX_SAFE_INTEGER, i = 0;
    const bits = Array(32).fill(0);
    for (let j = 0; j < nums.length; j++) {
        const cur = bitOf(nums[j]);
        for (let bit = 0; bit  < cur.length; bit++) {
            bits[bit] += cur[bit];
        }
        while (i <= j && isValid(bits)) {
            ans = Math.min(ans, j - i + 1);
            const sub = bitOf(nums[i++]);
            for (let bit = 0; bit < sub.length; bit++) {
                bits[bit] -= sub[bit];
            }
        }
    }

    return ans === Number.MAX_SAFE_INTEGER ? -1: ans;
};
