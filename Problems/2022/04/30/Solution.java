class Solution {

  private double val;

  public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
    Map<String, Map<String, Double>> graph = new HashMap<>();
    for (int i = 0; i < values.length; i++) {
      String u = equations.get(i).get(0);
      String v = equations.get(i).get(1);
      graph.putIfAbsent(u, new HashMap<>());
      graph.get(u).put(v, values[i]);
      graph.putIfAbsent(v, new HashMap<>());
      graph.get(v).put(u, (double) 1/values[i]);
    }

    double[] ans = new double[queries.size()];
    for (int i = 0; i < queries.size(); i++) {
      val = 1;
      Set<String> visited = new HashSet<>();
      if (dfs(queries.get(i).get(0), queries.get(i).get(1), graph, visited)) {
        ans[i] = val;
        continue;
      }
      ans[i] = -1;
    }
    return ans;
  }

  private boolean dfs(String start, String goal, Map<String, Map<String, Double>> graph, Set<String> visited) {
    if (!graph.containsKey(start) || !graph.containsKey(goal)) {
      return false;
    }
    if (start.equals(goal)) {
      return true;
    }
    visited.add(start);
    for (String next : graph.get(start).keySet()) {
      if (visited.contains(next)) {
        continue;
      }
      val *= graph.get(start).get(next);
      if (next.equals(goal)) {
        return true;
      }
      if (dfs(next, goal, graph, visited)) {
        return true;
      }
      val /= graph.get(start).get(next);
    }
    return false;
  }
}
