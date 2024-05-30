function countTriplets(arr: number[]): number {
    const prefix = [0, ...arr];
    for (let i = 0; i < arr.length; i++) {
        prefix[i+1] ^= prefix[i];
    }

    let ans = 0;
    for (let start = 0; start < prefix.length; start++) {
        for (let end = start+1; end < prefix.length; end++) {
            if (prefix[start] === prefix[end]) {
                ans += end - start - 1;
            }
        }
    }
    return ans;
};
