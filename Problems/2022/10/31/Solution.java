class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            if (!isSameDigonal(matrix, i, 0)) {
                return false;
            }
        }

        for (int i = 1; i < matrix[0].length; i++) {
            if (!isSameDigonal(matrix, 0, i)) {
                return false;
            }
        }

        return true;
    }

    private boolean isSameDigonal(int[][] matrix, int r, int c) {
        int val = matrix[r][c];
        r++;
        c++;
        while (r < matrix.length && c < matrix[0].length) {
            if (matrix[r][c] != val) {
                return false;
            }
            r++;
            c++;
        }
        return true;
    }
}
