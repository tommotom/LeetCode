class Solution {
    public String makeGood(String s) {
        for (int i = 0; i < s.length()-1; i++) {
            if (Character.toLowerCase(s.charAt(i)) == Character.toLowerCase(s.charAt(i+1)) && s.charAt(i) != s.charAt(i+1)) {
                return makeGood(s.substring(0, i) + s.substring(i+2, s.length()));
            }
        }
        return s;
    }
}
