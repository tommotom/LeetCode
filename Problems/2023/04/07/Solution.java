class Solution {

    private static final int[][] dirs = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
    private int m;
    private int n;
    private int[][] grid;

    public int numEnclaves(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 1) {
                dfs(i, 0);
            }
            if (grid[i][n-1] == 1) {
                dfs(i, n-1);
            }
        }
        for (int j = 1; j < n-1; j++) {
            if (grid[0][j] == 1) {
                dfs(0, j);
            }
            if (grid[m-1][j] == 1) {
                dfs(m-1, j);
            }
        }

        int ans = 0;
        for (int i = 1; i < m-1; i++) {
            for (int j = 1; j < n-1; j++) {
                if (grid[i][j] == 1) {
                    ans++;
                }
            }
        }

        return ans;
    }

    private void dfs(int i, int j) {
        if (i < 0 || i == m || j < 0 || j == n || grid[i][j] != 1) {
            return;
        }
        grid[i][j] = 0;
        for (int[] d : dirs) {
            dfs(i+d[0], j+d[1]);
        }
    }
}
