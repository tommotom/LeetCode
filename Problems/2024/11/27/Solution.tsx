function shortestDistanceAfterQueries(n: number, queries: number[][]): number[] {
    const graph = new Map();
    const steps = Array(n).fill(0);
    for (let i = 0; i < n-1; i++) {
        graph.set(i, [i+1]);
        steps[i+1] = i+1;
    }

    const dfs = (cur, step) => {
        if (steps[cur] <= step) {
            return;
        }
        steps[cur] = step;
        for (const next of graph.get(cur) || []) {
            dfs(next, step+1);
        }
    }

    const ans = [];
    for (const [u, v] of queries) {
        dfs(v, steps[u] + 1);
        graph.get(u).push(v);
        ans.push(steps[n-1]);
    }

    return ans;
};
