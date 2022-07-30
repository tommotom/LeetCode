class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> counter = new HashMap<>();
        for (char c : s.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0)+1);
        }
        for (char c : t.toCharArray()) {
            counter.put(c, counter.getOrDefault(c, 0)-1);
        }

        for (char c : counter.keySet()) {
            if (counter.get(c) != 0) {
                return false;
            }
        }
        return true;
    }
}
