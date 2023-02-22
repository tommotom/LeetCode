class Solution {

    private int[] weights;
    private int days;

    public int shipWithinDays(int[] weights, int days) {
        this.weights = weights;
        this.days = days;
        int l = 1, r = Integer.MAX_VALUE;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (isOK(m)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }

    private boolean isOK(int cap) {
        int cur = 0;
        int d = 1;
        for (int weight : weights) {
            if (weight > cap) {
                return false;
            }
            if (cur + weight > cap) {
                cur = weight;
                d++;
            } else {
                cur += weight;
            }
        }
        return d <= days;
    }
}
