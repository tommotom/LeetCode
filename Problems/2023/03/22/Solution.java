class Solution {
    public int minScore(int n, int[][] roads) {
        Map<Integer, List<Pair<Integer, Integer>>> graph = new HashMap<>();
        for (int i = 0; i < roads.length; i++) {
            int u = roads[i][0], v = roads[i][1];
            graph.putIfAbsent(u, new ArrayList<>());
            graph.putIfAbsent(v, new ArrayList<>());
            graph.get(u).add(new Pair(v, i));
            graph.get(v).add(new Pair(u, i));
        }

        int ans = Integer.MAX_VALUE;
        Set<Integer> used = new HashSet<>();
        LinkedList<Integer> q = new LinkedList<>();
        q.add(1);
        while (q.size() > 0) {
            int u = q.poll();
            for (Pair<Integer, Integer> next : graph.getOrDefault(u, new ArrayList<>())) {
                int v = next.getKey(), i = next.getValue();
                if (used.contains(i)) {
                    continue;
                }
                ans = Math.min(ans, roads[i][2]);
                q.add(v);
                used.add(i);
            }
        }
        return ans;
    }
}
