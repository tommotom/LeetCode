function knightDialer(n: number): number {
    const nexts = new Map([[1, [6, 8]], [2, [7, 9]], [3, [4, 8]], [4, [0, 3, 9]], [5, []], [6, [0, 1, 7]], [7, [2, 6]], [8, [1, 3]], [9, [2, 4]], [0, [4, 6]]]);
    const nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    const mod = 1000000007;
    const memo = new Map();

    function helper(n: number, num: number): number {
        if (n === 1) {
            return 1;
        }
        if (num === 5) {
            return 0;
        }
        const key = n.toString() + " " + num.toString();
        if (!memo.has(key)) {
            memo.set(key, nexts.get(num).map(next => helper(n-1, next)).reduce((a, b) => (a + b) % mod));
        }
        return memo.get(key);
    }

    return nums.map(num => helper(n, num)).reduce((a, b) => (a + b) % mod);
};
