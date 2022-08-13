class Solution {
    private int len;
    private Map<Integer, String> strAt = new HashMap<>();
    private String s;

    public List<Integer> findSubstring(String s, String[] words) {
        len = words[0].length();
        this.s = s;
        Map<String, Integer> counter = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }
        for (int i = 0; i <= s.length()-len; i++) {
            if (counter.containsKey(s.substring(i, i+len))) {
                strAt.put(i, s.substring(i, i+len));
            }
        }

        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= s.length()-(len*words.length); i++) {
            if (dfs(i, new HashMap<String, Integer>(counter))) {
                ans.add(i);
            }
        }
        return ans;
    }

    private boolean dfs(int i, Map<String, Integer> left) {
        if (i <= s.length() && isAllZero(left)) return true;
        if (i >= s.length()) return false;
        if (!strAt.containsKey(i)) return false;
        String word = strAt.get(i);
        if (left.get(word) == 0) return false;
        left.put(word, left.get(word)-1);
        return dfs(i+len, left);
    }

    private boolean isAllZero(Map<String, Integer> left) {
        for (String key : left.keySet()) {
            if (left.get(key) != 0) {
                return false;
            }
        }
        return true;
    }
}
