class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        int[] count1 = new int[26];
        for (char c : s1.toCharArray()) {
            count1[c - 'a']++;
        }

        int l1 = s1.length(), l2 = s2.length();
        int[] count2 = new int[26];
        for (int i = 0; i < l1-1; i++) {
            count2[s2.charAt(i) - 'a']++;
        }
        for (int i = l1-1; i < l2; i++) {
            count2[s2.charAt(i) - 'a']++;
            for (int j = 0; j < 26; j++) {
                if (count1[j] != count2[j]) {
                    break;
                }
                if (j == 25) {
                    return true;
                }
            }
            count2[s2.charAt(i-l1+1) - 'a']--;
        }

        return false;
    }
}
