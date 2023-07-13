function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const graph: Set<number>[] = [];
    for (let i = 0; i < numCourses; i++) {
        graph.push(new Set());
    }

    for (const p of prerequisites) {
        graph[p[0]].add(p[1]);
    }

    const q: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (graph[i].size === 0) {
            q.push(i);
        }
    }

    while (q.length > 0) {
        const cur = q.shift();
        for (let i = 0; i < numCourses; i++) {
            if (!graph[i].has(cur)) {
                continue;
            }
            graph[i].delete(cur);
            if (graph[i].size === 0) {
                q.push(i);
            }
        }
    }

    return graph.reduce((a, b) => a && (b.size === 0), true);
};
