function integerBreak(n: number): number {
    if (n === 2) {
        return 1;
    }
    if (n === 3) {
        return 2;
    }
    const three = Math.ceil((n-4) / 3);
    return (n - 3 * three) * Math.pow(3, three);
};
