function minSteps(s: string, t: string): number {
    function countOf(s: string): Map<string, number> {
        const counter = new Map();
        for (const c of s) {
            if (!counter.has(c)) {
                counter.set(c, 0);
            }
            counter.set(c, counter.get(c) + 1);
        }
        return counter;
    }

    const countS = countOf(s), countT = countOf(t);
    for (const c of countT.keys()) {
        if (!countS.has(c)) {
            countS.set(c, 0);
        }
        countS.set(c, countS.get(c) - countT.get(c));
    }
    let diff = 0;
    for (const v of countS.values()) {
        diff += Math.abs(v);
    }
    return Math.ceil(diff / 2);
};
