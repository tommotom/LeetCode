function shortestPalindrome(s: string): string {
    const build = s => {
        const ret = Array(s.length).fill(0);
        let len = 0;
        for (let i = 1; i < s.length; i++) {
            while (len > 0 && s.charAt(i) !== s.charAt(len)) {
                len = ret[len-1];
            }
            if (s.charAt(i) === s.charAt(len)) {
                len++;
            }
            ret[i] = len;
        }
        return ret;
    }

    const rev = s.split('').reverse().join('');
    const comb = s + '#' + rev;
    const prefix = build(comb);
    const len = prefix[prefix.length-1];
    const suffix = rev.substring(0, s.length-len);
    return suffix + s;
};
