function restoreMatrix(rowSum: number[], colSum: number[]): number[][] {
    const arr = Array(rowSum.length).fill(0).map(_ => Array(colSum.length).fill(0));
    for (let i = 0; i < rowSum.length; i++) {
        for (let j = 0; j < colSum.length; j++) {
            arr[i][j] = Math.min(rowSum[i], colSum[j]);
            rowSum[i] -= arr[i][j];
            colSum[j] -= arr[i][j];
        }
    }
    return arr;
}
