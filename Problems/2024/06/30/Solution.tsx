class UF {
    ids;
    constructor(n) {
        this.ids = Array(n).fill(0).map((_, i) => i);
    }

    find(u) {
        if (this.ids[u] !== u) {
            this.ids[u] = this.find(this.ids[u]);
        }
        return this.ids[u];
    }

    union(u, v) {
        u = this.find(u);
        v = this.find(v);
        this.ids[u] = v;
    }
}

function maxNumEdgesToRemove(n: number, edges: number[][]): number {
    const a = new UF(n);
    const b = new UF(n);

    edges = edges.map(e => [e[0], e[1]-1, e[2]-1]);
    edges.sort((a, b) => b[0] - a[0]);

    let ans = 0;

    for (const [t, u, v] of edges) {
        if (t === 1) {
            if (a.find(u) !== a.find(v)) {
                a.union(u, v);
            } else {
                ans++;
            }
        } else if (t === 2) {
            if (b.find(u) !== b.find(v)) {
                b.union(u, v);
            } else {
                ans++;
            }
        } else {
            if (a.find(u) !== a.find(v) || b.find(u) !== b.find(v)) {
                a.union(u, v);
                b.union(u, v);
            } else {
                ans++;
            }
        }
    }


    if (new Set(a.ids.map(i => a.find(i))).size > 1) {
        return -1;
    }
    if (new Set(b.ids.map(i => b.find(i))).size > 1) {
        return -1
    }
    return ans;
};
