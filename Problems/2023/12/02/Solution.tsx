function countCharacters(words: string[], chars: string): number {
    function counterOf(word: string): Map<string, number> {
        const counter = new Map();
        for (const c of word) {
            if (!counter.has(c)) {
                counter.set(c, 0);
            }
            counter.set(c, counter.get(c) + 1);
        }
        return counter;
    }

    const dic = counterOf(chars);
    let ans = 0;
    for (const word of words) {
        const counter = counterOf(word);
        let valid = true;
        for (const c of counter.keys()) {
            if (!dic.has(c) || dic.get(c) < counter.get(c)) {
                valid = false;
                break;
            }
        }
        ans += valid ? word.length : 0;
    }

    return ans;
};
