function searchMatrix(matrix: number[][], target: number): boolean {
    let u = 0, d = matrix.length;
    while (u < d) {
        const m = u + Math.floor((d - u) / 2);
        if (matrix[m][matrix[0].length-1] < target) {
            u = m + 1;
        } else {
            d = m;
        }
    }
    if (u === matrix.length) {
        return false;
    }
    let l = 0, r = matrix[0].length;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (matrix[u][m] < target) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l < matrix[0].length && matrix[u][l] === target;
};
