function reverseParentheses(s: string): string {
    const st = [], pair = new Map();
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === '(') {
            st.push(i);
        } else if (s.charAt(i) === ')') {
            pair.set(st.pop(), i);
        }
    }

    const arr = [];
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === '(') {
            arr.push(reverseParentheses(s.substring(i+1, pair.get(i))).split('').reverse().join(''));
            i = pair.get(i);
        } else {
            arr.push(s.charAt(i));
        }
    }
    return arr.join('');
};
