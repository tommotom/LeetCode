function minimumOneBitOperations(n: number): number {
    if (n === 0) {
        return 0;
    }

    let k = 0, cur = 1;
    while (cur * 2 <= n) {
        cur *= 2;
        k++;
    }

    return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ cur);
};
