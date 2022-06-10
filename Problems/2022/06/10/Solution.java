class Solution {
  public int lengthOfLongestSubstring(String s) {
    int[] last = new int[128];
    int validFrom = -1, ans = 0;
    Arrays.fill(last, -1);
    for (int i = 0; i < s.length(); i++) {
      int j = s.charAt(i) - ' ';
      validFrom = Math.max(validFrom, last[j] + 1);
      last[j] = i;
      ans = Math.max(ans, i-validFrom+1);
    }
    return ans;
  }
}
