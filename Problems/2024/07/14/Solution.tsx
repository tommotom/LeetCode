function countOfAtoms(formula: string): string {
    const isDigit = c => '0' <= c && c <= '9';
    const isLower = c => 'a' <= c && c <= 'z';

    const pair = new Map();
    const st = [];
    for (let i = 0; i < formula.length; i++) {
        if (formula.charAt(i) === '(') {
            st.push(i);
        } else if (formula.charAt(i) === ')') {
            pair.set(st.pop(), i);
        }
    }

    const helper = (start, end) => {
        const counter = new Map();
        for (let i = start; i < end; i++) {
            if (formula.charAt(i) === '(') {
                const child = helper(i+1, pair.get(i));
                i = pair.get(i) + 1;
                let j = i;
                while (isDigit(formula.charAt(j))) {
                    j++;
                }
                const num = i < j ? Number(formula.substring(i, j)) : 1;
                for (const [k, v] of child.entries()) {
                    if (!counter.has(k)) {
                        counter.set(k, 0);
                    }
                    counter.set(k, counter.get(k) + child.get(k) * num);
                }
                i = j-1;
            } else if (formula.charAt(i) === ')') {
                continue;
            } else {
                let j = i + 1;
                while (isLower(formula.charAt(j))) {
                    j++;
                }
                const atom = formula.substring(i, j);
                i = j;
                while (isDigit(formula.charAt(j))) {
                    j++;
                }
                const num = i < j ? Number(formula.substring(i, j)) : 1;
                if (!counter.has(atom)) {
                    counter.set(atom, 0);
                }
                counter.set(atom, counter.get(atom) + num);
                i = j - 1;
            }
        }
        return counter
    }

    const arr = [];
    for (const [k, v] of helper(0, formula.length).entries()) {
        arr.push([k, v]);
    }
    arr.sort();
    return arr.map(a => a[1] > 1 ? a[0] + a[1] : a[0]).join('');
};
