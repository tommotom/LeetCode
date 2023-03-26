class Solution {

    int ans = -1;
    int[] edges;
    int[] visitedAt;
    int[] tripFrom;

    public int longestCycle(int[] edges) {
        this.edges = edges;
        int n = edges.length;
        visitedAt = new int[n];
        tripFrom = new int[n];
        for (int i = 0; i < n; i++) {
            if (visitedAt[i] == 0) {
                dfs(i, i+1, 1);
            }
        }
        return ans;
    }

    private void dfs(int i, int trip, int time) {
        visitedAt[i] = time;
        tripFrom[i] = trip;
        int next = edges[i];
        if (next == -1) {
            return;
        }
        if (visitedAt[next] > 0 && tripFrom[next] == trip) {
            ans = Math.max(ans, time - visitedAt[next] + 1);
            return;
        }
        if (visitedAt[next] == 0) {
            dfs(next, trip, time+1);
        }
    }
}
