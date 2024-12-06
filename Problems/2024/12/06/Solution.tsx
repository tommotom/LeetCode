function maxCount(banned: number[], n: number, maxSum: number): number {
    const arr = Array.from(new Set(banned)).sort((a, b) => a - b);
    let i = 0 , sum = 0, ans = 0;
    for (let num = 1; num <= n; num++) {
        if (i < arr.length && arr[i] === num) {
            i++;
            continue;
        }
        if (sum + num <= maxSum) {
            sum += num;
            ans++;
        }
    }
    return ans;
};
