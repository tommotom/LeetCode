class Solution {

    private final Map<Integer, List<Integer>> graph = new HashMap<>();

    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {

        for (int[] edge : edges) {
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        return helper(0, hasApple, new HashSet<>());
    }

    private int helper(int cur, List<Boolean> hasApple, Set<Integer> visited) {
        visited.add(cur);
        int ans = 0;
        for (int next : graph.get(cur)) {
            if (visited.contains(next)) {
                continue;
            }
            int tmp = helper(next, hasApple, visited);
            if (tmp > 0 || hasApple.get(next)) {
                ans += tmp + 2;
            }
        }
        return ans;
    }
}
