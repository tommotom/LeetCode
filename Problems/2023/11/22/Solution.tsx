function findDiagonalOrder(nums: number[][]): number[] {
    const m = nums.length;
    const n = nums.map(r => r.length).reduce((a, b) => Math.max(a, b));

    const ans = [];
    let r = 0, c = 0;
    while(c < n) {
        let i = r, j = c;
        while (i >= 0) {
            if (j < nums[i].length) {
                ans.push(nums[i][j]);
            }
            i--;
            j++;
        }
        if (r+1 < m) {
            r++;
        } else {
            c++;
        }
    }
    return ans;
};
