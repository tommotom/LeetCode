function destCity(paths: string[][]): string {
    const graph = new Map();
    for (const path of paths) {
        graph.set(path[0], path[1]);
    }
    let cur = paths[0][1];
    while (graph.has(cur)) {
        cur = graph.get(cur);
    }
    return cur;
};
