function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (original.length !== m * n) {
        return [];
    }
    const ans = [];
    let i = 0;
    for (let r = 0; r < m; r++) {
        const row = [];
        for (let c = 0; c < n; c++) {
            row.push(original[i++]);
        }
        ans.push(row);
    }

    return ans;
};
