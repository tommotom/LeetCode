class Solution {
    public int computeArea(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - calcDup(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2);
    }

    private int area(int lx, int ly, int rx, int ry) {
        return (rx - lx) * (ry - ly);
    }

    private int calcDup(int ax1, int ay1, int ax2, int ay2, int bx1, int by1, int bx2, int by2) {
        if (ax2 <= bx1 || bx2 <= ax1 || ay2 <= by1 || by2 <= ay1) {
            return 0;
        }
        int cx1 = Math.max(ax1, bx1), cy1 = Math.max(ay1, by1);
        int cx2 = Math.min(ax2, bx2), cy2 = Math.min(ay2, by2);
        System.out.println(cx1 + " " + cy1 + " " + cx2 + " " + cy2);
        return area(cx1, cy1, cx2, cy2);
    }
}
