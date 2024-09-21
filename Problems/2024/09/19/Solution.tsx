function diffWaysToCompute(expression: string): number[] {
    if (!isNaN(Number(expression))) {
        return [Number(expression)];
    }

    const ans = [];

    for (let i = 0; i < expression.length; i++) {
        const c = expression.charAt(i);
        if (!isNaN(Number(c))) {
            continue;
        }
        const lefts = diffWaysToCompute(expression.substring(0, i));
        const rights = diffWaysToCompute(expression.substring(i+1, expression.length));
        for (const l of lefts) {
            for (const r of rights) {
                if (c === '+') {
                    ans.push(l + r);
                } else if (c === '-') {
                    ans.push(l - r);
                } else {
                    ans.push(l * r);
                }
            }
        }
    }

    return ans;
};
