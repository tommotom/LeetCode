function findLongestChain(pairs: number[][]): number {
    pairs.sort((a, b) => a[1] - b[1]);
    const length = [...Array(pairs.length)].map(_=> 0);

    function getPrev(i: number): number {
        let ret = 0;
        for (let j = i-1; j >= 0; j--) {
            if (pairs[j][1] < pairs[i][0]) {
                ret = Math.max(ret, length[j]);
            }
        }
        return ret;
    }

    for (let i = 0; i < pairs.length; i++) {
        length[i] = getPrev(i) + 1;
    }
    return length.reduce((a, b) => Math.max(a, b));
};
