function isNStraightHand(hand: number[], groupSize: number): boolean {
    const counter = new Map();
    for (const h of hand) {
        if (!counter.has(h)) {
            counter.set(h, 0);
        }
        counter.set(h, counter.get(h) + 1);
    }
    const vals = [...counter.keys()].sort((a, b) => a - b);
    for (const v of vals) {
        const c = counter.get(v);
        if (c === 0) {
            continue;
        }
        for (let tmp = 1; tmp < groupSize; tmp++) {
            if (!counter.has(v + tmp) || counter.get(v + tmp) < c) {
                return false;
            }
            counter.set(v + tmp, counter.get(v + tmp) - c);
        }
    }
    return true;
};
