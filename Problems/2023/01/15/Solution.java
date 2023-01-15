class UF {

    private final int[] id;
    private final int[] rank;

    UF(int n) {
        id = new int[n];
        for (int i = 0; i < n; i++) {
            id[i] = i;
        }
        rank = new int[n];
    }

    int find(int u) {
        if (id[u] == u) {
            return u;
        }
        id[u] = find(id[u]);
        return id[u];
    }

    void union(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v) {
            return;
        }
        if (rank[u] < rank[v]) {
            id[u] = id[v];
        } else if (rank[u] > rank[v]) {
            id[v] = id[u];
        } else {
            id[u] = id[v];
            rank[v]++;
        }
    }
}

class Solution {
    public int numberOfGoodPaths(int[] vals, int[][] edges) {
        int n = vals.length;

        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            if (vals[v] <= vals[u]) {
                graph[u].add(v);
            }
            if (vals[u] <= vals[v]) {
                graph[v].add(u);
            }
        }

        Map<Integer, List<Integer>> valToNode = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            valToNode.putIfAbsent(vals[i], new ArrayList<>());
            valToNode.get(vals[i]).add(i);
        }

        UF uf = new UF(n);
        int ans = n;
        for (List<Integer> nodes : valToNode.values()){
            for (int u : nodes) {
                for (int v : graph[u]) {
                    uf.union(u, v);
                }
            }

            Map<Integer, Integer> rootCount = new HashMap<>();
            for (int u : nodes) {
                int root = uf.find(u);
                rootCount.put(root, rootCount.getOrDefault(root, 0) + 1);
            }

            for (int count : rootCount.values()) {
                ans += count * (count-1) / 2;
            }
        }

        return ans;
    }
}
