class Solution {

    private final Map<Character, Integer> map = new HashMap<>();

    public boolean isAlienSorted(String[] words, String order) {
        for (int i = 0; i < order.length(); i++) {
            map.put(order.charAt(i), i);
        }

        for (int i = 1; i< words.length; i++) {
            if (compare(words[i-1], words[i]) == 1) {
                return false;
            }
        }
        return true;
    }

    private int compare(String a, String b) {
        for (int i = 0; i < a.length(); i++) {
            if (i == b.length()) {
                return 1;
            }
            if (map.get(a.charAt(i)) < map.get(b.charAt(i))) {
                return -1;
            } else if (map.get(a.charAt(i)) > map.get(b.charAt(i))) {
                return 1;
            }
        }

        if (a.length() == b.length()) {
            return 0;
        }
        return -1;
    }
}
