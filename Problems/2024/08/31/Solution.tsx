function maxProbability(n: number, edges: number[][], succProb: number[], start_node: number, end_node: number): number {
    const graph = new Map();
    for (let i = 0; i < edges.length; i++) {
        const [u, v] = edges[i];
        if (!graph.has(u)) {
            graph.set(u, []);
        }
        if (!graph.has(v)) {
            graph.set(v, []);
        }
        graph.get(u).push([v, succProb[i]]);
        graph.get(v).push([u, succProb[i]]);
    }
    const prob = Array(n).fill(0);
    prob[start_node] = 1;

    const q = [start_node];

    while (q.length > 0) {
        const u = q.shift();
        for (const [v, P] of graph.get(u) || []) {
            if (prob[u] * P > prob[v]) {
                prob[v] = prob[u] * P;
                q.push(v);
            }
        }
    }
    return prob[end_node];
};
