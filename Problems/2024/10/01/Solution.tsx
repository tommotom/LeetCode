function canArrange(arr: number[], k: number): boolean {
    const counter = new Map();
    for (let num of arr) {
        if (num < 0) {
            num = num + Math.ceil(Math.abs(num) / k) * k;
        }
        const mod = num % k;
        if (!counter.has(mod)) {
            counter.set(mod, 0);
        }
        counter.set(mod, counter.get(mod) + 1);
    }

    for (const [key, val] of counter.entries()) {
        if (key === 0) {
            if (val % 2 === 1) {
                return false;
            }
        } else {
            if (!counter.has(k - key) || counter.get(k - key) !== val) {
                return false;
            }
        }
    }
    return true;
};
