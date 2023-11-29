function hammingWeight(n: number): number {
    let ans = 0;
    while (n > 0) {
        ans += n % 2;
        n = Math.floor(n / 2);
    }
    return ans;
};
