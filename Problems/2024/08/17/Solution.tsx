function maxPoints(points: number[][]): number {
    const m = points.length, n = points[0].length;
    let prev = points[0];
    for (let i = 1; i < m; i++) {
        const left = Array(n).fill(0);
        left[0] = prev[0];
        for (let j = 1; j < n; j++) {
            left[j] = Math.max(left[j-1] - 1, prev[j]);
        }

        const right = Array(n).fill(0);
        right[n-1] = prev[n-1];
        for (let j = n-2; j >= 0; j--) {
            right[j] = Math.max(right[j+1] - 1, prev[j]);
        }

        const cur = [];
        for (let j = 0; j < n; j++) {
            cur.push(Math.max(left[j], right[j]) + points[i][j]);
        }

        prev = cur;
    }

    return prev.reduce((a, b) => Math.max(a, b));
};
