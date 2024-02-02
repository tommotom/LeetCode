function sequentialDigits(low: number, high: number): number[] {

    function gen(d: number): number[] {
        const ret = [];
        for (let i = 1; i <= Math.min(9, 10-d); i++) {
            let num = 0;
            for (let j = 1; j <= d; j++) {
                num *= 10;
                num += i+j-1;
            }
            ret.push(num);
        }
        return ret;
    }

    let tmp = low, d = low.toString().length;
    const ans = [];
    while (d > 0) {
        const arr = gen(d);
        if (arr.length === 0) {
            break;
        }
        for (const num of arr) {
            if (num < low) {
                continue;
            }
            if (num > high) {
                d = -1;
                break;
            }
            ans.push(num);
        }
        d++;
    }

    return ans;
};
