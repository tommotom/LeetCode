function uncommonFromSentences(s1: string, s2: string): string[] {
    const counter = new Map();
    for (const word of s1.split(' ')) {
        if (!counter.has(word)) {
            counter.set(word, 0);
        }
        counter.set(word, counter.get(word) + 1);
    }
    for (const word of s2.split(' ')) {
        if (!counter.has(word)) {
            counter.set(word, 0);
        }
        counter.set(word, counter.get(word) + 1);
    }
    const ans = [];
    for (const [k, v] of counter.entries()) {
        if (v === 1) {
            ans.push(k);
        }
    }
    return ans;
};
