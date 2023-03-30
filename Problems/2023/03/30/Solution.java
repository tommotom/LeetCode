class Solution {

    private final Map<String, Boolean> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) {return true;}

        int n = s1.length();
        if (n == 1) {return false;}

        String key = s1 + s2;
        if (memo.containsKey(key)) {return memo.get(key);}

        boolean ret = false;
        for (int i = 1; i < n; i++) {
            if (isScramble(s1.substring(0,i), s2.substring(0,i))
                    && isScramble(s1.substring(i), s2.substring(i))) {
                ret = true;
            }
            if (isScramble(s1.substring(0,i), s2.substring(n-i))
                    && isScramble(s1.substring(i), s2.substring(0,n-i))) {
                ret = true;
            }
        }

        memo.put(key, ret);

        return ret;
    }
}
