class Solution {

    private final List<List<Integer>> ans = new ArrayList<>();
    private int[][] graph;
    private int n;

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        this.graph = graph;
        this.n = graph.length - 1;
        dfs(new Stack<>(), 0);
        return ans;
    }

    private void dfs(Stack<Integer> path, int cur) {
        path.push(cur);
        if (cur == n) {
            ans.add(new ArrayList<>(path));
        } else {
            for (int next : graph[cur]) {
                dfs(path, next);
            }
        }
        path.pop();
    }
}
