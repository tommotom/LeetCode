class Solution {

  HashMap<Integer, Integer>[] visited;

  public int countVowelStrings(int n) {
    visited = new HashMap[n+1];
    return helper(n, 0);
  }

  private int helper(int n, int i) {
    if (n == 0) {
      return 0;
    }
    if (n == 1) {
      return 5-i;
    }
    if (visited[n] == null) {
      visited[n] = new HashMap<>();
    }
    if (visited[n].containsKey(i)) {
      return visited[n].get(i);
    }
    int ans = 0;
    for (int j = i; j < 5; j++) {
      ans += helper(n-1, j);
    }
    visited[n].put(i, ans);
    return ans;
  }
}
