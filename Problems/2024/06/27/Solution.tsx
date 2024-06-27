function findCenter(edges: number[][]): number {
    const n = edges.length + 1;
    const counter = new Map();
    for (const [u, v] of edges) {
        if (!counter.has(u)) {
            counter.set(u, 0);
        }
        counter.set(u, counter.get(u) + 1);
        if (!counter.has(v)) {
            counter.set(v, 0);
        }
        counter.set(v, counter.get(v) + 1);
    }
    for (const [k, v] of counter.entries()) {
        if (v === n-1) {
            return k;
        }
    }
};
