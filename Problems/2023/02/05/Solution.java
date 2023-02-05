class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        if (s.length() < p.length()) {
            return ans;
        }

        int[] pCount = new int[26];
        for (char c : p.toCharArray()) {
            pCount[c - 'a']++;
        }

        int[] sCount = new int[26];
        for (int i = 0; i < p.length()-1; i++) {
            sCount[s.charAt(i) - 'a']++;
        }

        for (int i = p.length()-1; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
            for (int j = 0; j < 26; j++) {
                if (pCount[j] != sCount[j]) {
                    break;
                }
                if (j == 25) {
                    ans.add(i-p.length()+1);
                }
            }
            sCount[s.charAt(i-p.length()+1) - 'a']--;
        }

        return ans;
    }
}
