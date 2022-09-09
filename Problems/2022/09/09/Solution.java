class Solution {
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a, b) -> b[0] - a[0]);
        int level = properties[0][0];
        int max = Integer.MIN_VALUE;
        int tmp = properties[0][1];
        int ans = 0;
        for (int[] property : properties) {
            if (level > property[0]) {
                max = Math.max(max, tmp);
                tmp = property[1];
            }
            level = property[0];
            if (property[1] < max) {
                ans++;
            }
            tmp = Math.max(tmp, property[1]);
        }
        return ans;
    }
}
