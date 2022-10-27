class Solution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int n = img1.length;
        int ans = 0;
        for (int r = -n+1; r < n; r++) {
            for (int c = -n+1; c < n; c++) {
                int over = 0;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (r+i < 0 || r+i >= n || c+j < 0 || c+j >= n) {
                            continue;
                        }
                        if (img1[r+i][c+j] == 1 && img2[i][j] == 1) {
                            over++;
                        }
                    }
                }
                ans = Math.max(ans, over);
            }
        }
        return ans;
    }
}
