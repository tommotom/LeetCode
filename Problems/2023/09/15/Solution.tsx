function minCostConnectPoints(points: number[][]): number {
    const ids = [...Array(points.length)].map((_, i) => i);
    function find(i: number): number {
        if (i !== ids[i]) {
            ids[i] = find(ids[i]);
        }
        return ids[i];
    }
    function union(i: number, j: number): void {
        i = find(i);
        j = find(j);
        ids[i] = j;
    }

    function dist(a: number[], b: number[]): number {
        return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
    }

    const edges = [];
    for (let i = 0; i < points.length-1; i++) {
        for (let j = i+1; j < points.length; j++) {
            edges.push([dist(points[i], points[j]), i, j]);
        }
    }
    edges.sort((a, b) => a[0] - b[0]);

    let ans = 0;
    for (const [d, a, b] of edges) {
        if (find(a) === find(b)) {
            continue;
        }
        union(a, b);
        ans += d;
    }

    return ans;
};
