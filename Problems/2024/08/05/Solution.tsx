function kthDistinct(arr: string[], k: number): string {
    const counter = new Map();

    for (const c of arr) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }

    for (const c of arr) {
        if (counter.get(c) === 1) {
            k--;
        }
        if (k === 0) {
            return c;
        }
    }

    return "";
};
