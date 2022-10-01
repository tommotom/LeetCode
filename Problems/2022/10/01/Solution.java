class Solution {

    Map<Integer, Integer> memo = new HashMap<>();

    public int numDecodings(String s) {
        return helper(s, 0);
    }

    private int helper(String s, int i) {
        if (memo.containsKey(i)) {
            return memo.get(i);
        }
        if (s.length() < i) {
            return 0;
        }
        if (s.length() == i) {
            return 1;
        }
        if (s.charAt(i) == '0') {
            return 0;
        }
        int ret = helper(s, i+1);
        if (i+1 < s.length() && s.charAt(i) == '1') {
            ret += helper(s, i+2);
        } else if (i+1 < s.length() && s.charAt(i) == '2' && s.charAt(i+1) >= '0' && s.charAt(i+1) <= '6') {
            ret += helper(s, i+2);
        }
        memo.put(i, ret);
        return ret;
    }
}
