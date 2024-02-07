function frequencySort(s: string): string {
    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }
    return s.split('')
        .sort(
            (a, b) => counter.get(a) !== counter.get(b)
                ? counter.get(b) - counter.get(a)
                : a.charCodeAt(0) - b.charCodeAt(0))
        .join('');
};
