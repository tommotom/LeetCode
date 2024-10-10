function maxWidthRamp(nums: number[]): number {
    const minIndex = (arr, num) => {
        let l = 0, r = arr.length;
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (arr[m][0] <= num) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l === arr.length ? Number.MAX_SAFE_INTEGER : arr[l][1];
    }

    const st = [];
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        ans = Math.max(ans, i - minIndex(st, nums[i]));
        if (st.length === 0 || st[st.length-1][0] > nums[i]) {
            st.push([nums[i], i]);
        }
    }
    return ans;
};
