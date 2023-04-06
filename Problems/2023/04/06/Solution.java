class Solution {

    private static final int[][] dir = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
    private int m;
    private int n;

    public int closedIsland(int[][] grid) {
        m = grid.length;
        n = grid[0].length;

        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                dfs(grid, i, 0);
            }
            if (grid[i][n-1] == 0) {
                dfs(grid, i, n-1);
            }
        }
        for (int j = 0; j < n; j++) {
            if (grid[0][j] == 0) {
                dfs(grid, 0, j);
            }
            if (grid[m-1][j] == 0) {
                dfs(grid, m-1, j);
            }
        }

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    dfs(grid, i, j);
                    ans++;
                }
            }
        }

        return ans;
    }

    private void dfs(int[][] grid, int row, int col) {
        if (row < 0 || row == m || col < 0 || col == n) {
            return;
        }
        if (grid[row][col] != 0) {
            return;
        }
        grid[row][col] = 2;
        for (int[] d : dir) {
            dfs(grid, row + d[0], col + d[1]);
        }
    }
}
