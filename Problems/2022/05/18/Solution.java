class Solution {

  private Map<Integer, List<Integer>> graph = new HashMap<>();
  private int[] disc;
  private int[] low;
  private int[] parent;
  private int time = 0;
  private List<List<Integer>> ans = new ArrayList<>();

  public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
    disc = new int[n];
    low = new int[n];
    parent = new int[n];

    for (int i = 0; i < connections.size(); i++) {
      List<Integer> edge = connections.get(i);
      int u = edge.get(0), v = edge.get(1);
      if (!graph.containsKey(u)) {
        graph.put(u, new ArrayList<>());
      }
      graph.get(u).add(v);
      if (!graph.containsKey(v)) {
        graph.put(v, new ArrayList<>());
      }
      graph.get(v).add(u);
    }

    helper(0);

    return ans;
  }

  private void dfs(int u) {
    disc[u] = low[u] = ++time;
    List<Integer> adj = graph.get(u);
    for (int i = 0; i < adj.size(); i++) {
      int v = adj.get(i);
      if (disc[v] == 0) {
        parent[v] = u;
        dfs(v);
        low[u] = Math.min(low[u], low[v]);
        if (low[v] > disc[u]) {
          ans.add(List.of(u, v));
        }
      }
      else if (parent[u] != v) {
        low[u] = Math.min(low[u], disc[v]);
      }
    }
  }
}
