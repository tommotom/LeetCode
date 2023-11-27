function largestSubmatrix(matrix: number[][]): number {
    const m = matrix.length, n = matrix[0].length;
    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i > 0 && matrix[i-1][j] > 0 && matrix[i][j] > 0) {
                matrix[i][j] += matrix[i-1][j];
            }
        }

        const cur = [...matrix[i]].sort((a, b) => b - a);
        for (let j = 0; j < n; j++) {
            ans = Math.max(ans, (j+1) * cur[j]);
        }
    }
    return ans;
};
