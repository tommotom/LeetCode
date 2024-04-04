function maxDepth(s: string): number {
    let depth = 0, ans = 0;
    for (const c of s.split('')) {
        if (c === '(') {
            depth++;
        } else if (c === ')') {
            depth--;
        }
        ans = Math.max(ans, depth);
    }
    return ans;
};
