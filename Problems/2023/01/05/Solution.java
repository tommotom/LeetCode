class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        int ans = 1, end = points[0][1];
        for (int i = 0; i < points.length; i++) {
            if (end < points[i][0]) {
                ans++;
                end = points[i][1];
            }
        }

        return ans;
    }
}
