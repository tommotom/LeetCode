function findMatrix(nums: number[]): number[][] {
    const counter = new Map();
    for (const num of nums) {
        if (!counter.has(num)) {
            counter.set(num, 0);
        }
        counter.set(num, counter.get(num) + 1);
    }

    const ans = [];
    while (counter.size > 0) {
        const arr = [];
        for (const key of counter.keys()) {
            if (counter.get(key) > 0) {
                arr.push(key);
                counter.set(key, counter.get(key) - 1);
                if (counter.get(key) === 0) {
                    counter.delete(key);
                }
            }
        }
        if (arr.length > 0) {
            ans.push(arr);
        }
    }
    return ans;
};
