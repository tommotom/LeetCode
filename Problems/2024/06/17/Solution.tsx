function judgeSquareSum(c: number): boolean {
    const seen = new Set();
    for (let num = 0; Math.pow(num, 2) <= c; num++) {
        seen.add(Math.pow(num, 2));
        if (seen.has(c - Math.pow(num, 2))) {
            return true;
        }
    }
    return false;
};
