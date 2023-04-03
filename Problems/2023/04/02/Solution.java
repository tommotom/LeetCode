class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;

        Arrays.sort(potions);
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int l = 0, r = m;
            while (l < r) {
                int j = l + (r - l) / 2;
                long product = ((long) spells[i]) * ((long) potions[j]);
                if (product < success) {
                    l = j + 1;
                } else {
                    r = j;
                }
            }
            ans[i] = m - l;
        }

        return ans;
    }
}
