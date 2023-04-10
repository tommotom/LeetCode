class Solution {
    public int largestPathValue(String colors, int[][] edges) {
        int[] deg = new int[colors.length()];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] e : edges) {
            graph.putIfAbsent(e[1], new ArrayList<>());
            graph.get(e[1]).add(e[0]);
            deg[e[0]]++;
        }

        LinkedList<Integer> q = new LinkedList<>();
        int[][] count = new int[colors.length()][26];
        for (int i = 0; i < deg.length; i++){
            if (deg[i] == 0) {
                q.add(i);
            }
        }

        int ans = 0;
        while (q.size() > 0) {
            int cur = q.poll();
            count[cur][colors.charAt(cur)-'a']++;
            ans = Math.max(ans, Arrays.stream(count[cur]).max().getAsInt());
            if (!graph.containsKey(cur)) {
                continue;
            }
            for (int next : graph.get(cur)) {
                for (int i = 0; i < 26; i++) {
                    count[next][i] = Math.max(count[next][i], count[cur][i]);
                }
                deg[next]--;
                if (deg[next] == 0) {
                    q.add(next);
                }
            }
        }

        for (int d : deg) {
            if (d > 0) {
                return -1;
            }
        }

        return ans;
    }
}
