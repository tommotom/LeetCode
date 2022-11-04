class Solution {
    public String reverseVowels(String s) {
        Set<Character> v = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        char[] vowels = new char[s.length()];
        int i = 0;
        for (char c : s.toCharArray()) {
            if (v.contains(c)) {
                vowels[i++] = c;
            }
        }

        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (v.contains(c)) {
                ans.append(vowels[--i]);
            }
            else {
                ans.append(c);
            }
        }

        return ans.toString();
    }
}
