function combinationSum2(candidates: number[], target: number): number[][] {
    const counter = new Map();
    for (const c of candidates) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }

    const nums = Array.from(counter.keys());
    nums.sort((a, b) => a - b);

    const ans = []
    const helper = (i, arr, sum) => {
        if (sum === target) {
            ans.push([...arr]);
            return;
        }
        if (i === nums.length || sum > target) {
            return;
        }
        helper(i+1, arr, sum);
        for (let c = 1; c <= counter.get(nums[i]); c++) {
            arr.push(nums[i]);
            helper(i+1, arr, sum + nums[i] * c);
        }
        for (let c = 1; c <= counter.get(nums[i]); c++) {
            arr.pop();
        }
    }

    helper(0, [], 0);

    return ans;
};
