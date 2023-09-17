function shortestPathLength(graph: number[][]): number {
    const n = graph.length, goal = (1 << n) - 1;
    const q = [];
    const visited = new Map();
    for (let i = 0; i < n; i++) {
        q.push([1 << i, i, 0]);
        visited.set(i, new Set([1 << i]));
    }
    while (q.length > 0) {
        const [mask, i, l] = q.shift();
        if (mask === goal) {
            return l;
        }
        for (const j of graph[i]) {
            const newMask = mask | (1 << j);
            if (visited.get(j).has(newMask)) {
                continue;
            }
            visited.get(j).add(newMask);
            q.push([newMask, j, l+1]);
        }
    }
    return -1;
};
