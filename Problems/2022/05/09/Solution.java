class Solution {

  HashMap<Character, String> mapping = new HashMap<>();

  public List<String> letterCombinations(String digits) {
    mapping.put('2', "abc");
    mapping.put('3', "def");
    mapping.put('4', "ghi");
    mapping.put('5', "jkl");
    mapping.put('6', "mno");
    mapping.put('7', "pqrs");
    mapping.put('8', "tuv");
    mapping.put('9', "wxyz");

    StringBuilder sb = new StringBuilder();
    List<String> ans = new ArrayList();

    if (digits.isEmpty()) {
      return ans;
    }

    helper(digits, 0, sb, ans);

    return ans;
  }

  private void helper(String digits, int i, StringBuilder sb, List<String> ans) {
    if (i == digits.length()) {
      ans.add(sb.toString());
      return;
    }

    String s = mapping.get(digits.charAt(i));
    for (int j = 0; j < s.length(); j++) {
      sb.append(s.charAt(j));
      helper(digits, i+1, sb, ans);
      sb.setLength(sb.length() - 1);
    }
  }
}
