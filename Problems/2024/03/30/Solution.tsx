class Counter {

    counter: Map<number, number>;

    constructor() {
        this.counter = new Map();
    }

    inc(num: number): void {
        if (!this.counter.has(num)) {
            this.counter.set(num, 1);
        } else {
            this.counter.set(num, this.counter.get(num) + 1);
        }
    }

    get(num: number): number {
        return this.counter.has(num) ? this.counter.get(num) : 0;
    }

    size(): number {
        return this.counter.size;
    }

    dec(num: number): void {
        this.counter.set(num, this.counter.get(num) - 1);
        if (this.counter.get(num) === 0) {
            this.counter.delete(num);
        }
    }
}

function subarraysWithKDistinct(nums: number[], k: number): number {
    let l = 0, ans = 0;
    const counter = new Counter();
    for (let r = 0; r < nums.length; r++) {
        const num = nums[r];
        counter.inc(num);
        while (counter.size() === k+1) {
            counter.dec(nums[l++]);
        }
        if (counter.size() === k) {
            let validTill = l;
            const reduce = new Counter();
            while (true) {
                const n = nums[validTill];
                reduce.inc(n);
                if (reduce.get(n) === counter.get(n)) {
                    break;
                }
                validTill++;
            }
            ans += validTill - l + 1;
        }
    }
    return ans
};
