class Solution {

    private Map<Integer, List<Integer>> graph = new HashMap<>();
    private Map<Integer, Map<Integer, Integer>> degree = new HashMap<>();
    private int n;

    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        this.n = n;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            graph.putIfAbsent(u, new ArrayList<>());
            graph.putIfAbsent(v, new ArrayList<>());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        LinkedList<Pair<Integer, Integer>> q = new LinkedList<>();
        q.add(new Pair(0, dist(0, new HashSet<>(), 0)));
        int[] ans = new int[n];
        Set<Integer> visited = new HashSet<>();
        while (!q.isEmpty()) {
            Pair<Integer, Integer> pair = q.poll();
            int u = pair.getKey(), dist = pair.getValue();
            visited.add(u);
            ans[u] = dist;

            for (int v : graph.getOrDefault(u, new ArrayList<>())) {
                if (!visited.contains(v)) {
                    int to = degree(u, v);
                    q.add(new Pair(v, dist - to + (n - to)));
                }
            }
        }

        return ans;
    }

    private int degree(int from, int to) {
        if (graph.get(from).size() == 1) {
            return n-1;
        }
        if (graph.get(to).size() == 1) {
            return 1;
        }
        if (degree.containsKey(from) && degree.get(from).containsKey(to)) {
            return degree.get(from).get(to);
        }
        int ret = 1;
        for (int next : graph.get(to)) {
            if (next == from) {continue;}
            ret += degree(to, next);
        }
        degree.putIfAbsent(from, new HashMap<>());
        degree.get(from).put(to, ret);
        return ret;
    }

    private int dist(int cur, Set<Integer> visited, int len) {
        int ret = 0;
        visited.add(cur);
        for (int next : graph.getOrDefault(cur, new ArrayList<>())) {
            if (!visited.contains(next)) {
                ret += dist(next, visited, len+1);
            }
        }
        return ret + len;
    }
}
