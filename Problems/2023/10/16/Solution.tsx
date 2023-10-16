function getRow(rowIndex: number): number[] {
    if (rowIndex === 0) {
        return [1];
    }
    const prev = getRow(rowIndex-1);
    const cur = [1];
    for (let i = 1; i < prev.length; i++) {
        cur.push(prev[i-1] + prev[i]);
    }
    cur.push(1);
    return cur;
};
