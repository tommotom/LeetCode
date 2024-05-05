function wonderfulSubstrings(word: string): number {
    const counter = new Map();
    counter.set(0, 1);
    let mask = 0, ans = 0;
    for (const c of word) {
        const bit = c.charCodeAt(0) - 'a'.charCodeAt(0);
        mask ^= (1 << bit);
        if (counter.has(mask)) {
            ans += counter.get(mask);
        } else {
            counter.set(mask, 0);
        }
        counter.set(mask, counter.get(mask) + 1);

        for (let i = 0; i < 11; i++) {
            const tmp = mask ^ (1 << i);
            if (counter.has(tmp)) {
                ans += counter.get(tmp);
            }
        }
    }
    return ans
};
