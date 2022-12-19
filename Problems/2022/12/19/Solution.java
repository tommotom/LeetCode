class Solution {

    private final int[] ids;

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        ids = new int[n];
        for (int i = 0; i < n; i++) {
            ids[i] = i;
        }

        for (int[] edge : edges) {
            union(edge[0], edge[1]);
        }

        return find(source) == find(destination);
    }

    private int find(int u) {
        if (u != ids[u]) {
            ids[u] = find(ids[u]);
        }
        return ids[u];
    }

    private void union(int u, int v) {
        ids[find(u)] = find(v);
    }

}
