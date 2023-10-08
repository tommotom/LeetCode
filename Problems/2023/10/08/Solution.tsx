function maxDotProduct(nums1: number[], nums2: number[]): number {
    const memo = new Map();
    function helper(i: number, j: number, valid: boolean):number {
        if (i === nums1.length || j === nums2.length) {
            return valid ? 0 : Number.MIN_SAFE_INTEGER;
        }
        const key = i + " " + j + " " + valid;
        if (!memo.has(key)) {
            const ret = [
                helper(i+1, j+1, true) + nums1[i] * nums2[j],
                helper(i+1, j, valid),
                helper(i, j+1, valid)
            ].reduce((a, b) => Math.max(a, b));
            memo.set(key, ret);
        }
        return memo.get(key);
    }
    return helper(0, 0, false);
};
