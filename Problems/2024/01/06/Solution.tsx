function jobScheduling(startTime: number[], endTime: number[], profit: number[]): number {
    const jobs = [];
    for (let i = 0; i < startTime.length; i++) {
        jobs.push([startTime[i], endTime[i], profit[i]]);
    }
    jobs.sort((a, b) => a[1] - b[1]);

    const dp = [[0, 0]];
    for (const [s, e, p] of jobs) {
        let l = 0, r = dp.length;
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (dp[m][0] <= s) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        l--;

        if (dp[l][0] <= s && dp[dp.length-1][1] < dp[l][1] + p) {
            dp.push([e, dp[l][1] + p]);
        }
    }
    return dp[dp.length-1][1];
};
