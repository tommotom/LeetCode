function findMinArrowShots(points: number[][]): number {
    points.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    let ans = 1, shot = points[0][1];
    for (const [s, e] of points) {
        if (shot < s) {
            ans++;
            shot = e;
        }
        shot = Math.min(shot, e);
    }
    return ans;
};
