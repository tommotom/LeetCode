class Solution {
    public int minDeletionSize(String[] strs) {
        int ans = 0, len = strs[0].length();
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < strs.length-1; j++) {
                if (strs[j].charAt(i) > strs[j+1].charAt(i)) {
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
}
