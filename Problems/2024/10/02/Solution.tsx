function arrayRankTransform(arr: number[]): number[] {
    const sorted = arr.map((num, i) => [num, i]).sort((a, b) => a[0] - b[0]);
    const ans = [];
    let rank = 0;
    for (const [num, i] of sorted) {
        if (ans.length === 0 || ans[ans.length-1][2] < num) {
            rank++;
        }
        ans.push([rank, i, num]);
    }
    return ans.sort((a, b) => a[1] - b[1]).map(el => el[0]);
};
