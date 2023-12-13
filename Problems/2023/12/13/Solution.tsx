function numSpecial(mat: number[][]): number {
    const rowCount = new Map();
    const colCount = new Map();
    for (let i = 0;  i < mat.length; i++) {
        rowCount.set(i, 0);
        for (let j = 0; j < mat[0].length; j++) {
            if (!colCount.has(j)) {
                colCount.set(j, 0);
            }
            if (mat[i][j] === 1) {
                rowCount.set(i, rowCount.get(i) + 1);
                colCount.set(j, colCount.get(j) + 1);
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < mat.length; i++) {
        for (let j = 0; j < mat[0].length; j++) {
            if (mat[i][j] === 1 && rowCount.get(i) === 1 && colCount.get(j) === 1) {
                ans++;
            }
        }
    }
    return ans;
};
