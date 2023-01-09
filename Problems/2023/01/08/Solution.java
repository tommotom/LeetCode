class Line {

    private final int x1;
    private final int y1;
    private final int x2;
    private final int y2;

    Line(int[] p1, int[] p2) {
        x1 = p1[0];
        y1 = p1[1];
        x2 = p2[0];
        y2 = p2[1];
    }

    boolean isOnTheLine(int[] p) {
        int left = (x1 - x2) * p[1];
        int right = (y1 - y2) * p[0] + x1*y2 - x2*y1;
        return left == right;
    }
}

class Solution {
    public int maxPoints(int[][] points) {
        int ans = 0, n = points.length;
        if (n == 1) {
            return 1;
        }
        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                Line line = new Line(points[i], points[j]);
                int tmp = 0;
                for (int k = 0; k < n; k++) {
                    if (line.isOnTheLine(points[k])) {
                        tmp++;
                    }
                }
                ans = Math.max(ans, tmp);
            }
        }
        return ans;
    }
}
