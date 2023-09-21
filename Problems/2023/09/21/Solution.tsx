function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    if (nums1.length > nums2.length) {
        const tmp = nums1;
        nums1 = nums2;
        nums2 = tmp;
    }
    const m = nums1.length, n = nums2.length;
    let l = 0, r = m;
    while (l <= m) {
        const i = l + Math.floor((r - l) / 2);
        const j = Math.floor((m + n + 1) / 2) - i;

        const X = i === 0 ? Number.MIN_SAFE_INTEGER : nums1[i-1];
        const Y = j === 0 ? Number.MIN_SAFE_INTEGER : nums2[j-1];
        const x = i === m ? Number.MAX_SAFE_INTEGER : nums1[i];
        const y = j === n ? Number.MAX_SAFE_INTEGER : nums2[j];

        if (Y <= x && X <= y) {
            return (m + n) % 2 === 0
                ? (Math.max(X, Y) + Math.min(x, y)) / 2
                : Math.max(X, Y);
        } else if (X > y) {
            r = i - 1;
        } else {
            l = i + 1;
        }
    }
};
