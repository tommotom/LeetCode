function uniqueOccurrences(arr: number[]): boolean {
    const count = new Map();
    for (const a of arr) {
        if (!count.has(a)) {
            count.set(a, 0);
        }
        count.set(a, count.get(a) + 1);
    }
    const set = new Set();
    for (const v of count.values()) {
        if (set.has(v)) {
            return false;
        }
        set.add(v);
    }
    return true;
};
