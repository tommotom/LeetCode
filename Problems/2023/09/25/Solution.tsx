function findTheDifference(s: string, t: string): string {
    function count(str: string): Map<string, number> {
        const counter = new Map();
        for (const c of str) {
            if (!counter.has(c)) {
                counter.set(c, 0);
            }
            counter.set(c, counter.get(c) + 1);
        }
        return counter;
    }

    const sCount = count(s);
    const tCount = count(t);

    for (const c of tCount.keys()) {
        if (!sCount.has(c)) {
            return c;
        }
        if (sCount.get(c) < tCount.get(c)) {
            return c;
        }
    }
};
