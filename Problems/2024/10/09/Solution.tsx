function minAddToMakeValid(s: string): number {
    let level = 0, ans = 0;
    for (const c of s.split('')) {
        if (c === '(') {
            level++;
        } else {
            level--;
        }
        if (level < 0) {
            ans++;
            level++;
        }
    }

    return ans + level;
};
