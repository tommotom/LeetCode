function findMinHeightTrees(n: number, edges: number[][]): number[] {
    if (edges.length === 0) {
        return [0]
    }

    const graph = new Map();
    const degrees = Array(n).fill(0);
    for (const [u, v] of edges) {
        if (!graph.has(u)) {
            graph.set(u, []);
        }
        if (!graph.has(v)) {
            graph.set(v, []);
        }
        graph.get(u).push(v);
        graph.get(v).push(u);
        degrees[u]++;
        degrees[v]++;
    }

    let q = [];
    for (let i = 0; i < n; i++) {
        if (degrees[i] === 1) {
            q.push(i);
        }
    }

    let remaining = n
    while (remaining > 2) {
        remaining -= q.length;
        const next = [];
        for (const u of q) {
            for (const v of graph.get(u)) {
                const arr = graph.get(v);
                arr.splice(arr.indexOf(u), 1);
                if (arr.length === 1) {
                    next.push(v);
                }
            }
        }
        q = next;
    }

    return q;
};
