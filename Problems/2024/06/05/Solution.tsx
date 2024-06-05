function commonChars(words: string[]): string[] {
    const toArray = (a) => {
        const arr = [];
        for (const k of a.keys()) {
            for (let i = 0; i < a.get(k); i++) {
                arr.push(k);
            }
        }
        return arr;
    }

    const intersection = (a, b) => {
        const c = new Map();
        for (const k of a.keys()) {
            if (b.has(k)) {
                c.set(k, Math.min(a.get(k), b.get(k)));
            }
        }
        return c;
    }

    const count = word => {
        const counter = new Map();
        for (const c of word) {
            if (!counter.has(c)) {
                counter.set(c, 0);
            }
            counter.set(c, counter.get(c) + 1);
        }
        return counter;
    }

    return toArray(words.map(word => count(word)).reduce((a, b) =>  intersection(a, b)));
};
