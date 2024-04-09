function minRemoveToMakeValid(s: string): string {
    const validate = (s: string[], isLtoR: boolean) => {
        const arr = [], d = isLtoR ? 1 : -1;
        let level = 0;
        for (const c of s) {
            if (c === '(') {
                level += d;
            } else if (c === ')') {
                level -= d;
            }
            if (level >= 0) {
                arr.push(c);
            } else {
                level = 0;
            }
        }
        return arr;
    }
    return validate(validate(s.split('').reverse(), false).reverse(), true).join('');
};
