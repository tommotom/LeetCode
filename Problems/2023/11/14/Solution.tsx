function countPalindromicSubsequence(s: string): number {
    const counts = [];
    const firsts = Array(26).fill(null);
    const lasts = Array(26).fill(null);
    let count = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        const j = s.charCodeAt(i) - "a".charCodeAt(0);
        count[j] += 1;
        counts.push(count);
        count = [...count];

        if (firsts[j] === null) {
            firsts[j] = i;
        }
        lasts[j] = i;
    }

    let ans = 0;
    for (let i = 0; i < 26; i++) {
        const f = firsts[i], l = lasts[i];
        if (f === l) {
            continue;
        }
        for (let j = 0; j< 26; j++) {
            ans += counts[l-1][j] > counts[f][j] ? 1 : 0;
        }
    }

    return ans;
};
