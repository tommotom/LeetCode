function numDecodings(s: string): number {
    const memo = new Map()
    function helper(i: number): number {
        if (i < s.length && s.charAt(i) === '0') {
            return 0;
        }
        if (i+1 === s.length || i === s.length) {
            return 1;
        }
        if (!memo.has(i)) {
            memo.set(i, helper(i+1) + (s.substring(i, i+2) < "27" ? helper(i+2) : 0));
        }
        return memo.get(i);
    }
    return helper(0);
};
