function findLeastNumOfUniqueInts(arr: number[], k: number): number {
    const c = new Map();
    for (const a of arr) {
        if (!c.has(a)) {
            c.set(a, 0);
        }
        c.set(a, c.get(a) + 1);
    }
    arr.sort((a, b) => c.get(a) === c.get(b) ? a - b : c.get(a) - c.get(b));
    const ans = new Set();
    for (let i = k; i < arr.length; i++) {
        ans.add(arr[i]);
    }
    return ans.size;
};
