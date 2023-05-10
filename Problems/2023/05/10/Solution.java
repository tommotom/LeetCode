class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];
        int num = 1, r = 0, c = 0, i = 0;
        int[][] dirs = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        for (int j = 0; j < n * n; j++) {
            ans[r][c] = num++;
            if (r + dirs[i][0] < 0 || r + dirs[i][0] == n || c + dirs[i][1] < 0 || c + dirs[i][1] == n || ans[r + dirs[i][0]][c + dirs[i][1]] > 0) {
                i = (i+1) % 4;
            }
            r += dirs[i][0];
            c += dirs[i][1];
        }
        return ans;
    }
}
