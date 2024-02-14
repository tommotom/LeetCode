function rearrangeArray(nums: number[]): number[] {
    const p = [], n = [];
    for (const num of nums) {
        if (num > 0) {
            p.push(num);
        } else {
            n.push(num);
        }
    }
    const ans = [];
    for (let i = 0; i < p.length; i++) {
        ans.push(p[i]);
        ans.push(n[i]);
    }
    return ans;
};
