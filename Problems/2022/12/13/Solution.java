class Solution {
    public int minFallingPathSum(int[][] matrix) {
        for (int r = 1; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) {
                int val = matrix[r-1][c];
                if (c > 0) {
                    val = Math.min(val, matrix[r-1][c-1]);
                }
                if (c+1 < matrix[0].length) {
                    val = Math.min(val, matrix[r-1][c+1]);
                }
                matrix[r][c] += val;
            }
        }
        return Arrays.stream(matrix[matrix.length-1]).min().getAsInt();
    }
}
