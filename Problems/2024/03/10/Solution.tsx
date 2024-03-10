function intersection(nums1: number[], nums2: number[]): number[] {
    const numSet1 = new Set(nums1);
    const seen = new Set();
    return nums2.filter((a) => {
        const result = numSet1.has(a) && !seen.has(a);
        seen.add(a);
        return result;
    });
};
