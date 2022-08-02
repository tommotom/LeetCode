class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int l = -1000000000, r = 1000000000;
        while (l < r) {
            int m = l + (r - l) / 2;
            int c = count(matrix, m);
            if (c < k) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }

    private int count(int[][] matrix, int num) {
        int ret = 0;
        for (int i = 0; i < matrix.length; i++) {
            int l = 0, r = matrix[0].length;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (matrix[i][m] <= num) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            ret += l;
        }
        return ret;
    }
}
