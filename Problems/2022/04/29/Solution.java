class Solution {
  public boolean isBipartite(int[][] graph) {
    int n = graph.length;
    int[] color = new int[n];
    for (int u = 0; u < n; u++) {
      if (color[u] == 0) {
        color[u] = 1;
        if (!dfs(u, color, graph)) {
          return false;
        }
      }
    }
    return true;
  }

  private boolean dfs(int u, int[] color, int[][] graph) {
    for (int i = 0; i < graph[u].length; i++) {
      int v = graph[u][i];
      if (color[u] == color[v]) {
        return false;
      }
      if (color[u] + color[v] == 3) {
        continue;
      }
      color[v] = color[u] == 1 ? 2 : 1;
      if (!dfs(v, color, graph)) {
        return false;
      }
    }
    return true;
  }
}
