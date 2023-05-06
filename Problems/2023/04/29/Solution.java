class UF {

    private int[] ids;

    UF(int size) {
        ids = new int[size];
        for (int i = 0; i < size; i++) {
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
        ids[find(u)] = ids[find(v)];
    }
}

class Solution {
    public boolean[] distanceLimitedPathsExist(int n, int[][] edgeList, int[][] queries) {
        int m = queries.length;
        Map<int[], Integer> indice = new HashMap<>();
        for (int i = 0; i < m; i++) {
            indice.put(queries[i], i);
        }

        Arrays.sort(edgeList, (a, b) -> a[2] - b[2]);
        Arrays.sort(queries, (a, b) -> a[2] - b[2]);

        int j = 0;
        UF uf = new UF(n);
        boolean[] isExist = new boolean[m];
        for (int i = 0; i < m; i++) {
            while (j < edgeList.length && edgeList[j][2] < queries[i][2]) {
                uf.union(edgeList[j][0], edgeList[j][1]);
                j++;
            }
            if (uf.find(queries[i][0]) == uf.find(queries[i][1])){
                isExist[indice.get(queries[i])] = true;
            }
        }

        return isExist;
    }
}
