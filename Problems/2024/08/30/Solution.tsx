function modifiedGraphEdges(n: number, edges: number[][], source: number, destination: number, target: number): number[][] {
    const graph = new Map();
    for (const [a, b, w] of edges) {
        if (!graph.has(a)) {
            graph.set(a, []);
        }
        if (!graph.has(b)) {
            graph.set(b, []);
        }
        graph.get(a).push([b, w]);
        graph.get(b).push([a, w]);
    }

    const q = [[source, 0]];
    const dist = new Map([[source, 0]]);
    while (q.length > 0) {
        const [cur, d] = q.shift();
        for (const [next, w] of graph.get(cur) || []) {
            if (dist.has(next) && dist.get(next) <= d + 1) {
                continue;
            }
            dist.set(next, d + 1);
            q.push([next, d+1]);
        }
    }

    const shortest = dist.get(destination);
    const visited = Array(n).fill(false);
    let ans = undefined, sum = 0, count = 0, reached = false;

    const dfs = (a, d) => {
        if (visited[a] || sum + count > target) {
            return;
        }
        if (!shortest || shortest < d) {
            return;
        }
        if (a === destination) {
            if (count > 0 || sum === target) {
                reached = true;
            }
            return;
        }

        visited[a] = true;
        for (const [b, w] of graph.get(a) || []) {
            if (w === -1) {
                ans = [a, b];
                count++;
            } else {
                sum += w;
            }

            dfs(b, d+1);

            if (reached) {
                return;
            }

            if (w === -1) {
                ans = undefined;
                count--;
            } else {
                sum -= w;
            }
        }
        visited[a] = false;
    }

    dfs(source, 0);

    if (ans) {
        const [A, B] = ans;
        for (let i = 0; i < edges.length; i++) {
            const [a, b, w] = edges[i];
            if ((a === A && b === B) || (a === B && b === A)) {
                edges[i][2] = target - sum - count + 1;
            } else if (w === -1) {
                edges[i][2] = 1;
            }
        }
    }

    return ans ? edges : [];
};
