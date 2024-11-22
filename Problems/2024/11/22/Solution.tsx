function maxEqualRowsAfterFlips(matrix: number[][]): number {
    const counter = new Map();
    for (const row of matrix) {
        const arr = [];
        for (let i = 0; i < row.length; i++) {
            arr.push(row[0] === row[i] ? "T" : "F");
        }
        const key = arr.join('');
        if (!counter.has(key)) {
            counter.set(key, 0);
        }
        counter.set(key, counter.get(key) + 1);
    }
    let ans = 0;
    for (const v of counter.values()) {
        ans = Math.max(ans, v);
    }
    return ans;
};
