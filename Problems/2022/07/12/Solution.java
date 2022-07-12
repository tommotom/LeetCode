class Solution {

  private int[] lengthes = new int[4];
  private int[] matchsticks;
  private int edge;


  public boolean makesquare(int[] matchsticks) {
    int sum = Arrays.stream(matchsticks).sum();
    if (sum % 4 != 0) {
      return false;
    }
    int edge = sum / 4;

    Arrays.sort(matchsticks);
    this.matchsticks = matchsticks;
    this.edge = edge;
    return dfs(matchsticks.length-1);
  }

  private boolean dfs(int i) {
    if (i == -1) {
      return true;
    }
    for (int j = 0; j < 4; j++) {
      if (lengthes[j] + matchsticks[i] > edge) {
        continue;
      }
      lengthes[j] += matchsticks[i];
      if (dfs(i-1)) {
        return true;
      }
      lengthes[j] -= matchsticks[i];
    }
    return false;
  }
}
