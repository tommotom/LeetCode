class UF {

    ids: number[];

    constructor(n: number) {
        this.ids = [...Array(n)].map((_, i) => i);
    }

    find(u: number): number {
        return u === this.ids[u] ? u : this.ids[u] = this.find(this.ids[u]);
    }

    union(u: number, v:number): void {
        u = this.find(u), v = this.find(v);
        this.ids[u] = v;
    }

    isST(): boolean {
        for (let i = 1; i < this.ids.length; i++) {
            if (this.find(0) !== this.find(i)) {
                return false;
            }
        }
        return true;
    }
}

function findCriticalAndPseudoCriticalEdges(n: number, edges: number[][]): number[][] {
    edges = edges.map(([a, b, w], i) => [a, b, w, i]);
    edges.sort((a, b) => a[2] - b[2]);
    console.log(edges);

    function findMST(base: number, exclude: number) {
        const uf = new UF(n);
        let weight = 0;
        if (base !== -1) {
            uf.union(edges[base][0], edges[base][1]);
            weight += edges[base][2];
        }
        for (let i = 0; i < edges.length; i++) {
            const [a, b, w, _] = edges[i];
            if (i === exclude || uf.find(a) === uf.find(b)) {
                continue;
            }
            uf.union(a, b);
            weight += w;
        }
        return uf.isST() ? weight : Number.MAX_SAFE_INTEGER;
    }

    const ans = [[], []];
    const mst = findMST(-1, -1);
    for (let i = 0; i < edges.length; i++) {
        if (mst < findMST(-1, i)) {
            ans[0].push(edges[i][3]);
        } else if (mst === findMST(i, -1)) {
            ans[1].push(edges[i][3]);
        }
    }
    return ans;
};
