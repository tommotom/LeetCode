function insert(intervals: number[][], newInterval: number[]): number[][] {
    const ans = [];

    function mergeIfOverlap(interval: number[]) {
        if (ans.length > 0 && interval[0] <= ans[ans.length-1][1]) {
            ans[ans.length-1][1] = Math.max(ans[ans.length-1][1], interval[1]);
        } else {
            ans.push(interval);
        }
    }

    let inserted = false;
    for (const [s, e] of intervals) {
        if (newInterval[0] <= s) {
            mergeIfOverlap(newInterval);
            inserted = true;
        }
        mergeIfOverlap([s, e]);
    }

    if (!inserted) {
        mergeIfOverlap(newInterval);
    }

    return ans;
};
