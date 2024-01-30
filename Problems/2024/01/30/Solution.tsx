function evalRPN(tokens: string[]): number {
    const op = new Set(['+', '-', '*', '/']);
    const st = [];

    for (const t of tokens) {
        if (op.has(t)) {
            let num1 = st.pop(), num2 = st.pop();
            if (t === '+') {
                st.push(num2 + num1);
            } else if (t === '-') {
                st.push(num2 - num1);
            } else if (t === '*') {
                st.push(num2 * num1);
            } else {
                st.push(num2 * num1 < 0 ? Math.ceil(num2 / num1) : Math.floor(num2 / num1));
            }
        } else {
            st.push(Number(t));
        }
    }

    return st.pop();
};
