function minEnd(n: number, x: number): number {
    let ans = BigInt(x);
    let N = BigInt(n-1), X = BigInt(x);
    let mask = 1n

    while (N > 0n) {
        if ((mask & X) == 0n) {
            ans |= (N & 1n) * mask;
            N >>= 1n;
        }
        mask <<= 1n;
    }

    return Number(ans);
};
