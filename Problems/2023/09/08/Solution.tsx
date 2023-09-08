function generate(numRows: number): number[][] {
    function nextRow(row: number[]): number[] {
        const ret = [1];
        for (let i = 0; i < row.length-1; i++) {
            ret.push(row[i] + row[i+1]);
        }
        ret.push(1);
        return ret;
    }

    const ans = [[1]];
    for (let i = 1; i < numRows; i++) {
        ans.push(nextRow(ans[ans.length-1]));
    }
    return ans;
};
