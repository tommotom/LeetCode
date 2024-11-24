function maxMatrixSum(matrix: number[][]): number {
    let sum = 0, min = Number.MAX_SAFE_INTEGER, count = 0;
    for (const row of matrix) {
        for (const num of row) {
            sum += Math.abs(num);
            count += num < 0 ? 1 : 0;
            min = Math.min(min, Math.abs(num));
        }
    }
    return sum - (count % 2 === 1 ? 2 * min : 0);
};
