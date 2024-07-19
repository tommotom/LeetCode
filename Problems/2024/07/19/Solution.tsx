function luckyNumbers (matrix: number[][]): number[] {
    const ans = [];
    for (let i = 0; i < matrix.length; i++) {
        let m = -1, num = Number.MAX_SAFE_INTEGER;
        for (let j = 0; j < matrix[0].length; j++) {
            if (num > matrix[i][j]) {
                m = j;
                num = matrix[i][j];
            }
        }
        let isMax = true;
        for (let r = 0; r < matrix.length; r++) {
            if (num < matrix[r][m]) {
                isMax = false;
                break;
            }
        }
        if (isMax) {
            ans.push(num);
        }
    }
    return ans;
};
