class Solution {

    private int[] ids;
    private Map<Integer, List<Integer>> graph = new HashMap<>();

    public boolean possibleBipartition(int n, int[][] dislikes) {
        ids = new int[n];

        for (int[] dislike : dislikes) {
            int u = dislike[0] - 1, v = dislike[1] - 1;
            if (!graph.containsKey(u)) {
                graph.put(u, new ArrayList<>());
            }
            if (!graph.containsKey(v)) {
                graph.put(v, new ArrayList<>());
            }
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for (int i = 0; i < n; i++) {
            if (ids[i] == 0 && !dfs(i, 1)) {
                return false;
            }
        }

        return true;
    }

    private boolean dfs(int i, int group) {
        ids[i] = group;
        if (!graph.containsKey(i)) {
            return true;
        }
        for (int j : graph.get(i)) {
            if (ids[j] != 0) {
                if (ids[j] * group == 1) {
                    return false;
                }
            } else if (!dfs(j, group * -1)) {
                return false;
            }
        }
        return true;
    }
}
