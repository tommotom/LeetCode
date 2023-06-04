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
        u = find(u);
        v = find(v);
        ids[u] = v;
    }
}

class Solution {
    public int findCircleNum(int[][] isConnected) {
        final int n = isConnected.length;
        final UF uf = new UF(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (isConnected[i][j] == 1) {
                    uf.union(i, j);
                }
            }
        }

        Set<Integer> ans = new HashSet<>();
        for (int id : uf.ids) {
            ans.add(uf.find(id));
        }
        return ans.size();
    }
}
