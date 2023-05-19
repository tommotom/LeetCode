class Solution {

    private int[][] graph;
    private int[] colors;

    public boolean isBipartite(int[][] graph) {
        this.graph = graph;
        this.colors = new int[graph.length];
        for (int i = 0; i < graph.length; i++) {
            if (colors[i] == 0 && !isBipartite(i, 1)) {
                return false;
            }
        }
        return true;
    }

    private boolean isBipartite(int node, int color) {
        colors[node] = color;
        for (int next : graph[node]) {
            if (colors[next] == color) {
                return false;
            } else if (colors[next] == 0 && !isBipartite(next, 2/color)) {
                return false;
            }
        }
        return true;
    }
}
