class Solution {
  public int maxProduct(String[] words) {
    int n = words.length;
    int[] masks = new int[n];
    for (int i = 0; i < n; i++) {
      for (Character c : words[i].toCharArray()) {
        masks[i] |= 1 << (c - 'a');
      }
    }

    int ans = 0;
    for (int i = 1; i < n; i++) {
      for (int j = 0; j < i; j++) {
        if ((masks[i] & masks[j]) == 0) {
          ans = Math.max(ans, words[i].length() * words[j].length());
        }
      }
    }
    return ans;
  }
}
