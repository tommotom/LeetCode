class Costs implements Comparable<Costs> {
  int a;
  int b;

  public Costs(int[] cost) {
    a = cost[0];
    b = cost[1];
  }

  @Override
  public int compareTo(Costs c) {
    return Integer.compare(a-b, c.a - c.b);
  }
}

class Solution {
  public int twoCitySchedCost(int[][] costs) {
    List<Costs> c = new ArrayList<>();
    for (int i = 0; i < costs.length; i++) {
      c.add(new Costs(costs[i]));
    }
    Collections.sort(c);
    int n = costs.length / 2, ans = 0;
    for (int i = 0; i < n; i++) {
      ans += c.get(i).a;
    }

    for (int i = n; i < costs.length; i++) {
      ans += c.get(i).b;
    }

    return ans;
  }
}
