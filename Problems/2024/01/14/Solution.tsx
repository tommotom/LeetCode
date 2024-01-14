function closeStrings(word1: string, word2: string): boolean {
    if (word1.length !== word2.length) {
        return false;
    }

    function stringCounter(word: string): Map<string, number> {
        const counter = new Map();
        for (const c of word) {
            if (!counter.has(c)) {
                counter.set(c, 0);
            }
            counter.set(c, counter.get(c) + 1);
        }
        return counter;
    }

    function numCounter(counter: Map<string, number>): Map<number, number> {
        const countCounter = new Map();
        for (const v of counter.values()) {
            if (!countCounter.has(v)) {
                countCounter.set(v, 0);
            }
            countCounter.set(v, countCounter.get(v) + 1);
        }
        return countCounter;
    }

    const sc1 = stringCounter(word1), sc2 = stringCounter(word2);
    for (const k of sc1.keys()) {
        if (!sc2.has(k)) {
            return false;
        }
    }
    for (const k of sc2.keys()) {
        if (!sc1.has(k)) {
            return false;
        }
    }

    const c1 = numCounter(sc1), c2 = numCounter(sc2);
    for (const key of c1.keys()) {
        if (!c2.has(key) || c1.get(key) !== c2.get(key)) {
            return false;
        }
    }
    return true;
};
