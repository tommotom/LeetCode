class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>(List.of('a', 'i', 'u', 'e', 'o'));
        int count = 0;
        for (int i = 0; i < k; i++) {
            if (vowels.contains(s.charAt(i))) {
                count++;
            }
        }
        int ans = count;
        for (int i = k; i < s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                count++;
            }
            if (vowels.contains(s.charAt(i-k))) {
                count--;
            }
            ans = Math.max(ans, count);
        }
        return ans;
    }
}
