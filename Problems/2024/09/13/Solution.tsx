function xorQueries(arr: number[], queries: number[][]): number[] {
    const cum = [0];
    for (const num of arr) {
        cum.push(cum[cum.length-1] ^ num);
    }
    const ans = [];
    for (const [l, r] of queries) {
        ans.push(cum[l] ^ cum[r+1]);
    }
    return ans;
};
