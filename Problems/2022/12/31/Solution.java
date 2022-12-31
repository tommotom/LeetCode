class Solution {

    private final int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    private int[][] grid;
    private int ans;
    private int count;

    public int uniquePathsIII(int[][] grid) {
        this.grid = grid;

        int startI = 0, startJ = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    startI = i;
                    startJ = j;
                } else if (grid[i][j] == 0) {
                    count++;
                }
            }
        }
        helper(startI, startJ);
        return ans;
    }

    private void helper(int i, int j) {
        if (grid[i][j] == 2) {
            if (count == 0) {
                ans++;
            }
            return;
        }

        int org = grid[i][j];
        if (org == 0) {
            count--;
        }
        grid[i][j] = 3;
        for (int[] dir : dirs) {
            int nextI = i + dir[0];
            int nextJ = j + dir[1];
            if (nextI < 0 || nextI >= grid.length) {
                continue;
            }
            if (nextJ < 0 || nextJ >= grid[0].length) {
                continue;
            }
            if (grid[nextI][nextJ] == 0 || grid[nextI][nextJ] == 2) {
                helper(nextI, nextJ);
            }
        }
        if (org == 0) {
            count++;
        }
        grid[i][j] = org;
    }
}
