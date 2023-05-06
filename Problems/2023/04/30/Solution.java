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
        ids[find(u)] = ids[find(v)];
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        Arrays.sort(edges, (a, b) -> b[0] - a[0]);

        UF a = new UF(n);
        UF b = new UF(n);

        int ans = 0;
        for (int[] e : edges) {
            if (e[0] == 1) {
                if (a.find(e[1]-1) != a.find(e[2]-1)) {
                    a.union(e[1]-1, e[2]-1);
                } else {
                    ans++;
                }
            } else if (e[0] == 2) {
                if (b.find(e[1]-1) != b.find(e[2]-1)) {
                    b.union(e[1]-1, e[2]-1);
                } else {
                    ans++;
                }
            } else {
                if (a.find(e[1]-1) != a.find(e[2]-1)
                        || b.find(e[1]-1) != b.find(e[2]-1)) {
                    a.union(e[1]-1, e[2]-1);
                    b.union(e[1]-1, e[2]-1);
                } else {
                    ans++;
                }
            }
        }

        Set<Integer> alice = new HashSet<>();
        for (int id : a.ids) {
            alice.add(a.find(id));
        }
        Set<Integer> bob = new HashSet<>();
        for (int id : b.ids) {
            bob.add(b.find(id));
        }

        return alice.size() > 1 || bob.size() > 1 ? -1 : ans;
    }
}
