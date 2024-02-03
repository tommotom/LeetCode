function maxSumAfterPartitioning(arr: number[], k: number): number {
    const dp = [0];
    for (let i = 0; i < arr.length; i++) {
        dp.push(dp[dp.length-1] + arr[i]);
        let num = arr[i];
        for (let j = 1; j < k; j++) {
            if (i - j < 0) {
                break;
            }
            num = Math.max(num, arr[i-j]);
            dp[i+1] = Math.max(dp[i+1], dp[i-j] + num * (j+1));
        }
    }
    return dp[dp.length-1];
};
