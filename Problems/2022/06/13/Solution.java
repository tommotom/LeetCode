class Solution {
  public int minimumTotal(List<List<Integer>> triangle) {
    for (int i = 1; i < triangle.size(); i++) {
      List<Integer> prev = triangle.get(i-1);
      List<Integer> row = triangle.get(i);
      for (int j = 0; j < row.size(); j++) {
        int tmp = Integer.MAX_VALUE;
        if (j < prev.size()) {
          tmp = prev.get(j);
        }
        if (j > 0) {
          tmp = Math.min(tmp, prev.get(j-1));
        }
        row.set(j, row.get(j)+tmp);
      }
    }
    return triangle.get(triangle.size()-1).stream().min(Comparator.naturalOrder()).get();
  }
}
