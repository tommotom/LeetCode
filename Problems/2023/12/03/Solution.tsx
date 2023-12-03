function minTimeToVisitAllPoints(points: number[][]): number {
    let ans = 0;
    for (let i = 1; i < points.length; i++) {
        const X = Math.abs(points[i-1][0] - points[i][0]);
        const Y = Math.abs(points[i-1][1] - points[i][1]);
        ans += Math.min(X, Y) + Math.abs(X - Y);
    }
    return ans;
};
