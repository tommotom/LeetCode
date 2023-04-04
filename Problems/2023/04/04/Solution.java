class Solution {
    public int partitionString(String s) {
        Set<Character> seen = new HashSet<>();
        int ans = 1;
        for (char c : s.toCharArray()) {
            if (seen.contains(c)) {
                seen = new HashSet<>();
                ans++;
            }
            seen.add(c);
        }
        return ans;
    }
}
