function maxValue(n: number, index: number, maxSum: number): number {
    let l = 0;
    let r = maxSum+1;
    while (l < r) {
        const m = Math.floor(l+ (r - l) / 2);
        const leftSum = sumFor(m-1, index);
        const rightSum = sumFor(m, n-index);
        if (leftSum + rightSum <= maxSum) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l - 1;
}

function sumFor(num: number, length: number): number {
    const len = Math.min(length, num);
    return (num + (num - len + 1)) * len / 2 + length - len;
}
