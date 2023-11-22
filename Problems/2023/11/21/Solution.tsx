function countNicePairs(nums: number[]): number {
    const mod = 10 ** 9 + 7
    function rev(num: number): number {
        return Number([...num.toString()].reverse().join(''));
    }

    const diff = [];
    for (const num of nums) {
        diff.push(num - rev(num));
    }

    const counter = new Map();
    for (const d of diff) {
        if (!counter.has(d)) {
            counter.set(d, 0);
        }
        counter.set(d, counter.get(d) + 1);
    }

    let ans = 0
    for (const d of diff) {
        ans += counter.get(d) - 1;
    }

    return ans / 2 % mod;
};
