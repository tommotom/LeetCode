function maxScoreWords(words: string[], letters: string[], score: number[]): number {
    let ans = 0;
    const counter = Array(26).fill(0);
    for (const c of letters) {
        counter[c.charCodeAt(0) - "a".charCodeAt(0)]++;
    }
    for (let bit = 1; bit < Math.pow(2, words.length); bit++) {
        const tmp = Array(26).fill(0);
        for (let i = 0; i < words.length; i++) {
            if ((bit & (1 << i)) === 0) {
                continue;
            }
            for (let j = 0; j < words[i].length; j++) {
                tmp[words[i].charCodeAt(j) - "a".charCodeAt(0)]++;
            }
        }
        let valid = true
        for (let i = 0; i < 26; i++) {
            if (tmp[i] > counter[i]) {
                valid = false;
                break;
            }
        }
        if (valid) {
            let s = 0;
            for (let i = 0; i < 26; i++) {
                s += score[i] * tmp[i];
            }
            ans = Math.max(ans, s);
        }
    }
    return ans;
};
