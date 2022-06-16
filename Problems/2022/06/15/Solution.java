class Solution {
  public int longestStrChain(String[] words) {
    Arrays.sort(words, (a, b) -> a.length() - b.length());
    Map<String, Integer> chain = new HashMap<>();
    int ans = 0;
    for (String w : words) {
      chain.put(w, 1);
      for (int i = 0; i < w.length(); i++) {
        StringBuilder sb = new StringBuilder(w);
        String next = sb.deleteCharAt(i).toString();
        if (chain.containsKey(next) && chain.get(next) + 1 > chain.get(w)) {
          chain.put(w, chain.get(next)+1);
        }
      }
      ans = Math.max(ans, chain.get(w));
    }
    return ans;
  }
}
