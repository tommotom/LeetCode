class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            int[] a = new int[n];
            for (int j = i; j < m; j++) {
                for (int l = 0; l < n; l++) {
                    a[l] += matrix[j][l];
                }
                ans = Math.max(ans, helper(a, k));
            }
        }
        return ans;
    }

    private int helper(int[] a, int k) {
        int sum = Integer.MIN_VALUE;
        for (int i = 0; i < a.length; i++) {
            int s = 0;
            for (int j = i; j < a.length; j++) {
                s += a[j];
                if (s <= k) {
                    sum = Math.max(sum, s);
                }
            }
        }
        return sum;
    }
}
