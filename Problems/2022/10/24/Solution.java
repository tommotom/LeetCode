class Solution {
    public int maxLength(List<String> arr) {
        int n = arr.size();
        int[][] count = new int[n][26];
        for (int i = 0; i < n; i++) {
            String s = arr.get(i);
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                count[i][c-'a']++;
            }
        }

        int ans = 0;
        for (int mask = 0; mask < Math.pow(2, n); mask++) {
            int[] curr = new int[26];
            boolean isUnique = true;
            for (int i = 0; i < n; i++) {
                if ((mask&(1 << i)) == 0) {
                    continue;
                }
                for (int j = 0; j < 26; j++) {
                    curr[j] += count[i][j];
                    if (curr[j] > 1) {
                        isUnique = false;
                    }
                }
                if (!isUnique) {
                    break;
                }
            }
            if (isUnique) {
                ans = Math.max(ans, Arrays.stream(curr).sum());
            }
        }

        return ans;
    }
}
