function kWeakestRows(mat: number[][], k: number): number[] {
    return mat.map((arr, i) => [arr.reduce((a, b) => a + b), i])
        .sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0])
        .slice(0, k)
        .map(a => a[1]);
};
