function maxUniqueSplit(s: string): number {
    const seen = new Set();
    let ans = 1;
    const helper = (i, j, count) => {
        if (i === s.length) {
            ans = Math.max(ans, count);
            return;
        }
        if (j > s.length) {
            return;
        }
        helper(i, j+1, count);
        const substr = s.substring(i, j);
        if (seen.has(substr)) {
            return;
        }
        seen.add(substr);
        helper(j, j+1, count+1);
        seen.delete(substr);
    }

    helper(0, 1, 0);

    return ans;
};
