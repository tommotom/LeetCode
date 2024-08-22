function findComplement(num: number): number {
    const bin = [];
    while (num > 0) {
        bin.push(num % 2);
        num = Math.floor(num / 2);
    }
    let ans = 0;
    while (bin.length > 0) {
        ans *= 2;
        ans += bin.pop() ^ 1;
    }
    return ans;
};
