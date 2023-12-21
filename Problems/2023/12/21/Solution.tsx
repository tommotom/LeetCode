function maxWidthOfVerticalArea(points: number[][]): number {
    const xs = [...new Set(points.map(a => a[0]))].sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < xs.length-1; i++) {
        ans = Math.max(ans, xs[i+1] - xs[i]);
    }
    return ans;
};
