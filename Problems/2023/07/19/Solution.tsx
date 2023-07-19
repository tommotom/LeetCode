function eraseOverlapIntervals(intervals: number[][]): number {
    intervals.sort((a, b) => a[1] - b[1]);
    let ans = 0;
    let i = 0;
    while (i < intervals.length - 1) {
        let j = i + 1;
        while (j < intervals.length) {
            if (intervals[i][1] > intervals[j][0]) {
                ans++;
                j++;
            } else {
                break;
            }
        }
        i = j;
    }
    return ans;
};
