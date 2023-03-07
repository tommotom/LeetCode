class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        long l = 0, r = 100000000000000L;
        while (l < r) {
            long m = l + (r - l) / 2;
            long trips = 0;
            for (int i = 0; i < time.length; i++) {
                trips += m / time[i];
            }
            if (trips < totalTrips) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
}
