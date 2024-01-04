function minOperations(nums: number[]): number {
    const memo = new Map([[0,0], [1,-1], [2,1], [3,1], [4,2]]);
    function del(num: number):number {
        if (num < 5) {
            return memo.get(num);
        }
        const quotient = Math.floor((num-2)/3);
        const remainder = num - 3 * quotient;
        return quotient + memo.get(remainder);
    }

    const counter = new Map();
    for (const num of nums) {
        if (!counter.has(num)) {
            counter.set(num, 0);
        }
        counter.set(num, counter.get(num) + 1);
    }

    let ans = 0;
    for (const c of counter.values()) {
        if (c === 1) {
            return -1;
        }
        ans += del(c);
    }

    return ans;
};
