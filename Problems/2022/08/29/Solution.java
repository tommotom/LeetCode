class Solution {
    private int[][] dirs = {{0,1},{1,0},{-1,0},{0,-1}};

    public int numIslands(char[][] grid) {
        int ans = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    ans++;
                }
            }
        }
        return ans;
    }

    private void dfs(char[][] grid, int i, int j) {
        grid[i][j] = '2';
        for (int[] dir : dirs) {
            int nextI = i + dir[0];
            int nextJ = j + dir[1];
            if (nextI < 0 || nextI >= grid.length || nextJ < 0 || nextJ >= grid[0].length || grid[nextI][nextJ] != '1') {
                continue;
            }
            dfs(grid, nextI, nextJ);
        }
    }
}
