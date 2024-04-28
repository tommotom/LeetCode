function sumOfDistancesInTree(n: number, edges: number[][]): number[] {
    const graph = new Map();
    for (const [u, v] of edges) {
        if (!graph.has(u)) {
            graph.set(u, []);
        }
        if (!graph.has(v)) {
            graph.set(v, []);
        }
        graph.get(u).push(v);
        graph.get(v).push(u);
    }

    const ans = Array(n).fill(0);
    const count = Array(n).fill(1);

    const postOrder = (node, parent = null) => {
        for (const child of graph.has(node) ? graph.get(node) : []) {
            if (child === parent) {
                continue;
            }
            postOrder(child, node);
            count[node] += count[child];
            ans[node] += ans[child] + count[child];
        }
    }

    const preOrder = (node, parent = null) => {
        for (const child of graph.has(node) ? graph.get(node) : []) {
            if (child === parent) {
                continue;
            }
            ans[child] = ans[node] - count[child] + (n - count[child]);
            preOrder(child, node);
        }
    }

    postOrder(0);
    preOrder(0);

    return ans;
};
