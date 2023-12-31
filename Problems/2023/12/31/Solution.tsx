function maxLengthBetweenEqualCharacters(s: string): number {
    const first = new Map(), last = new Map();
    for (let i = 0; i < s.length; i++) {
        if (!first.has(s.charAt(i))) {
            first.set(s.charAt(i), i);
        }
        last.set(s.charAt(i), i);
    }
    let ans = -1;
    for (const c of first.keys()) {
        if (last.has(c)) {
            ans = Math.max(ans, last.get(c) - first.get(c) - 1);
        }
    }
    return ans;
};
