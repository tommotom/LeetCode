class Solution {
  public boolean hasAllCodes(String s, int k) {
    int val = 0;
    for (int i = 0; i < k && i < s.length(); i++) {
      val <<= 1;
      val += Character.getNumericValue(s.charAt(i));
    }
    Set<Integer> set = new HashSet<>();
    set.add(val);

    int maxDigit = 1 << k;
    for (int i = k; i < s.length(); i++) {
      val -= Character.getNumericValue(s.charAt(i-k)) << (k-1);
      val <<= 1;
      val += Character.getNumericValue(s.charAt(i));
      set.add(val);
    }
    return set.size() == maxDigit;
  }
}
