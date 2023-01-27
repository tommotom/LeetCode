class Solution {

    private final Set<String> seen = new HashSet<>();

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Arrays.sort(words, (a, b) -> a.length() - b.length());
        List<String> ans = new ArrayList<>();
        for (String word : words) {
            if (helper(word, 0)) {
                ans.add(word);
            }
            seen.add(word);
        }
        return ans;
    }

    private boolean helper(String s, int i) {
        if (i == s.length()) {
            return true;
        }
        for (int j = i+1; j <= s.length(); j++) {
            if (seen.contains(s.substring(i, j)) && helper(s, j)) {
                return true;
            }
        }
        return false;
    }
}
