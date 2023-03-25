class UF {

    final int[] ids;

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
        ids[find(u)] = find(v);
    }

}

class Solution {
    public long countPairs(int n, int[][] edges) {
        UF uf = new UF(n);
        for (int[] e : edges) {
            uf.union(e[0], e[1]);
        }

        Map<Integer, Integer> counter = new HashMap<>();
        for (int id : uf.ids) {
            id = uf.find(id);
            counter.put(id, counter.getOrDefault(id, 0) + 1);
        }

        long ans = 0;
        int rest = n;
        for (int id : counter.keySet()) {
            rest -= counter.get(id);
            ans += rest * counter.get(id);
        }
        return ans;
    }
}
