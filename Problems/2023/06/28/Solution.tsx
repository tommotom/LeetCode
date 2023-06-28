function maxProbability(n: number, edges: number[][], succProb: number[], start: number, end: number): number {
    const graph: Map<number, Map<number, number>> = new Map();
    for (let i = 0; i < edges.length; i++) {
        const a = edges[i][0], b = edges[i][1];
        if (!graph.has(a)) {
            graph.set(a, new Map());
        }
        if (!graph.has(b)) {
            graph.set(b, new Map());
        }
        graph.get(a).set(b, succProb[i]);
        graph.get(b).set(a, succProb[i]);
    }

    const prob = new Array(n);
    for (let i = 0; i < n; i++) {
        prob[i] = 0;
    }

    const q = new Array([start, 1]);
    while (q.length > 0) {
        const arr = q.shift();
        const cur = arr[0], p = arr[1];
        if (prob[cur] >= p) {
            continue;
        }
        prob[cur] = p;
        if (!graph.has(cur)) {
            continue;
        }
        for (const next of graph.get(cur)) {
            q.push([next[0], next[1] * p]);
        }
    }

    return prob[end];
};
