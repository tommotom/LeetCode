class Solution {
    public String orderlyQueue(String s, int k) {
        if (k == 1) {
            StringBuilder sb = new StringBuilder(s);
            StringBuilder ans = new StringBuilder(sb);
            for (int i = 0; i < s.length(); i++) {
                sb.append(sb.charAt(0));
                sb.deleteCharAt(0);
                if (sb.compareTo(ans) < 0) {
                    ans = new StringBuilder(sb);
                }
            }
            return ans.toString();
        }
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
}
