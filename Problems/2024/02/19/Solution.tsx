function isPowerOfTwo(n: number): boolean {
    const str = (n >>> 0).toString(2);
    let count = 0;
    for (const c of str) {
        count += c === '1' ? 1 : 0;
    }
    return n > 0 && count === 1;
};
