function firstUniqChar(s: string): number {
    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }
    for (let i = 0; i < s.length; i++) {
        if (counter.get(s.charAt(i)) === 1) {
            return i;
        }
    }
    return -1;
};
