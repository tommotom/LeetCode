function checkValidString(s: string): boolean {
    const valid = (s, d) => {
        let level = 0, any = 0;
        for (const c of s) {
            if (c === '(') {
                level += d;
            } else if (c === ')') {
                level -= d;
            } else {
                any++;
            }
            if (level < 0 && Math.abs(level) > any) {
                return false;
            }
        }
        return Math.abs(level) <= any;
    }
    return valid(s, 1) && valid(s.split('').reverse().join(''), -1);
};
