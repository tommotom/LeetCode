function getAncestors(n: number, edges: number[][]): number[][] {
    const ins = Array(n).fill(0);
    const graph = Array(n).fill(0).map(_ => []);
    for (const [u, v] of edges) {
        ins[v]++;
        graph[u].push(v);
    }

    const st = [];
    for (let i = 0; i < n; i++) {
        if (ins[i] === 0) {
            st.push(i);
        }
    }

    const sets = Array(n).fill(0).map(_ => new Set());

    while (st.length > 0) {
        const u = st.pop();
        for (const v of graph[u]) {
            sets[v].add(u);
            for (const num of sets[u]) {
                sets[v].add(num);
            }
            ins[v]--;
            if (ins[v] === 0) {
                st.push(v);
            }
        }
    }

    const ans = [];
    for (let i = 0; i < n; i++) {
        ans[i] = Array.from(sets[i].values());
        ans[i].sort((a, b) => a - b);
    }

    return ans;
};
