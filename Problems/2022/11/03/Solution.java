class Solution {
    public int longestPalindrome(String[] words) {
        int same = 0;
        int rev = 0;
        Map<String, Integer> revs = new HashMap<>();
        for (String word : words) {
            if (revs.containsKey(word) && revs.get(word) > 0) {
                rev += 1;
                revs.put(word, revs.get(word) - 1);
                if (word.charAt(0) == word.charAt(1)) {
                    same -= 1;
                }
            } else {
                String key = new StringBuffer(word).reverse().toString();
                revs.put(key, revs.getOrDefault(key, 0) + 1);
                if (word.charAt(0) == word.charAt(1)) {
                    same += 1;
                }
            }
        }

        return 4 * rev + (same > 0 ? 2 : 0);
    }
}
