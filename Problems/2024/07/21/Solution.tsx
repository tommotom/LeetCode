class DefaultDict {
    map;
    f;

    constructor(func) {
        this.map = new Map();
        this.f = func;
    }

    get(key) {
        if (!this.map.has(key)) {
            this.map.set(key, this.f());
        }
        return this.map.get(key);
    }

    set(key, value) {
        this.map.set(key, value);
    }
}

function buildMatrix(k: number, rowConditions: number[][], colConditions: number[][]): number[][] {
    const buildGraph = conditions => {
        const graph = new DefaultDict(() => []);
        const degree = new DefaultDict(() => 0);
        for (const [a, b] of conditions) {
            degree.set(b, degree.get(b) + 1);
            graph.get(a).push(b);
        }

        return {graph, degree};
    }

    const topSort = ({graph, degree}) => {
        const st = [];
        for (let num = 1; num <= k; num++) {
            if (degree.get(num) === 0) {
                st.push(num);
            }
        }

        const ret = [];
        while (st.length > 0) {
            const u = st.pop();
            ret.push(u);
            for (const v of graph.get(u)) {
                degree.set(v, degree.get(v) - 1);
                if (degree.get(v) === 0) {
                    st.push(v);
                }
            }
        }
        return ret;
    }

    const ans = Array(k).fill(0).map(_ => Array(k).fill(0));

    const row = topSort(buildGraph(rowConditions));
    const col = topSort(buildGraph(colConditions));

    if (row.length < k || col.length < k) {
        return [];
    }

    const colIndexOf = new Map();
    for (let i = 0; i < k; i++) {
        colIndexOf.set(col[i], i);
    }

    for (let i = 0; i < k; i++) {
        ans[i][colIndexOf.get(row[i])] = row[i];
    }


    return ans;
};
