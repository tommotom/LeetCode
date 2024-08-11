function numMagicSquaresInside(grid: number[][]): number {
    const rowSum = (i, j) => {
        return grid[i][j] + grid[i][j+1] + grid[i][j+2];
    }

    const colSum = (i, j) => {
        return grid[i][j] + grid[i+1][j] + grid[i+2][j];
    }

    const isDistinct = (i, j) => {
        const nums = new Set();
        for (let r = i; r < i + 3; r++) {
            for (let c = j; c < j + 3; c++) {
                if (grid[r][c] < 1 || grid[r][c] > 9) {
                    return false;
                }
                nums.add(grid[r][c]);
            }
        }
        return nums.size === 9;
    };

    const isSameSum = (i, j) => {
        const sum = rowSum(i, j);
        for (let r = i + 1; r < i + 3; r++) {
            if (sum !== rowSum(r, j)) {
                return false;
            }
        }
        for (let c = j; c < j + 3; c++) {
            if (sum !== colSum(i, c)) {
                return false;
            }
        }
        return grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] === sum && grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] === sum;
    }

    let ans = 0;
    for (let i = 0; i < grid.length - 2; i++) {
        for (let j = 0; j < grid[0].length - 2; j++) {
            if (isDistinct(i, j) && isSameSum(i, j)) {
                ans++;
            }
        }
    }
    return ans;
};
