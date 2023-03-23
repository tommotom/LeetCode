class UF {

    int[] ids;

    UF(int n) {
        ids = new int[n];
        for (int i = 0; i < n; i++) {
            ids[i] = i;
        }
    }

    int find(int u) {
        if (u != ids[u]) {
            ids[u] = find(ids[u]);
        }
        return ids[u];
    }

    void union(int u, int v) {
        u = find(u);
        v = find(v);
        ids[u] = v;
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) {
            return -1;
        }
        UF uf = new UF(n);
        for (int[] c : connections) {
            uf.union(c[0], c[1]);
        }

        Set<Integer> set = new HashSet<>();
        for (int id : uf.ids) {
            set.add(uf.find(id));
        }

        return set.size() - 1;
    }
}
