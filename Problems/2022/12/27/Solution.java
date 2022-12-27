class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int ans = 0, n = capacity.length;
        int[] vacancy = new int[n];
        for (int i = 0; i < n; i++) {
            vacancy[i] = capacity[i] - rocks[i];
        }

        Arrays.sort(vacancy);

        for (int i = 0; i < n; i++) {
            if (vacancy[i] == 0) {
                ans++;
            } else if (vacancy[i] <= additionalRocks) {
                additionalRocks -= vacancy[i];
                ans++;
            } else {
                break;
            }
        }

        return ans;
    }
}
