class Solution {
    public int[] findBall(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int c = i;
            boolean valid = true;
            for (int j = 0; j < m; j++) {
                if (grid[j][c] == 1) {
                    if (c+1 == n || grid[j][c+1] == -1) {
                        valid = false;
                        break;
                    }
                    c++;
                } else {
                    if (c == 0 || grid[j][c-1] == 1) {
                        valid = false;
                        break;
                    }
                    c--;
                }
            }
            ans[i] = valid ? c : -1;
        }
        return ans;
    }
}
