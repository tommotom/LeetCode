class Solution {

  private int[] houses;
  private int[][] cost;
  private Integer[][][] memo = new Integer[100][100][21];
  private int m;
  private int n;
  private int target;
  private int MAX_COST = 1000001;

  public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
    this.houses = houses;
    this.cost = cost;
    this.m = m;
    this.n = n;
    this.target = target;

    int ans = helper(0, 0, 0);
    return ans == MAX_COST ? -1 : ans;
  }

  private int helper(int i, int parts, int prevColor) {
    if (i == m) {
      return parts == target ? 0 : MAX_COST;
    }
    if (parts > target) {
      return MAX_COST;
    }
    if (memo[i][parts][prevColor] != null) {
      return memo[i][parts][prevColor];
    }

    int ret = MAX_COST;
    if (houses[i] != 0) {
      if (prevColor != houses[i]) {
        ret = helper(i+1, parts+1, houses[i]);
      } else {
        ret = helper(i+1, parts, houses[i]);
      }
    } else {
      for (int j = 0; j < n; j++) {
        houses[i] = j+1;
        if (prevColor != houses[i]) {
          ret = Math.min(ret, helper(i+1, parts+1, houses[i]) + cost[i][j]);
        } else {
          ret = Math.min(ret, helper(i+1, parts, houses[i]) + cost[i][j]);
        }
      }
      houses[i] = 0;
    }
    memo[i][parts][prevColor] = ret;
    return ret;
  }
}
