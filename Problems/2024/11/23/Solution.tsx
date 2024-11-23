function rotateTheBox(box: string[][]): string[][] {
    const m = box.length, n = box[0].length;
    const ans = Array(n).fill(0).map(_ => Array(m).fill('.'));

    const fill = (count, row, col) => {
        for (let r = row - 1; r >= 0; r--) {
            if (count === 0) {
                break;
            }
            ans[r][col] = '#'
            count--;
        }
    }

    for (let r = 0; r < m; r++) {
        let leaves = 0;
        for (let c = 0; c < n; c++) {
            if (box[r][c] === '#') {
                leaves++;
            } else if (box[r][c] === '*') {
                ans[c][m - r - 1] = '*'
                fill(leaves, c, m - r - 1);
                leaves = 0;
            }
        }
        fill(leaves, n, m - r - 1);
    }
    return ans;
};
