class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] count1 = new int[26];
        for (char c : word1.toCharArray()) count1[c-'a']++;

        int[] count2 = new int[26];
        for (char c : word2.toCharArray()) count2[c-'a']++;

        for (int i = 0; i < 26; i++) {
            if (count1[i] != count2[i] && count1[i] * count2[i] == 0) return false;
        }

        Arrays.sort(count1);
        Arrays.sort(count2);
        for (int i = 0; i < 26; i++) {
            if (count1[i] != count2[i]) {
                return false;
            }
        }

        return true;
    }
}
