function decodeAtIndex(s: string, k: number): string {
    function isAlpha(c: string): boolean {
        return 'a' <= c && c <= 'z';
    }
    let K = BigInt(k);
    let size:bigint = 0n;
    for (const c of s) {
        if (isAlpha(c)) {
            size += 1n;
        } else {
            size *= BigInt(c);
        }
    }

    const arr = s.split('').reverse();
    for (const c of arr) {
        K %= size;
        if (K === 0n && isAlpha(c)) {
            return c;
        }
        if (isAlpha(c)) {
            size -= 1n;
        } else {
            size /= BigInt(c);
        }
    }

    return '';
};
