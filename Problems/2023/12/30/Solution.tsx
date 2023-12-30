function makeEqual(words: string[]): boolean {
    const counter = new Map();
    for (const word of words) {
        for (const w of word) {
            if (!counter.has(w)) {
                counter.set(w, 0);
            }
            counter.set(w, counter.get(w) + 1);
        }
    }
    const n = words.length;
    for (const c of counter.values()) {
        if (c % n !== 0) {
            return false;
        }
    }
    return true;
};
