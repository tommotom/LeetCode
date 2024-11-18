function decrypt(code: number[], k: number): number[] {
    const n = code.length;
    if (k === 0) {
        return Array(n).fill(0);
    }

    const arr = code.concat(code);
    const ans = [];
    for (let i = 0; i < n; i++) {
        let sum = 0;
        for (let j = 1; j <= Math.abs(k); j++) {
            sum += k > 0 ? arr[i+j] : arr[i+n-j];
        }
        ans.push(sum);
    }
    return ans;
};
