function tribonacci(n: number): number {
    const memo = new Map([[0, 0], [1, 1], [2, 1]]);
    const helper = n => {
        if (!memo.has(n)) {
            memo.set(n, helper(n-3) + helper(n-2) + helper(n-1));
        }
        return memo.get(n);
    }
    return helper(n);
};
