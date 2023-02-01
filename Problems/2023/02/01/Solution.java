class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() < str2.length()) {
            String tmp = str1;
            str1 = str2;
            str2 = tmp;
        }
        for (int i = str2.length(); i > 0; i--) {
            if (str1.length() % i != 0 || str2.length() % i != 0) {
                continue;
            }
            String sub = str2.substring(0, i);
            if (isDevisor(str1, sub) && isDevisor(str2, sub)) {
                return sub;
            }
        }
        return "";
    }

    private boolean isDevisor(String str, String sub) {
        int i = 0;
        while (i < str.length()) {
            for (int j = 0; j < sub.length(); j++) {
                if (str.charAt(i) != sub.charAt(j)) {
                    return false;
                }
                i++;
            }
        }
        return true;
    }
}
