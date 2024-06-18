function maxProfitAssignment(difficulty: number[], profit: number[], worker: number[]): number {
    const jobs = [], n = difficulty.length;
    for (let i = 0; i < n; i++) {
        jobs.push([difficulty[i], profit[i]]);
    }
    jobs.sort((a, b) => a[0] - b[0]);

    const sorted = [];
    for (const job of jobs) {
        if (sorted.length === 0 || sorted[sorted.length-1][1] < job[1]) {
            sorted.push(job);
        }
    }

    let ans = 0;
    for (const w of worker) {
        let l = 0, r = sorted.length;
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (sorted[m][0] <= w) {
                l = m + 1;
            } else {
                r = m
            }
        }
        if (l > 0) {
            ans += sorted[l-1][1];
        }
    }

    return ans;
};
