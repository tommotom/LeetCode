function change(amount: number, coins: number[]): number {
    coins.sort((a, b) => b - a);
    const memo: Map<string, number> = new Map();

    function helper(i: number, amount: number): number {
        if (amount === 0) {
            return 1;
        }
        if (i+1 === coins.length) {
            return amount % coins[i] === 0 ? 1 : 0;
        }
        const key: string = i.toString() + " " + amount.toString();
        if (memo.has(key)) {
            return memo.get(key);
        }
        let ret = i+1 < coins.length ? helper(i+1, amount) : 0;
        while (amount - coins[i] >= 0) {
            amount -= coins[i];
            ret += helper(i+1, amount);
        }
        memo.set(key, ret);
        return ret;
    }

    return helper(0, amount);
};
