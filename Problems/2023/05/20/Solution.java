class Solution {

    private final Map<String, Map<String, Double>> graph = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);
            if (!graph.containsKey(a)) {graph.put(a, new HashMap<>());}
            if (!graph.containsKey(b)) {graph.put(b, new HashMap<>());}
            graph.get(a).put(b, values[i]);
            graph.get(b).put(a, 1/values[i]);
        }

        int n = queries.size();
        double[] ans = new double[n];
        for (int i = 0; i < n; i++) {
            ans[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 1, new HashSet<>());
        }

        return ans;
    }

    private double dfs(String a, String b, double val, Set<String> visited) {
        if (!graph.containsKey(a)) {
            return -1;
        }
        if (a.equals(b)) {
            return val;
        }
        visited.add(a);
        Map<String, Double> map = graph.get(a);
        for (String key : map.keySet()) {
            if (visited.contains(key)) {
                continue;
            }
            double ret = dfs(key, b, val * map.get(key), visited);
            if (ret != -1) {
                return ret;
            }
        }
        return -1;
    }
}
