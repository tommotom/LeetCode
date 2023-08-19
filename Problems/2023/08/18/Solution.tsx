function maximalNetworkRank(n: number, roads: number[][]): number {
    const graph: Map<number, Set<number>> = new Map();
    for (const [a, b] of roads) {
        if (!graph.has(a)) {
            graph.set(a, new Set());
        }
        if (!graph.has(b)) {
            graph.set(b, new Set());
        }
        graph.get(a).add(b);
        graph.get(b).add(a);
    }

    let ans = 0;
    for (const a of graph.keys()) {
        for (const b of graph.keys()) {
            if (a === b) {
                continue;
            }
            const A = graph.get(a), B = graph.get(b);
            ans = Math.max(ans, A.size + B.size - (A.has(b) ? 1 : 0));
        }
    }

    return ans;
};
