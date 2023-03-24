class Solution {
    public int minReorder(int n, int[][] connections) {
        Map<Integer, List<Integer>> upstream = new HashMap<>();
        Map<Integer, List<Integer>> downstream = new HashMap<>();
        for (int[] c : connections) {
            downstream.putIfAbsent(c[0], new ArrayList<>());
            upstream.putIfAbsent(c[1], new ArrayList<>());
            downstream.get(c[0]).add(c[1]);
            upstream.get(c[1]).add(c[0]);
        }

        LinkedList<Integer> q = new LinkedList<>();
        q.add(0);
        boolean[] visited = new boolean[n];
        int ans = 0;
        while (q.size() > 0) {
            int cur = q.poll();
            visited[cur] = true;
            for (int next : downstream.getOrDefault(cur, new ArrayList<>())) {
                if (!visited[next]) {
                    q.add(next);
                    ans++;
                }
            }
            for (int next : upstream.getOrDefault(cur, new ArrayList<>())) {
                if (!visited[next]) {
                    q.add(next);
                }
            }
        }

        return ans;
    }
}
