function minOperations(s: string): number {
    let zero = 0, one = 0;
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === (i%2).toString()) {
            one++;
        } else {
            zero++;
        }
    }
    return Math.min(zero, one);
};
