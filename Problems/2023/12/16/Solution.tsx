function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }

    for (const c of t) {
        if (!counter.has(c) || counter.get(c) === 0) {
            return false;
        }
        counter.set(c, counter.get(c) - 1);
    }

    return true;
};
