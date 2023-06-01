class Solution {

    private int n;
    private int m;

    public int shortestPathBinaryMatrix(int[][] grid) {
        this.n = grid.length;
        this.m = grid[0].length;
        int[][] dirs = new int[][]{{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1}};
        Integer[][] memo = new Integer[n][m];

        LinkedList<int[]> q = new LinkedList<>();
        if (grid[0][0] == 0) {
            q.add(new int[]{0, 0, 1});
        }
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            if (memo[cur[0]][cur[1]] != null) {
                continue;
            }
            if (cur[0] == n-1 && cur[1] == m-1) {
                return cur[2];
            }
            memo[cur[0]][cur[1]] = cur[2];
            for (int[] dir : dirs) {
                int nextR = cur[0] + dir[0];
                int nextC = cur[1] + dir[1];
                if (!isValid(nextR, nextC)) {
                    continue;
                }
                if (grid[nextR][nextC] == 1) {
                    continue;
                }
                q.add(new int[]{nextR, nextC, cur[2] + 1});
            }
        }
        return -1;
    }


    private boolean isValid(int r, int c) {
        return 0 <= r && r < n && 0 <= c && c < m;
    }
}
