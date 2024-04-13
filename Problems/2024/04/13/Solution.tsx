function maximalRectangle(matrix: string[][]): number {
    const zeros = [];
    for (const row of matrix) {
        const zero = [0];
        for (const r of row) {
            zero.push(zero[zero.length-1] + (r === '0' ? 1 : 0));
        }
        zeros.push(zero);
    }

    let ans = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            let c = matrix[i].length;
            let r = i;
            while (r < zeros.length) {
                while (zeros[r][j] < zeros[r][c]) {
                    c--;
                }
                if (c === j) {
                    break;
                }
                ans = Math.max(ans, (r - i + 1) * (c - j));
                r++;
            }
        }
    }

    return ans;
};
