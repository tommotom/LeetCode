function longestStrChain(words: string[]): number {

    function isPredecessor(wordA: string, wordB: string): boolean {
        if (wordA.length + 1 !== wordB.length) {
            return false;
        }
        let inserted = false;
        let i = 0, j = 0;
        while (i < wordA.length) {
            if (wordA.charAt(i) !== wordB.charAt(j)) {
                if (inserted) {
                    return false;
                }
                inserted = true;
                j++;
            } else {
                i++;
                j++;
            }
        }
        return true;
    }

    words.sort((a, b) => a.length - b.length);
    let prev = [], cur = [];
    const len = new Map();
    for (const word of words) {
        len.set(word, 1);
        if (cur.length > 0 && cur[0].length !== word.length) {
            prev = cur;
            cur = [];
        }
        for (const p of prev) {
            if (isPredecessor(p, word)) {
                len.set(word, Math.max(len.get(word), len.get(p) + 1));
            }
        }
        cur.push(word);
    }

    return Math.max(...len.values());
};
