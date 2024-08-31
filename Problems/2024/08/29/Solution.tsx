function removeStones(stones: number[][]): number {
    const n = stones.length;
    const graph = Array(n).fill(0).map(_ => []);
    for (let i = 0; i < n-1; i++) {
        for (let j = i+1; j < n; j++) {
            if (stones[i][0] === stones[j][0] || stones[i][1] === stones[j][1]) {
                graph[i].push(j);
                graph[j].push(i);
            }
        }
    }

    const visited = Array(n).fill(false);

    const dfs = u => {
        visited[u] = true;
        for (const v of graph[u]) {
            if (!visited[v]) {
                dfs(v);
            }
        }
    }

    let groups = 0;

    for (let u = 0; u < n; u++) {
        if (!visited[u]) {
            dfs(u);
            groups++;
        }
    }

    return n - groups;
};
