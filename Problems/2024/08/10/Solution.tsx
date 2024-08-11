function regionsBySlashes(grid: string[]): number {
    const n = grid.length;
    const toCor = i => {
        return { r: Math.floor(i / n), c: i % n };
    };

    const ids = Array(n * n * 4).fill(0).map((_, i) => i);
    const find = u => {
        while (u !== ids[u]) {
            ids[u] = ids[ids[u]];
            u = ids[u];
        }
        return u;
    }
    const union = (u, v) => {
        u = find(u);
        v = find(v);
        ids[u] = v;
    }

    for (let i = 0; i < n * n; i++) {
        const { r, c } = toCor(i);
        const j = 4 * i;
        if (r > 0) {
            union(ids[j], ids[j-n*4+2]);
        }
        if (r < n - 1) {
            union(ids[j+2], ids[j+n*4]);
        }
        if (c > 0) {
            union(ids[j+3], ids[j-3]);
        }
        if (c < n - 1) {
            union(ids[j+1], ids[j+7]);
        }
        if (grid[r][c] !== '/') {
            union(ids[j], ids[j+1]);
            union(ids[j+2], ids[j+3]);
        }
        if (grid[r][c] !== '\\') {
            union(ids[j], ids[j+3]);
            union(ids[j+1], ids[j+2]);
        }
    }

    let set = new Set();
    for (let i = 0; i < n * n * 4; i++) {
        set.add(find(ids[i]));
    }

    return set.size;
};
