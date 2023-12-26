function numRollsToTarget(n: number, k: number, target: number): number {
    const memo = new Map(), mod = 1000000007;
    function helper(n: number, target: number): number {
        if (target === 0 && n === 0) {
            return 1;
        }
        if (target <= 0 || n === 0) {
            return 0;
        }
        const key = n.toString() + "," + target.toString();
            let sum = 0;
            for (let num = 1; num <= k; num++) {
                sum += helper(n-1, target - num);
                sum %= mod;
            }
            memo.set(key, sum);
        }
        return memo.get(key);
    }
    return helper(n, target);
};
