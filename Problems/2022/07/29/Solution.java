class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new LinkedList<>();
        for (String word : words) {
            if (isMatch(word, pattern)) {
                ans.add(word);
            }
        }
        return ans;
    }

    private boolean isMatch(String word, String pattern) {
        HashMap<Character, Character> map1 = new HashMap<>();
        HashMap<Character, Character> map2 = new HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            if (!map1.containsKey(word.charAt(i))) {
                map1.put(word.charAt(i), pattern.charAt(i));
            }
            if (!map2.containsKey(pattern.charAt(i))) {
                map2.put(pattern.charAt(i), word.charAt(i));
            }
            if (map1.get(word.charAt(i)) != pattern.charAt(i)) {
                return false;
            }
            if (map2.get(pattern.charAt(i)) != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
