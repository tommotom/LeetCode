function maximumOddBinaryNumber(s: string): string {
    let one = 0;
    for (const c of s) {
        if (c === '1') {
            one++;
        }
    }
    const arr = [];
    for (let i = 0; i < s.length-1; i++) {
        if (one > 1) {
            arr.push('1');
            one--;
        } else {
            arr.push('0');
        }
    }
    arr.push('1');
    return arr.join('');
};
