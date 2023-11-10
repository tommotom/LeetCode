function restoreArray(adjacentPairs: number[][]): number[] {
    const graph = new Map();
    for (const [u, v] of adjacentPairs) {
        if (!graph.has(u)) {
            graph.set(u, []);
        }
        if (!graph.has(v)) {
            graph.set(v, []);
        }
        graph.get(u).push(v);
        graph.get(v).push(u);
    }

    let cur;
    for (const u of graph.keys()) {
        if (graph.get(u).length === 1) {
            cur = u;
            break;
        }
    }

    const ans = [];
    const visited = new Set();
    while (ans.length <= adjacentPairs.length) {
        ans.push(cur);
        visited.add(cur);
        for (const next of graph.get(cur)) {
            if (visited.has(next)) {
                continue;
            } else {
                cur = next;
            }
        }
    }

    return ans;
};
