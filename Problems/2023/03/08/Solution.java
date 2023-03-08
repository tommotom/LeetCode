class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1, r = Arrays.stream(piles).max().getAsInt();
        while (l < r) {
            int m = l + (r - l) / 2;
            int hour = 0;
            for (int p : piles) {
                hour += (p+m-1)/m;
            }
            if (h < hour) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
