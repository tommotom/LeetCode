class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int n = people.length;
        Arrays.sort(people);
        boolean[] done = new boolean[n];
        int ans = 0;
        for (int i = n-1; i >= 0; i--) {
            if (done[i]) {
                continue;
            }
            done[i] = true;
            int cap = limit - people[i];
            int l = 0, r = i;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (people[m] <= cap) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            l--;
            while (l >= 0 && done[l]) {
                l--;
            }
            if (l >= 0 && cap >= people[l]) {
                done[l] = true;
            }
            ans++;
        }
        return ans;
    }
}
