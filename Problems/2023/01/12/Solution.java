class Solution {

    private int[][] count;
    private final Map<Integer, List<Integer>> graph = new HashMap<>();

    public int[] countSubTrees(int n, int[][] edges, String labels) {
        count = new int[n][26];
        for (int[] edge : edges) {
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        helper(0, new HashSet<>(), labels);

        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = count[i][labels.charAt(i)-'a'];
        }
        return ans;
    }

    private void helper(int cur, Set<Integer> visited, String labels) {
        if (visited.contains(cur)) {
            return;
        }
        visited.add(cur);

        for (int next : graph.get(cur)) {
            if (visited.contains(next)) {
                continue;
            }
            helper(next, visited, labels);
            for (int i = 0; i < 26; i++) {
                count[cur][i] += count[next][i];
            }
        }
        count[cur][labels.charAt(cur)-'a'] += 1;
    }
}
