class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int[][] dir = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        List<Integer> ans = new ArrayList<>();
        int i = 0, m = matrix.length, n = matrix[0].length, r = 0, c = 0;
        for (int j = 0; j < m * n; j++) {
            ans.add(matrix[r][c]);
            matrix[r][c] = Integer.MAX_VALUE;
            if (r + dir[i][0] < 0 || r + dir[i][0] == m) {
                i = (i + 1) % 4;
            } else if (c + dir[i][1] < 0 || c + dir[i][1] == n) {
                i = (i + 1) % 4;
            } else if (matrix[r + dir[i][0]][c + dir[i][1]] == Integer.MAX_VALUE) {
                i = (i + 1) % 4;
            }
            r += dir[i][0];
            c += dir[i][1];
        }
        return ans;
    }
}
