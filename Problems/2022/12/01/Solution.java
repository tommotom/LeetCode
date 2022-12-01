class Solution {
    final static Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
    public boolean halvesAreAlike(String s) {
        int half = s.length() / 2;
        int count = 0;
        for (int i = 0; i < half; i++) {
            if (vowels.contains(s.charAt(i))) {
                count++;
            }
        }
        for (int i = half; i < s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                count--;
            }
        }
        return count == 0;
    }
}
