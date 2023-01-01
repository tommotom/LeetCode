class Solution {
    public boolean wordPattern(String pattern, String s) {
        Map<Character, String> a = new HashMap<>();
        Map<String, Character> b = new HashMap<>();
        int i = 0;
        for (String str : s.split(" ")) {
            if (i == pattern.length()) {
                return false;
            }
            if (a.containsKey(pattern.charAt(i)) && !a.get(pattern.charAt(i)).equals(str)) {
                return false;
            }
            a.put(pattern.charAt(i), str);
            if (b.containsKey(str) && b.get(str) != pattern.charAt(i)) {
                return false;
            }
            b.put(str, pattern.charAt(i));
            i++;
        }
        return i == pattern.length();
    }
}
