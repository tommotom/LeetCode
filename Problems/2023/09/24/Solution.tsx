function champagneTower(poured: number, query_row: number, query_glass: number): number {
    let prev = [poured];
    for (let row = 1; row <= query_row; row++) {
        let cur = [...Array(row+1)].map(_ => 0);
        for (let col = 0; col < row; col++) {
            if (prev[col] < 1) {
                continue;
            }
            cur[col] += (prev[col] - 1) / 2;
            cur[col+1] += (prev[col] - 1) / 2;
        }
        prev = cur;
    }
    return Math.min(prev[query_glass], 1);
};
