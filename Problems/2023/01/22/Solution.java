class Solution {

    private final List<List<String>> ans = new ArrayList<>();
    private String s;

    public List<List<String>> partition(String s) {
        this.s = s;
        helper(0, new ArrayList<>());
        return ans;
    }

    private void helper(int i, List<String> list) {
        if (i == s.length()) {
            ans.add(new ArrayList<>(list));
            return;
        }
        for (int j = i+1; j <= s.length(); j++) {
            if (isPalindrome(s.substring(i, j))) {
                list.add(s.substring(i, j));
                helper(j, list);
                list.remove(list.size()-1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        for (int i = 0; i < s.length() / 2; i++) {
            if (s.charAt(i) != s.charAt(s.length()-i-1)) {
                return false;
            }
        }
        return true;
    }
}
