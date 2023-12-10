function transpose(matrix: number[][]): number[][] {
    const m = matrix.length, n = matrix[0].length;
    const arr = [];
    for (let i = 0; i < n; i++) {
        const row = [];
        for (let j = 0; j < m; j++) {
            row.push(matrix[j][i]);
        }
        arr.push(row);
    }
    return arr;
};
