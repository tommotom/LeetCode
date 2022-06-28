class Solution {
  public int minDeletions(String s) {
    HashMap<Character, Integer> count = new HashMap<>();
    int max = 0;
    for (char c : s.toCharArray()) {
      count.put(c, count.getOrDefault(c, 0) + 1);
      max = Math.max(max, count.get(c));
    }

    HashMap<Integer, Integer> countToChars= new HashMap<>();
    for (char c : count.keySet()) {
      int i = count.get(c);
      countToChars.put(i, countToChars.getOrDefault(i, 0) + 1);
    }

    int ans = 0;
    int over = 0;
    for (int i = max; i > 0; i--) {
      int thisLevel = countToChars.getOrDefault(i, 0);
      ans += Math.max(over + thisLevel - 1, 0);
      over = Math.max(over + thisLevel - 1, 0);
    }
    return ans;
  }
}
