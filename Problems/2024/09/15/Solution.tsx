function findTheLongestSubstring(s: string): number {
    const index = new Map([['e', 0], ['i', 1], ['o', 2], ['a', 3], ['u', 4]]);
    const counter = [0, 0, 0, 0, 0];
    const seenAt = new Map([[counter.join(','), -1]]);
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s.charAt(i);
        if (index.has(c)) {
            const j = index.get(c);
            counter[j] = (counter[index.get(c)] + 1) % 2;
        }
        const key = counter.join(',');
        if (seenAt.has(key)) {
            ans = Math.max(ans, i - seenAt.get(key));
        } else {
            seenAt.set(key, i);
        }
    }
    return ans;
};
