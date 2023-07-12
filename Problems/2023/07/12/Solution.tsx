function eventualSafeNodes(graph: number[][]): number[] {
    const revGraph: number[][] = new Array();
    for (let u = 0; u < graph.length; u++) {
        revGraph.push(new Array());
    }
    for (let u = 0; u < graph.length; u++) {
        for (const v of graph[u]) {
            revGraph[v].push(u);
        }
    }

    const terminates: Set<number> = new Set();
    let q: Array<number> = new Array();
    for (let u = 0; u < graph.length; u++) {
        if (graph[u].length === 0) {
            q.push(u);
            terminates.add(u);
        }
    }

    while (q.length > 0) {
        const u = q.shift();
        while (revGraph[u].length > 0) {
            const v = revGraph[u].shift();
            graph[v] = graph[v].filter(w => w !== u);
            if (graph[v].length === 0) {
                q.push(v);
                terminates.add(v);
            }
        }
    }

    return Array.from(terminates.values()).sort((a, b) => a - b);
};
