function rangeSum(nums: number[], n: number, left: number, right: number): number {
    const cum = [0];

    for (let i = 0; i < n; i++) {
        cum.push(cum[cum.length-1] + nums[i]);
    }

    const arr = [];
    for (let i = 0; i < n; i++) {
        for (let j = i+1; j < n+1; j++) {
            arr.push(cum[j] - cum[i]);
        }
    }

    arr.sort((a, b) => a - b);

    let ans = 0;
    for (let i = left-1; i < right; i++) {
        ans += arr[i];
    }

    return ans;
};
