function numSteps(s: string): number {
    let step = 0, carry = 0;
    for (let i = s.length-1; i > 0; i--) {
        const d = Number(s.charAt(i)) + carry;
        if (d % 2 === 1) {
            step += 2;
            carry = 1;
        } else {
            step++;
        }
    }
    return step + carry;
};
