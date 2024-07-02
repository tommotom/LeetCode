function intersect(nums1: number[], nums2: number[]): number[] {
    const counter = new Map();
    for (const num of nums1) {
        if (!counter.has(num)) {
            counter.set(num, 0);
        }
        counter.set(num, counter.get(num) + 1);
    }
    const ans = [];
    for (const num of nums2) {
        if (counter.has(num) && counter.get(num) > 0) {
            ans.push(num);
            counter.set(num, counter.get(num) - 1);
        }
    }
    return ans;
};
