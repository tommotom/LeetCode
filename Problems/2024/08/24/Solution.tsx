function nearestPalindromic(n: string): string {
    const convert = num => {
        const s = num.toString();
        const n = s.length;
        let l = Math.floor((n-1) / 2), r = Math.floor(n / 2);
        const sArr = [...s];
        while (l >= 0) {
            sArr[r++] = sArr[l--];
        }
        return BigInt(sArr.join(''));
    }

    const prev = num => {
        let l = 0n, r = BigInt(num);
        let ans = -1000000000000000000n;
        while (l <= r) {
            const m = (r - l) / 2n + l;
            const palin = convert(m);
            if (palin < num) {
                ans = palin;
                l = m + 1n;
            } else {
                r = m - 1n;
            }
        }
        return ans;
    }

    const next = num => {
        let l = BigInt(num), r = 1000000000000000000n;
        let ans = -1000000000000000000n;
        while (l <= r) {
            const m = (r - l) / 2n + l;
            const palin = convert(m);
            if (palin > num) {
                ans = palin;
                r = m - 1n;
            } else {
                l = m + 1n;
            }
        }
        return ans;
    }

    const num = BigInt(n);
    const a = prev(num);
    const b = next(num);
    if (Math.abs(Number(a - num)) <= Math.abs(Number(b - num))) {
        return a.toString();
    }
    return b.toString();
};
