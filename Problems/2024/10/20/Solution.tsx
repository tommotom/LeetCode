function parseBoolExpr(e: string): boolean {
    const pair = new Map();
    const st = [];
    for (let i = 0; i < e.length; i++) {
        if (e.charAt(i) === '(') {
            st.push(i);
        } else if (e.charAt(i) === ')') {
            pair.set(st.pop(), i);
        }
    }

    const helper = (i, j) => {
        if (j - i === 1) {
            return e.charAt(i) === 't';
        }
        if (e.charAt(i) === '!') {
            return !helper(i+2, pair.get(i+1));
        }
        const parsed = [];
        let last = i+2, level = 0;
        for (let k = i+3; k < j; k++) {
            if (e.charAt(k) === ',' && level === 0) {
                parsed.push([last, k]);
                last = k+1;
            } else if (e.charAt(k) === '(') {
                level++;
            } else if (e.charAt(k) === ')') {
                level--;
            }
        }
        parsed.push([last, j-1]);
        return e.charAt(i) === '&'
            ? parsed.reduce((a, b) => a && helper(b[0], b[1]), true)
            : parsed.reduce((a, b) => a || helper(b[0], b[1]), false);
    }

    return helper(0, e.length);
};
