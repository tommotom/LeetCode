function findFarmland(land: number[][]): number[][] {
    const helper = (i, j) => {
        let I = i, J = j;
        while (I+1 < land.length && land[I+1][j] === 1) {
            I++;
        }
        while (J+1 < land[0].length && land[i][J+1] === 1) {
            J++;
        }
        for (let r = i; r < I+1; r++) {
            for (let c = j; c < J+1; c++) {
                land[r][c] = 0;
            }
        }
        return [I, J];
    }

    const ans = [];
    for (let i = 0; i < land.length; i++) {
        for (let j = 0; j < land[0].length; j++) {
            if (land[i][j] === 1) {
                ans.push([i, j, ...helper(i, j)]);
            }
        }
    }
    return ans;
};
