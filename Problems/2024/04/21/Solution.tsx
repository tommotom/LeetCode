function validPath(n: number, edges: number[][], source: number, destination: number): boolean {
    const visited = new Set();
    const graph = new Map();
    for (const [u, v] of edges) {
        if (!graph.has(u)) {
            graph.set(u, []);
        }
        if (!graph.has(v)) {
            graph.set(v, []);
        }
        graph.get(u).push(v);
        graph.get(v).push(u);
    }

    const dfs = u => {
        if (u === destination) {
            return true;
        }
        if (visited.has(u)) {
            return false;
        }
        visited.add(u);
        for (const v of graph.get(u)) {
            if (dfs(v)) {
                return true;
            }
        }
        return false;
    }

    return dfs(source);
};
