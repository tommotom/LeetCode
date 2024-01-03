function numberOfBeams(bank: string[]): number {
    function count(row: string): number {
        let ret = 0;
        for (const c of row) {
            if (c === '1') {
                ret++;
            }
        }
        return ret;
    }
    let last = count(bank[0]), ans = 0;
    for (let i = 1; i < bank.length; i++) {
        const cur = count(bank[i]);
        if (cur > 0) {
            ans += last * cur;
            last = cur;
        }
    }
    return ans;
};
