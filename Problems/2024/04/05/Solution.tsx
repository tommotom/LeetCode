function makeGood(s: string): string {
    const isUpper = (c: string) => c === c.toUpperCase();
    const isNotGood = (a: string, b: string) => a.toLowerCase() === b.toLowerCase() && isUpper(a) !== isUpper(b);
    const ans = [];
    for (const c of s.split('')) {
        ans.push(c);
        if (ans.length > 1 && isNotGood(ans[ans.length-1], ans[ans.length-2])) {
            ans.pop();
            ans.pop();
        }
    }
    return ans.join('');
};
