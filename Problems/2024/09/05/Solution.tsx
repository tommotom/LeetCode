function missingRolls(rolls: number[], mean: number, n: number): number[] {
    let left = mean * (n + rolls.length) - rolls.reduce((a, b) => a + b);
    const ans = [];
    for (let i = 0; i < n; i++) {
        const num = Math.floor(left / (n-i));
        if (num > 6 || num < 1) {
            return [];
        }
        ans.push(num)
        left -= num;
    }
    return ans;
};
