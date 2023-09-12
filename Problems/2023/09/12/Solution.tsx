function minDeletions(s: string): number {
    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }

    const numCounter = new Map();
    for (const c of counter.values()) {
        if (!numCounter.has(c)) {
            numCounter.set(c, 0);
        }
        numCounter.set(c, numCounter.get(c) + 1);
    }

    let num = 0;
    for (const c of numCounter.keys()) {
        num = Math.max(num, c);
    }

    let ans = 0;
    while (num > 0) {
        if (numCounter.has(num) && numCounter.get(num) > 1) {
            const sup = numCounter.get(num) - 1;
            ans += sup;
            if (!numCounter.has(num-1)) {
                numCounter.set(num-1, 0);
            }
            numCounter.set(num-1, numCounter.get(num-1) + sup);
        }
        num -= 1;
    }

    return ans;
};
